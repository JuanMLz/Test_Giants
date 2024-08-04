import os
import requests
import glob
import pandas as pd
from datetime import date


class CalcSelic:
    def __init__(self):
        self._PATH = os.path.abspath(os.getcwd())

    def is_valid_input(self, start_date: date, end_date: date) -> list:

        if isinstance(start_date, (date)) and isinstance(end_date, (date)):
            if start_date >= end_date:
                raise Exception('start_date cannot be greater than end_date')

            start_date = start_date.strftime('%d/%m/%Y')
            end_date = end_date.strftime('%d/%m/%Y')
            return [start_date, end_date]

        else:
            raise Exception('Inputs are in wrong format, shoud be date object')
        return

    def reshape_df(self, df: pd.DataFrame, frequency: str) -> pd.DataFrame:
        df.set_index('data', inplace=True)

        if frequency == 'month':
            df = df.groupby([df.index.year, df.index.month]).tail(1)
        elif frequency == 'year':
            df = df.groupby([df.index.year]).tail(1)

        df = df.sort_index()
        df["Amount earned"] = df["compound"] - self.capital
        df.drop(['valor'], axis='columns', inplace=True)
        df.rename(columns={'compound': 'Capital'}, inplace=True)
        df.index.names = ['Date']

        return df

    def calc_sum(self, start_date, end_date, df):
        _df = df[(df['data'] >= start_date) & (df['data'] <= end_date)].copy()
        _df.loc[:, 'x'] = self.capital
        _df['x'] = self.capital * _df['valor'].shift().add(1).cumprod().fillna(1)
        val = _df.iloc[-1]['x']
        return val

    def max_val_range(self, df, range_of=500):
        length = len(df.index) - range_of + 1
        best_start = None
        best_end = None
        best_value = 0

        for i in range(0, length):
            start = df.iloc[i]['data']
            end = start + pd.DateOffset(days=range_of)
            value = self.calc_sum(start, end, df)

            if value > best_value:
                best_start = start
                best_end = end
                best_value = value
                best_df = df[(df['data'] >= best_start) & (df['data'] <= best_end)]

        print(
            f'\nThe best day to invest is {best_start.date()},'
            f'with an amount earned of {best_value} after {range_of}'
            f'days ({best_start.date()} to {best_end.date()})'
        )

        return best_df

    def save_csv(self, df, file_name):
        files_present = glob.glob(file_name)
        if not files_present:
            df.to_csv(file_name)
            print(f'Path to csv output: {self._PATH}/{file_name}')
        else:
            print('File already exists, ignoring')

    def calc_amount(
            self,
            start_date: date,
            end_date: date,
            capital: float,
            frequency: str,
            save_csv: bool,
    ) -> pd.DataFrame:
        self.capital = capital
        start_date, end_date = self.is_valid_input(start_date, end_date)
        base_url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&"
        date_range_str = f'dataInicial={start_date}&dataFinal={end_date}'
        url = base_url + date_range_str

        try:
            resp = requests.get(url)
            df = pd.read_json(resp.text)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return pd.DataFrame()

        df['data'] = pd.to_datetime(df['data'], format="%d/%m/%Y")
        df['valor'] = pd.to_numeric(df['valor'])
        df.drop_duplicates(subset='data', inplace=True)
        df.sort_values(by=['data'], inplace=True)
        if df.iloc[0]["data"] < pd.to_datetime(start_date):
            df.drop(index=df.index[0], axis=0, inplace=True)
        df['valor'] = df['valor'] / 100
        df_raw = df.copy()
        df['compound'] = capital * (1 + df['valor'].shift()).cumprod().fillna(1)

        best_df = self.max_val_range(df)
        sol_df = self.reshape_df(best_df, frequency)

        if save_csv:
            self.save_csv(sol_df, file_name=f'solution_{frequency}.csv')
            self.save_csv(df_raw, file_name='df_raw.csv')

        return sol_df
