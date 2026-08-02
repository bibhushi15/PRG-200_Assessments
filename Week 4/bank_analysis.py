import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("nepal_bank_transactions PRG 200.csv")
print("Dataset loaded successfully.")
#column name
print(df.columns)
print(100 * "--")

#head and tail
print(df.head())
print(df.tail())

#generalized stastistical analysis 
print(df.info)

print(80* "--")
print(df.describe(include='all'))

print(80* "--")
print(df.shape)
print(80* "--")
age= df['customer_age']
print(age)
print(80* "--")
print(df.shape)

print(df.dtypes)

channel=df['channel'].head
print(channel)

#.Loc and .iloc
print(df.loc[0,"branch_name"])
print(df.iloc[0,3])
df.loc[0:2,["branch_name","channel","transaction_status"]]

# filtering ATM cash withdrawals
atm_withdrawal = df[(df["channel"] == "ATM") & (df["transaction_type"] == "Cash Withdrawal")]
print(f"ATM withdrawals:\n{atm_withdrawal}")

# filtering failed transactions
not_successful = df[df["transaction_status"] != "Success"]
print(f"Not Successful: {len(not_successful)} out of {len(df)} ({len(not_successful)/len(df):.1%})")
not_successful["transaction_status"].value_counts()

#high value fund
large_transfers=df[(df["transaction_type"]== "Fund Transfer") & (df["amount_npr"] >50000)]
print(f"Large fund transfers (>NRP 50,000): {len(large_transfers)}")

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"]=(9,5)
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["year_month"]=df["date"].dt.to_period("M").astype(str)
print(df.head(2))

channel_counts = df["channel"].value_counts()

plt.figure()
sns.barplot(x=channel_counts.index, y=channel_counts.values, hue=channel_counts.index, palette="viridis", legend=False)
plt.title("Transaction Count by Channel")
plt.xlabel("Channel")
plt.ylabel("Number of Transaction")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

#Linechart
monthly = df.groupby("year_month").size()
plt.figure()
plt.plot(monthly.index, monthly.values, marker="o",color="#2E7D32")
plt.title("monthly Transaction Volume, 2024")
plt.xlabel("Month")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.axvspan("2024-10", "2024-11" , color="orange", alpha=0.5, label="Dashain/TIhar seasion")
plt.legend()
plt.tight_layout()
plt.show()

#Creaating a histogram (for continuous data)
withdrawals = df[df["transaction_type"] == "Cash Withdrawal"]

plt.figure()
plt.hist(withdrawals["amount_npr"], bins=20, color="#1565CB", edgecolor="white")
plt.title("Distribution of ATM/Counter Cash Withdrawal Amounts")
plt.xlabel("Amount (NPR)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.figure()
sns.boxplot(
    data=df,
    x="channel",
    y="processing_time_ms",
    hue="channel",
    palette="Set2",
    legend=False
)

plt.title("Processing Time by Channel")
plt.xlabel("Channel")
plt.ylabel("Processing Time (ms)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

#Creating a heatmap - channel vs transaction status
pivot = pd.crosstab(df["channel"], df["transaction_status"])

plt.figure()
sns.heatmap(
    pivot,
    annot=True,
    fmt="d",
    cmap="YlGnBu"
)
plt.title("Transaction Status by Channel")
plt.ylabel("Channel")
plt.xlabel("Status")
plt.tight_layout()
plt.show()

#pie chart
account_count=df["account_type"].value_counts()

plt.figure()
plt.pie(
    account_count.values,
    labels=account_count.index,
    autopct="%1.1f%%",
    colors=sns.color_palette("pastel"),
)
plt.title("Transaction Share by Account Type")
plt.tight_layout()
plt.show()