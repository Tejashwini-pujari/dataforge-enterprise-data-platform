import pandas as pd
import re
from logger_config import logger


def validate_log_data(df):
    """
    Validate website log data.
    """

    print("\n" + "=" * 50)
    print("LOG DATA VALIDATION REPORT")
    print("=" * 50)

    logger.info("Starting Log Data Validation")

    for index, row in df.iterrows():

        row_number = index + 1

        # -------------------------------
        # Validate Timestamp
        # -------------------------------
        try:
            pd.to_datetime(
                row["timestamp"],
                format="%Y-%m-%d %H:%M:%S"
            )
        except Exception:
            print(f"Row {row_number} -> Invalid Timestamp")
            logger.warning(f"Row {row_number}: Invalid Timestamp")

        # -------------------------------
        # Validate IP Address
        # -------------------------------
        ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"

        if not re.match(ip_pattern, str(row["ip_address"])):
            print(f"Row {row_number} -> Invalid IP Address")
            logger.warning(f"Row {row_number}: Invalid IP Address")

        # -------------------------------
        # Validate URL
        # -------------------------------
        if str(row["url"]).strip() == "":
            print(f"Row {row_number} -> Missing URL")
            logger.warning(f"Row {row_number}: Missing URL")

        # -------------------------------
        # Validate Status Code
        # -------------------------------
        status = str(row["status_code"])

        if not status.isdigit():
            print(f"Row {row_number} -> Invalid Status Code")
            logger.warning(f"Row {row_number}: Invalid Status Code")

    logger.info("Log Data Validation Completed")