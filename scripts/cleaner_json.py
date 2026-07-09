import pandas as pd
from logger_config import logger



def clean_customer_data(df):
    """
    Cleans customer dataset.
    """

    logger.info("Starting Customer Data Cleaning")

    clean_df = df.copy()

    # -------------------------------
    # Fill Missing Values
    # -------------------------------

    clean_df["customer_name"] = clean_df["customer_name"].fillna("Unknown")
    clean_df["email"] = clean_df["email"].fillna("Not Available")
    clean_df["phone"] = clean_df["phone"].fillna("0000000000")
    clean_df["city"] = clean_df["city"].fillna("Unknown")

    # Replace blank values
    clean_df["customer_name"] = clean_df["customer_name"].replace("", "Unknown")
    clean_df["email"] = clean_df["email"].replace("", "Not Available")
    clean_df["phone"] = clean_df["phone"].replace("", "0000000000")

    # -------------------------------
    # Remove Duplicate Customers
    # -------------------------------

    before = len(clean_df)

    clean_df = clean_df.drop_duplicates(subset=["customer_id"])

    after = len(clean_df)

    logger.info(f"Removed {before-after} duplicate customers")

    # -------------------------------
    # Standardize Text
    # -------------------------------

    clean_df["customer_name"] = (
        clean_df["customer_name"]
        .str.strip()
        .str.title()
    )

    clean_df["city"] = (
        clean_df["city"]
        .str.strip()
        .str.title()
    )

    clean_df["email"] = (
        clean_df["email"]
        .str.strip()
        .str.lower()
    )

    logger.info("Customer Data Cleaning Completed")

    return clean_df


def save_clean_customers(df, output_path):

    df.to_json(
        output_path,
        orient="records",
        indent=4
    )

    logger.info(f"Clean customer data saved to {output_path}")