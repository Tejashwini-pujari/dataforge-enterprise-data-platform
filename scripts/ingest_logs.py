import pandas as pd
from logger_config import logger
from validator_logs import validate_log_data
from cleaner_logs import clean_log_data, save_clean_logs


def read_log_data(file_path):
    """
    Reads website log file and returns a DataFrame.
    """

    try:
        logger.info(f"Reading log file: {file_path}")

        data = []

        with open(file_path, "r") as file:
            for line in file:
                parts = [x.strip() for x in line.split("|")]

                if len(parts) == 4:
                    data.append(parts)

        df = pd.DataFrame(
            data,
            columns=[
                "timestamp",
                "ip_address",
                "url",
                "status_code"
            ]
        )

        print("=" * 50)
        print("LOG DATA LOADED SUCCESSFULLY")
        print("=" * 50)

        logger.info(f"Loaded {len(df)} log records")

        return df

    except Exception as e:
        logger.error(e)
        print(e)
        return None


def log_quality_report(df):

    logger.info("Generating Log Data Quality Report")

    print("\n" + "=" * 50)
    print("LOG DATA QUALITY REPORT")
    print("=" * 50)

    print(f"\nRows : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

    print("\nFirst Five Records:")
    print(df.head())


if __name__ == "__main__":

    logs_df = read_log_data(
        "data/raw/website_logs.txt"
    )

    if logs_df is not None:

        log_quality_report(logs_df)

        validate_log_data(logs_df)

        clean_df = clean_log_data(logs_df)

        save_clean_logs(
            clean_df,
            "data/processed/clean_logs.csv"
        )