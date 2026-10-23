from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "sample_beauty_wellness_transactions.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

def main():
    df = pd.read_csv(DATA, parse_dates=["transaction_date"])
    print("Dataset shape:", df.shape)
    print("\nData types:\n", df.dtypes)
    print("\nMissing values:\n", df.isna().sum())
    print("\nDuplicate transaction IDs:", df["transaction_id"].duplicated().sum())

    # Basic validation
    df = df.drop_duplicates(subset=["transaction_id"]).copy()
    df = df.dropna(subset=["customer_id", "transaction_date", "product_category", "order_value"])
    df = df[df["order_value"] >= 0]
    df["month"] = df["transaction_date"].dt.to_period("M").astype(str)

    category_summary = (
        df.groupby("product_category", as_index=False)
          .agg(transaction_count=("transaction_id", "count"),
               total_order_value=("order_value", "sum"),
               average_order_value=("order_value", "mean"))
          .sort_values("transaction_count", ascending=False)
    )
    category_summary.to_csv(OUT / "category_summary.csv", index=False)
    print("\nCategory summary:\n", category_summary.to_string(index=False))

    customer_summary = (
        df.groupby("customer_id", as_index=False)
          .agg(order_count=("transaction_id", "count"),
               total_spend=("order_value", "sum"),
               average_order_value=("order_value", "mean"),
               last_purchase=("transaction_date", "max"))
    )
    customer_summary.to_csv(OUT / "customer_summary.csv", index=False)

    category_counts = df["product_category"].value_counts().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    category_counts.plot(kind="bar")
    plt.title("Synthetic Sample: Transactions by Product Category")
    plt.xlabel("Product category")
    plt.ylabel("Number of transactions")
    plt.tight_layout()
    plt.savefig(OUT / "category_purchase_counts.png", dpi=150)
    plt.close()

    monthly = df.groupby("month")["transaction_id"].count()
    plt.figure(figsize=(9, 5))
    monthly.plot(kind="line", marker="o")
    plt.title("Synthetic Sample: Transactions by Month")
    plt.xlabel("Month")
    plt.ylabel("Number of transactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUT / "monthly_order_counts.png", dpi=150)
    plt.close()

    print("\nOutputs saved in:", OUT)
    print("Reminder: this is synthetic sample data, not real market evidence.")

if __name__ == "__main__":
    main()
