import pandas as pd
import numpy as np

df = pd.read_csv("bhatbhateni_sales.csv")
print("Dataset loaded successfully.")

# Displaying the first five rows
print("\nFirst five rows:")
print(df.head())

# Displaying the number of rows and columns
print("\nDataset shape:", df.shape)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

# Display the data type of each column
print("\nData types:")
print(df.dtypes)

# Display general dataset information
print("\nDataset information:")
df.info()

# Display numeric summary statistics
print("\nNumeric summary:")
print(df.describe())

# Display summary for all columns
print("\nFull summary:")
print(df.describe(include="all"))

# Count missing values
missing_count = df.isnull().sum()

# Calculate missing-value percentages
missing_percentage = (missing_count / len(df)) * 100

# Create a missing-value summary table
missing_summary = pd.DataFrame({
    "Missing Count": missing_count,
    "Missing Percentage": missing_percentage
})

# Show only columns that contain missing values
missing_summary = missing_summary[
    missing_summary["Missing Count"] > 0
]

print("\nMissing-value summary:")
print(missing_summary)


# Count fully duplicated rows
duplicate_count = df.duplicated().sum()

print("\nNumber of exact duplicate rows:", duplicate_count)


# Display repeated TransactionIDs
# A repeated TransactionID may represent multiple products in one order
repeated_transactions = df[
    df.duplicated(subset=["TransactionID"], keep=False)
].sort_values("TransactionID")

print("\nExamples of repeated TransactionIDs:")
print(repeated_transactions.head(20))


# Check how many products appear in each transaction
transaction_check = (
    df.groupby("TransactionID")
    .agg(
        NumberOfRows=("TransactionID", "size"),
        UniqueProducts=("ProductName", "nunique"),
        TotalQuantity=("Quantity", "sum")
    )
    .sort_values("NumberOfRows", ascending=False)
)

print("\nTransaction line-item check:")
print(transaction_check.head(10))


# Check whether TotalAmount equals Quantity multiplied by UnitPrice
valid_price_rows = df["UnitPrice"].notna()

expected_total = df["Quantity"] * df["UnitPrice"]

incorrect_totals = df[
    valid_price_rows
    & ~np.isclose(
        df["TotalAmount"],
        expected_total,
        atol=0.01
    )
]

print("\nNumber of incorrect TotalAmount values:", len(incorrect_totals))

print("\nExamples of incorrect totals:")
print(incorrect_totals.head())

rows_before = len(df)
duplicates_before = df.duplicated().sum()

# Remove fully identical rows
df = df.drop_duplicates().copy()

rows_after = len(df)
duplicates_after = df.duplicated().sum()

print("\nRows before removing duplicates:", rows_before)
print("Duplicates found:", duplicates_before)
print("Rows after removing duplicates:", rows_after)
print("Duplicates remaining:", duplicates_after)
print("Rows removed:", rows_before - rows_after)

# Save missing-value counts before cleaning
nulls_before = df.isnull().sum()

# Create a CustomerID-to-CustomerName mapping
customer_name_map = (
    df.dropna(subset=["CustomerName"])
    .drop_duplicates(subset=["CustomerID"])
    .set_index("CustomerID")["CustomerName"]
)

# Fill names using CustomerID
df["CustomerName"] = df["CustomerName"].fillna(
    df["CustomerID"].map(customer_name_map)
)

# Fill any names that are still missing
df["CustomerName"] = df["CustomerName"].fillna(
    "Unknown Customer"
)

# Find the most common category for each product
product_category_map = (
    df.dropna(subset=["ProductCategory"])
    .groupby("ProductName")["ProductCategory"]
    .agg(lambda values: values.mode().iloc[0])
)

# Fill categories using ProductName
df["ProductCategory"] = df["ProductCategory"].fillna(
    df["ProductName"].map(product_category_map)
)

# Fill any categories that are still missing
df["ProductCategory"] = df["ProductCategory"].fillna(
    "Unknown Category"
)

missing_price_rows = (
    df["UnitPrice"].isna()
    & df["TotalAmount"].notna()
    & (df["Quantity"] > 0)
)

df.loc[missing_price_rows, "UnitPrice"] = (
    df.loc[missing_price_rows, "TotalAmount"]
    / df.loc[missing_price_rows, "Quantity"]
)

# Use the median price of the same product if needed
product_median_price = df.groupby(
    "ProductName"
)["UnitPrice"].transform("median")

df["UnitPrice"] = df["UnitPrice"].fillna(
    product_median_price
)

# Use the median price of the same category if needed
category_median_price = df.groupby(
    "ProductCategory"
)["UnitPrice"].transform("median")

df["UnitPrice"] = df["UnitPrice"].fillna(
    category_median_price
)

# Use the overall median price as the final option
df["UnitPrice"] = df["UnitPrice"].fillna(
    df["UnitPrice"].median()
)

# Use Unknown because guessing a payment method may be inaccurate
df["PaymentMethod"] = df["PaymentMethod"].fillna(
    "Unknown"
)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print(
    "\nTotal missing values remaining:",
    df.isnull().sum().sum()
)

# Convert Date into datetime format
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

# Check for invalid dates
print("\nInvalid dates:", df["Date"].isnull().sum())

# Remove rows with invalid dates
df = df.dropna(subset=["Date"]).copy()


# Create date-related columns
df["Year"] = df["Date"].dt.year
df["MonthNumber"] = df["Date"].dt.month
df["Month"] = df["Date"].dt.month_name()
df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)
df["DayOfWeek"] = df["Date"].dt.day_name()
df["DayNumber"] = df["Date"].dt.dayofweek
df["Quarter"] = df["Date"].dt.quarter


# Mark Saturdays and Sundays as weekends
df["WeekendStatus"] = np.where(
    df["DayNumber"] >= 5,
    "Weekend",
    "Weekday"
)


# Extract the city from Branch
# Example: "Pokhara - Lakeside" becomes "Pokhara"
df["City"] = (
    df["Branch"]
    .str.split("-")
    .str[0]
    .str.strip()
)


# Recalculate TotalAmount
df["CalculatedTotal"] = (
    df["Quantity"] * df["UnitPrice"]
).round(2)


# Check totals before replacing them
incorrect_total_count = (
    ~np.isclose(
        df["TotalAmount"],
        df["CalculatedTotal"],
        atol=0.01
    )
).sum()

print(
    "\nIncorrect totals before correction:",
    incorrect_total_count
)


# Replace TotalAmount with the calculated amount
df["TotalAmount"] = df["CalculatedTotal"]

# Remove the temporary column
df.drop(columns=["CalculatedTotal"], inplace=True)


# Confirm that all totals are now correct
all_totals_correct = np.isclose(
    df["TotalAmount"],
    df["Quantity"] * df["UnitPrice"],
    atol=0.01
).all()

print("All totals are correct:", all_totals_correct)


# Create a cleaning summary
cleaning_summary = pd.DataFrame({
    "Missing Before": nulls_before,
    "Missing After": df[
        nulls_before.index
    ].isnull().sum()
})

print("\nCleaning summary:")
print(cleaning_summary)