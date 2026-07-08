


# import pandas as pd
# from logger_config import logger


# def read_sales_data(file_path):
#     """
#     Reads the sales CSV file and returns a Pandas DataFrame.
#     """
#     try:
#         df = pd.read_csv(file_path)
#         print("=" * 50)
#         print("Sales Data Loaded Successfully")
#         print("=" * 50)
#         return df

#     except Exception as e:
#         print(f"Error reading file: {e}")
#         return None


# def data_quality_report(df):
#     """
#     Displays basic data quality checks.
#     """

#     print("\n" + "=" * 50)
#     print("DATA QUALITY REPORT")
#     print("=" * 50)

#     print(f"\nTotal Rows    : {df.shape[0]}")
#     print(f"Total Columns : {df.shape[1]}")

#     print("\nColumn Names:")
#     print(df.columns.tolist())

#     print("\nMissing Values:")
#     print(df.isnull().sum())

#     print("\nDuplicate Rows:")
#     print(df.duplicated().sum())

#     print("\nData Types:")
#     print(df.dtypes)


# if __name__ == "__main__":
#     file_path = "data/raw/sales.csv"

#     sales_df = read_sales_data(file_path)

#     if sales_df is not None:
#         data_quality_report(sales_df)

import pandas as pd
from logger_config import logger
from validator import validate_data
from cleaner import clean_data, save_clean_data


def read_sales_data(file_path):
    """
    Reads the sales CSV file and returns a Pandas DataFrame.
    """

    try:
        logger.info(f"Reading file: {file_path}")

        df = pd.read_csv(file_path)

        logger.info(f"Successfully loaded {len(df)} records")

        print("=" * 50)
        print("Sales Data Loaded Successfully")
        print("=" * 50)

        return df

    except Exception as e:
        logger.error(f"Error reading file: {e}")

        print(f"Error reading file: {e}")
        return None


def data_quality_report(df):
    """
    Displays basic data quality checks.
    """

    logger.info("Generating Data Quality Report")

    print("\n" + "=" * 50)
    print("DATA QUALITY REPORT")
    print("=" * 50)

    print(f"\nTotal Rows    : {df.shape[0]}")
    print(f"Total Columns : {df.shape[1]}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nData Types:")
    print(df.dtypes)

    logger.info("Data Quality Report Generated Successfully")


if __name__ == "__main__":

    file_path = "data/raw/sales.csv"

    sales_df = read_sales_data(file_path)

    if sales_df is not None:
        data_quality_report(sales_df)
        validate_data(sales_df)
        
    
        cleaned_df = clean_data(sales_df)

        save_clean_data(
            cleaned_df,
            "data/processed/clean_sales.csv"
        )