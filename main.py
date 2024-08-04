from solution import CalcSelic

from datetime import date


if __name__ == '__main__':
    calc = CalcSelic()

    calc.calc_amount(
        start_date=date(2010, 1, 1),
        end_date=date(2021, 3, 1),
        capital=657.43,
        frequency='daily',
        save_csv=True,
    )

    calc.calc_amount(
        start_date=date(2010, 1, 1),
        end_date=date(2021, 3, 1),
        capital=657.43,
        frequency='month',
        save_csv=True,
    )

    calc.calc_amount(
        start_date=date(2010, 1, 1),
        end_date=date(2021, 3, 1),
        capital=657.43,
        frequency='year',
        save_csv=True,
    )
