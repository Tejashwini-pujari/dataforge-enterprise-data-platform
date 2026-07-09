import pandas as pd
from logger_config import logger



def clean_log_data(df):
    """
    Cleans website log dataset.
    """

    logger.info("Starting Log Data Cleaning")

    clean_df = df.copy()

    # -------------------------------
    # Remove Invalid IP Address
    # -------------------------------
    clean_df = clean_df[
        clean_df["ip_address"] != "INVALID_IP"
    ]

    # -------------------------------
    # Remove Missing URL
    # -------------------------------
    clean_df = clean_df[
        clean_df["url"].str.strip() != ""
    ]

    # -------------------------------
    # Keep Only Numeric Status Codes
    # -------------------------------
    clean_df = clean_df[
        clean_df["status_code"].astype(str).str.isdigit()
    ]

    # -------------------------------
    # Convert Data Types
    # -------------------------------
    clean_df["timestamp"] = pd.to_datetime(
        clean_df["timestamp"],
        format="%Y-%m-%d %H:%M:%S",
        errors="coerce"
    )

    clean_df["status_code"] = clean_df["status_code"].astype(int)

    # -------------------------------
    # Remove Duplicate Records
    # -------------------------------
    before = len(clean_df)

    clean_df = clean_df.drop_duplicates()

    after = len(clean_df)

    logger.info(f"Removed {before-after} duplicate records")

    logger.info("Log Data Cleaning Completed")

    return clean_df


def save_clean_logs(df, output_path):
    """
    Save cleaned logs to CSV.
    """

    df.to_csv(
        output_path,
        index=False
    )

    logger.info(f"Clean log data saved to {output_path}")