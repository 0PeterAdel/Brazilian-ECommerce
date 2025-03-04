import pandas as pd
import numpy as np

# -----------------------------------------------
# 1. Define the folder path and load the files
# -----------------------------------------------
root_path = "DataSet/"

# Load the orders file and convert date columns to datetime\orders = pd.read_csv(
orders = pd.read_csv(
    root_path + "olist_orders_dataset.csv",
    parse_dates=[
        "order_purchase_timestamp", 
        "order_approved_at", 
        "order_delivered_carrier_date", 
        "order_delivered_customer_date", 
        "order_estimated_delivery_date"
    ]
)
# Load the order items file
order_items = pd.read_csv(root_path + "olist_order_items_dataset.csv")

# Load the payments file
order_payments = pd.read_csv(root_path + "olist_order_payments_dataset.csv")

# Load the reviews file
order_reviews = pd.read_csv(root_path + "olist_order_reviews_dataset.csv")

# -----------------------------------------------
# 2. Display samples of the data
# -----------------------------------------------
print("----- Orders -----")
print(orders.head(3))
print("\n----- Order Items -----")
print(order_items.head(3))
print("\n----- Order Payments -----")
print(order_payments.head(3))
print("\n----- Order Reviews -----")
print(order_reviews.head(3))

# -----------------------------------------------
# 3. Count and print the number of missing values in each file
# -----------------------------------------------
print("\nMissing values in orders:")
print(orders.isnull().sum())

print("\nMissing values in order_items:")
print(order_items.isnull().sum())

print("\nMissing values in order_payments:")
print(order_payments.isnull().sum())

print("\nMissing values in order_reviews:")
print(order_reviews.isnull().sum())

# -----------------------------------------------
# 4. Calculate the percentage of missing values in the orders file
# -----------------------------------------------
orders_missing_pct = orders.isnull().mean() * 100
print("\nMissing values percentage in orders:\n", orders_missing_pct)

# -----------------------------------------------
# 5. Analyze orders that lack critical values
# -----------------------------------------------
# Analyze orders missing order_approved_at
missing_approved = orders[orders['order_approved_at'].isnull()]
print("\nOrder status distribution for missing order_approved_at:")
print(missing_approved['order_status'].value_counts())

# Analyze orders missing order_delivered_customer_date
missing_delivered = orders[orders['order_delivered_customer_date'].isnull()]
print("\nOrder status distribution for missing order_delivered_customer_date:")
print(missing_delivered['order_status'].value_counts())

# -----------------------------------------------
# 6. Ensure datetime columns are properly converted (revalidation)
# -----------------------------------------------
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'], errors='coerce')
orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'], errors='coerce')
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'], errors='coerce')
orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'], errors='coerce')

# -----------------------------------------------
# 7. Handle missing values in the orders file
# -----------------------------------------------
# (A) Handling order_approved_at:
# Extract delivered orders that lack order_approved_at
delivered_missing_approval = orders[(orders['order_status'] == 'delivered') & (orders['order_approved_at'].isnull())]
print("\nNumber of orders delivered without order_approved_at:", delivered_missing_approval.shape[0])

# Exclude these rows from approval time calculations (since they are very few)
orders_valid_approval = orders[~((orders['order_status'] == 'delivered') & (orders['order_approved_at'].isnull()))]

# (B) Handling order_delivered_customer_date:
# Extract delivered orders missing order_delivered_customer_date
delivered_missing_delivery = orders[(orders['order_status'] == 'delivered') & (orders['order_delivered_customer_date'].isnull())]
print("Number of orders delivered without order_delivered_customer_date:", delivered_missing_delivery.shape[0])

# Use estimated delivery date as a temporary replacement for these delivered orders (documenting this step)
mask = (orders['order_status'] == 'delivered') & (orders['order_delivered_customer_date'].isnull())
orders.loc[mask, 'order_delivered_customer_date'] = orders.loc[mask, 'order_estimated_delivery_date']

# Ensure missing values in order_delivered_customer_date for delivered orders are handled
missing_delivered_after = orders[(orders['order_status'] == 'delivered') & (orders['order_delivered_customer_date'].isnull())].shape[0]
print("After imputation, number of orders delivered without order_delivered_customer_date:", missing_delivered_after)

# -----------------------------------------------
# 8. Handle missing values in the order_reviews file
# -----------------------------------------------
# In order_reviews, there are many missing values in the review_comment_message column.
# Replace them with a default text "No Comment" for easier analysis.
order_reviews['review_comment_message'] = order_reviews['review_comment_message'].fillna("No Comment")

# -----------------------------------------------
# 9. Save the processed data
# -----------------------------------------------
# Save a copy of orders after excluding invalid rows (for approval time analysis, for example)
orders_clean = orders_valid_approval.copy()
orders_clean.to_csv("cleaned_orders_dataset.csv", index=False)

# Save a copy of order_reviews after handling missing values
order_reviews.to_csv("cleaned_order_reviews_dataset.csv", index=False)

# -----------------------------------------------
# 10. Display samples of the processed data for validation
# -----------------------------------------------
print("\n----- Cleaned Orders Sample -----")
print(orders_clean.head())

print("\n----- Cleaned Order Reviews Sample -----")
print(order_reviews.head())
