import pandas as pd
import re
from logger_config import logger



def validate_customer_data(df):
    """
    Validate customer data and print row-level issues.
    """

    print("\n" + "=" * 50)
    print("CUSTOMER DATA VALIDATION REPORT")
    print("=" * 50)

    logger.info("Starting Customer Data Validation")

    # -------------------------------
    # Check Duplicate Customer IDs
    # -------------------------------
    duplicate_ids = df[df.duplicated(subset=["customer_id"], keep=False)]

    if not duplicate_ids.empty:
        print("\nDuplicate Customer IDs Found:")
        print(duplicate_ids["customer_id"].tolist())
        logger.warning(
            f"Duplicate Customer IDs Found: {duplicate_ids['customer_id'].tolist()}"
        )

    # -------------------------------
    # Row-by-row Validation
    # -------------------------------
    for index, row in df.iterrows():

        customer_id = row["customer_id"]

        # Missing Customer Name
        if pd.isna(row["customer_name"]) or str(row["customer_name"]).strip() == "":
            print(f"Customer {customer_id} -> Missing Customer Name")
            logger.warning(f"Customer {customer_id}: Missing Customer Name")

        # Missing Email
        if pd.isna(row["email"]) or str(row["email"]).strip() == "":
            print(f"Customer {customer_id} -> Missing Email")
            logger.warning(f"Customer {customer_id}: Missing Email")

        # Invalid Email
        elif not re.match(
            r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
            str(row["email"])
        ):
            print(f"Customer {customer_id} -> Invalid Email")
            logger.warning(f"Customer {customer_id}: Invalid Email")

        # Missing Phone
        if pd.isna(row["phone"]) or str(row["phone"]).strip() == "":
            print(f"Customer {customer_id} -> Missing Phone")
            logger.warning(f"Customer {customer_id}: Missing Phone")

        # Invalid Phone Number
        elif not (
            str(row["phone"]).isdigit() and len(str(row["phone"])) == 10
        ):
            print(f"Customer {customer_id} -> Invalid Phone Number")
            logger.warning(f"Customer {customer_id}: Invalid Phone Number")

        # Missing City
        if pd.isna(row["city"]) or str(row["city"]).strip() == "":
            print(f"Customer {customer_id} -> Missing City")
            logger.warning(f"Customer {customer_id}: Missing City")

    logger.info("Customer Data Validation Completed")