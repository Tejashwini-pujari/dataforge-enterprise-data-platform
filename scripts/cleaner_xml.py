import pandas as pd
from logger_config import logger



def clean_employee_data(df):
    """
    Cleans employee dataset.
    """

    logger.info("Starting Employee Data Cleaning")

    clean_df = df.copy()

    # -------------------------------
    # Fill Missing Values
    # -------------------------------

    clean_df["employee_name"] = clean_df["employee_name"].fillna("Unknown")
    clean_df["department"] = clean_df["department"].fillna("General")
    clean_df["city"] = clean_df["city"].fillna("Unknown")
    clean_df["salary"] = clean_df["salary"].fillna(0)

    # Replace blank values
    clean_df["employee_name"] = clean_df["employee_name"].replace("", "Unknown")
    clean_df["department"] = clean_df["department"].replace("", "General")
    clean_df["city"] = clean_df["city"].replace("", "Unknown")

    # -------------------------------
    # Remove Duplicate Employees
    # -------------------------------

    before = len(clean_df)

    clean_df = clean_df.drop_duplicates(subset=["employee_id"])

    after = len(clean_df)

    logger.info(f"Removed {before-after} duplicate employees")

    # -------------------------------
    # Standardize Text
    # -------------------------------

    clean_df["employee_name"] = (
        clean_df["employee_name"]
        .str.strip()
        .str.title()
    )

    clean_df["department"] = (
        clean_df["department"]
        .str.strip()
        .str.title()
    )

    clean_df["city"] = (
        clean_df["city"]
        .str.strip()
        .str.title()
    )

    logger.info("Employee Data Cleaning Completed")

    return clean_df


def save_clean_employees(df, output_path):
    """
    Save cleaned employee data to XML.
    """

    df.to_xml(
        output_path,
        index=False,
        root_name="employees",
        row_name="employee"
    )

    logger.info(f"Clean employee data saved to {output_path}")