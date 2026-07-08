import pandas as pd
from logger_config import logger


def validate_data(df):
    """
    Validate sales data and print row-level issues.
    """

    print("\n" + "=" * 50)
    print("DATA VALIDATION REPORT")
    print("=" * 50)

    logger.info("Starting Data Validation")

    # -------------------------------
    # Check Duplicate Sale IDs
    # -------------------------------
    duplicate_ids = df[df.duplicated(subset=["sale_id"], keep=False)]

    if not duplicate_ids.empty:
        print("\nDuplicate Sale IDs Found:")
        print(duplicate_ids["sale_id"].tolist())
        logger.warning(
            f"Duplicate Sale IDs Found: {duplicate_ids['sale_id'].tolist()}"
        )

    # -------------------------------
    # Row-by-row Validation
    # -------------------------------
    for index, row in df.iterrows():

        sale_id = row["sale_id"]

        # Missing Quantity
        if pd.isna(row["quantity"]):
            print(f"Sale ID {sale_id} -> Missing Quantity")
            logger.warning(f"Sale ID {sale_id}: Missing Quantity")

        # Invalid Quantity
        elif row["quantity"] <= 0:
            print(f"Sale ID {sale_id} -> Invalid Quantity")
            logger.warning(f"Sale ID {sale_id}: Invalid Quantity")

        # Missing Price
        if pd.isna(row["price"]):
            print(f"Sale ID {sale_id} -> Missing Price")
            logger.warning(f"Sale ID {sale_id}: Missing Price")

        # Invalid Price
        elif row["price"] <= 0:
            print(f"Sale ID {sale_id} -> Invalid Price")
            logger.warning(f"Sale ID {sale_id}: Invalid Price")

        # Missing City
        if pd.isna(row["city"]):
            print(f"Sale ID {sale_id} -> Missing City")
            logger.warning(f"Sale ID {sale_id}: Missing City")

        # Missing Product
        if pd.isna(row["product"]) or str(row["product"]).strip() == "":
            print(f"Sale ID {sale_id} -> Missing Product")
            logger.warning(f"Sale ID {sale_id}: Missing Product")

        # Invalid Customer ID
        if not str(row["customer_id"]).startswith("C"):
            print(f"Sale ID {sale_id} -> Invalid Customer ID")
            logger.warning(f"Sale ID {sale_id}: Invalid Customer ID")

   
        
        # Invalid Sale Date
    try:
        pd.to_datetime(str(row["sale_date"]).strip(), format="%d-%m-%Y")

    except Exception:
        print(f"Sale ID {sale_id} -> Invalid Sale Date")
        logger.warning(f"Sale ID {sale_id}: Invalid Sale Date")

            

    logger.info("Data Validation Completed")