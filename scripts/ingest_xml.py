import pandas as pd
from logger_config import logger
from validator_xml import validate_employee_data
from cleaner_xml import clean_employee_data, save_clean_employees


def read_employee_data(file_path):
    """
    Reads employee XML file and returns a DataFrame.
    """

    try:
        logger.info(f"Reading XML file: {file_path}")

        df = pd.read_xml(file_path)

        print("=" * 50)
        print("EMPLOYEE DATA LOADED SUCCESSFULLY")
        print("=" * 50)

        logger.info(f"Successfully loaded {len(df)} employee records")

        return df

    except Exception as e:
        logger.error(f"Error reading XML file: {e}")
        print(f"Error: {e}")
        return None


def employee_quality_report(df):
    """
    Displays basic data quality report.
    """

    logger.info("Generating Employee Data Quality Report")

    print("\n" + "=" * 50)
    print("EMPLOYEE DATA QUALITY REPORT")
    print("=" * 50)

    print(f"\nTotal Rows    : {df.shape[0]}")
    print(f"Total Columns : {df.shape[1]}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

    print("\nData Types:")
    print(df.dtypes)

    logger.info("Employee Data Quality Report Generated Successfully")


if __name__ == "__main__":

    file_path = "data/raw/employees.xml"

    employee_df = read_employee_data(file_path)

    if employee_df is not None:

        employee_quality_report(employee_df)

        validate_employee_data(employee_df)

        clean_df = clean_employee_data(employee_df)

        save_clean_employees(
            clean_df,
            "data/processed/clean_employees.xml"
        )