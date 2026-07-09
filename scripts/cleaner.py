import pandas as pd
from logger_config import logger



def clean_data(df):
    """
    Cleans sales dataset.
    """

    logger.info("Starting Data Cleaning")

    clean_df = df.copy()


    # -------------------------------
    # Handle Missing Values
    # -------------------------------

    clean_df["quantity"] = clean_df["quantity"].fillna(0)

    clean_df["price"] = clean_df["price"].fillna(0)

    clean_df["city"] = clean_df["city"].fillna("Unknown")

    clean_df["product"] = clean_df["product"].fillna("Unknown")


    logger.info("Missing values handled")


    # -------------------------------
    # Remove Duplicate Records
    # -------------------------------

    before = len(clean_df)

    clean_df = clean_df.drop_duplicates(
        subset=[
            "customer_id",
            "product",
            "category",
            "quantity",
            "price",
            "sale_date",
            "city"
        ]
    )

    after = len(clean_df)

    logger.info(
        f"Removed {before - after} duplicate records"
    )


    # -------------------------------
    # Standardize Text Columns
    # -------------------------------

    clean_df["city"] = (
        clean_df["city"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    clean_df["product"] = (
        clean_df["product"]
        .astype(str)
        .str.strip()
        .str.title()
    )


    logger.info("Text standardization completed")


    # -------------------------------
    # Convert Date Format
    # -------------------------------

    clean_df["sale_date"] = (
        pd.to_datetime(
            clean_df["sale_date"],
            format="%d-%m-%Y",
            errors="coerce"
        )
        .dt.strftime("%Y-%m-%d")
    )


    logger.info("Date format converted")


    logger.info("Data Cleaning Completed")

    return clean_df



def save_clean_data(df, output_path):
    """
    Saves cleaned data into processed folder.
    """

    df.to_csv(
        output_path,
        index=False
    )

    logger.info(
        f"Clean data saved at {output_path}"
    )