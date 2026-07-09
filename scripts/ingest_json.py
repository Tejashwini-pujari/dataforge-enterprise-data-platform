import pandas as pd
from logger_config import logger
from validator_json import validate_customer_data
from cleaner_json import clean_customer_data, save_clean_customers


def read_customer_data(file_path):
    """
    Reads customer JSON file and returns a DataFrame.
    """

    try:
        logger.info(f"Reading JSON file: {file_path}")

        df = pd.read_json(file_path)

        print("=" * 50)
        print("CUSTOMER DATA LOADED SUCCESSFULLY")
        print("=" * 50)

        logger.info(f"Successfully loaded {len(df)} customer records")

        return df

    except Exception as e:
        logger.error(f"Error reading JSON file: {e}")
        print(f"Error: {e}")
        return None


def customer_quality_report(df):
    """
    Displays basic data quality report.
    """

    logger.info("Generating Customer Data Quality Report")

    print("\n" + "=" * 50)
    print("CUSTOMER DATA QUALITY REPORT")
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

    logger.info("Customer Data Quality Report Generated Successfully")


if __name__ == "__main__":

    file_path = "data/raw/customers.json"

    customer_df = read_customer_data(file_path)

    if customer_df is not None:

        customer_quality_report(customer_df)

        validate_customer_data(customer_df)

        clean_df = clean_customer_data(customer_df)

        save_clean_customers(
            clean_df,
            "data/processed/clean_customers.json"
        )