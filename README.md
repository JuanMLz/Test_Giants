# Giants Steps Capital Test

## Technical Test: Financial Investment Analysis

### Challenge Overview

In this technical test, the task is to identify and fix problems in the existing code base from the previous implementation. The key challenge is to improve the code and ensure that it can accurately determine the most profitable period for investment.

### Task Description

The goal is to answer the following question:
- Which 500 calendar day period from January 1, 2010 to March 1, 2021 was the most profitable? More specifically, if an initial capital of 657.43 was invested, which period within that period was the most profitable?

The expected outcome of this challenge is to identify the most profitable period, which is from June 16, 2015 to October 28, 2016, which has a return of 787.952750655493.


## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/JuanMLz/Test_Giants

2. **Create and activate a Virtual Environment**

    ```bash
    python -m venv venv

    venv\Scripts\activate

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```


### Implementation Steps

1. **Code Fixes**: The initial code, created by a previous implementation named 'Bot', contained errors that prevented it from producing the correct results. My task was to debug and fix these issues to ensure accurate calculations.

   **The Bugs**

- **Removal of unused imports:** Unused imports (such as Timedelta) have been removed to clean up the code and improve efficiency.

- **Duplicate arguments in is_valid_input:** The is_valid_input method had a duplicate argument issue where the start_date argument was repeated. This caused the method to not correctly check the end_date. Fixed it by naming the arguments correctly.

- **DataFrame copy issue in calc_sum:** The calc_sum method directly modified the DataFrame "_df", which could cause issues. The solution is to use .copy() of _df before making the changes to ensure the original data is not affected.

- **Incorrect method name in max_val_range:** In max_val_range, the method name for calling calc_sum was incorrect, causing an error. Use the correct method name to fix this.

- **Incorrect number of days in max_val_range:** The method incorrectly counted the number of rows instead of the actual number of calendar days, causing an inaccurate 500-day period. The logic has been updated to ensure that 500 calendar days are accurately considered.


2. **Code Enhancement**: In addition to fixing bugs, I improved the code's robustness and maintainability. This included restructuring the code to facilitate easier updates and enhancements.

    **The changes**

- **Merged Functionality in reshape_df:** The "earned" method was only adding a column to the DataFrame, which was used in reshape_df. I integrated this functionality directly into "reshape_df" and removed the earned method.

- **Removed Redundant "compound_interest" Method:** The "compound_interest" method was redundant because the same column was already created in the "calc_amount" method. Therefore, I removed the "compound_interest" method.

- **Simplified "is_valid_input" Method:** The frequency parameter in "is_valid_input" was not used, so I removed it. Additionally, the check for capital inside "is_valid_input" was unnecessary and was also removed.

- **Refactored Compound Interest Calculation in "calc_amount":** I streamlined the line of code for calculating compound interest in "calc_amount" to make it more direct and readable.

- **Introduced best_df in "max_val_range":** I created a new DataFrame, "best_df", containing the results of the 500-day period with the best investment return. This makes it easier to iterate over this DataFrame in other methods.

- **Added Error Handling for API Connection:** I added a try-except block in "calc_amount" to handle potential API connection errors gracefully.

- **Improved Column Creation in "calc_amount":** I refined the line of code that creates the "compound" column for better readability.

- **Removed Redundant run_example Method:** The "run_example" method was removed because the "calc_amount" method is already called in the main code, making it redundant.

- **Added Frequency-Based CSV Creation:** In the main class "calc_amount", I added calls for daily, monthly, and yearly frequencies, each creating a distinct CSV file.


3. **Unit Testing**: I implemented unit tests to ensure the correctness of the code and prevent similar issues in the future. This step was crucial to verify that the fixes and enhancements did not introduce new bugs.

    **The tests**

- The *test_is_valid_input* method checks three cases. First, it checks for valid data to make sure it is in the correct format. Second, it checks what happens if the start date is later than the end date and expects an error message. Finally, it checks for invalid date formats (strings instead of dates) to make sure the method throws an error on incorrect input types.

- The *test_reshape_df_invalid_Frequency* method tests how the code handles invalid frequency values. If an unsupported frequency is specified, an error is raised.


## How the code works

The main method of the code is *calc_amount*, which orchestrates the entire process of calculating the most profitable investment period. Here is a step-by-step overview of how it operates:

**- Data Extraction and Filtering:**
The "calc_amount" method starts by extracting data from an API. It constructs a URL based on the provided start and end dates, which filters the data to the specific period required by the technical test.
The API response is then converted into a DataFrame.

**- Input Validation:**
The "is_valid_input" method is used to ensure that the start and end dates are of the correct type and format. This validation is crucial for preventing errors in subsequent calculations.

**- Calculation of Compound Interest:**
Within "calc_amount", the compound interest is calculated using the given capital and the extracted data. This involves computing the accumulated value over time.

**- Determining the Most Profitable Period:**
The "max_val_range" method is called to identify the 500-day period with the highest return. This method processes the DataFrame to find the optimal investment period.

**- Data Formatting:**
After identifying the best 500 days, the "reshape_df" method is used to format the DataFrame according to the specified frequency (daily, monthly, or yearly).

**- Saving Results:**
Finally, the "save_csv" method saves the resulting DataFrames to CSV files. It creates different files based on the specified frequency, providing a clear output of the results.

By structuring the code in this way, the process from data extraction to result output is streamlined and efficient, ensuring accurate and easy-to-understand results.


## Contributing

This repository is in response to the technical test by Giant Steps Capital. The developers who will review and evaluate this code are: 

- Samuel Rohr (samuelrohr) 
- Vitor Saito (xtatus) 

Any feedback or suggestions for improvements are highly appreciated.

## License

[MIT](https://choosealicense.com/licenses/mit/)