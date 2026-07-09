import pandas as pd
from logger_config import logger



def merge_sales_customers(sales_file, customer_file):
    """
    Merge sales and customer data using customer_id.
    """

    logger.info("Reading cleaned sales data")
    sales_df = pd.read_csv(sales_file)

    logger.info("Reading cleaned customer data")
    customer_df = pd.read_json(customer_file)

    logger.info("Merging sales and customer data")

    merged_df = pd.merge(
        sales_df,
        customer_df,
        on="customer_id",
        how="left"
    )

    print("\n" + "=" * 50)
    print("MERGED DATA")
    print("=" * 50)

    print(merged_df.head())

    logger.info("Data merged successfully")

    return merged_df


def save_merged_data(df, output_path):
    """
    Save merged data to CSV.
    """

    df.to_csv(output_path, index=False)

    logger.info(f"Merged data saved to {output_path}")


if __name__ == "__main__":

    merged_df = merge_sales_customers(
        "data/processed/clean_sales.csv",
        "data/processed/clean_customers.json"
    )

    save_merged_data(
        merged_df,
        "data/processed/final_sales_report.csv"
    )