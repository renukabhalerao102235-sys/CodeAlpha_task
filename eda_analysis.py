import pandas as pd
import matplotlib.pyplot as plt

# Load the books dataset
df = pd.read_csv("books_data.csv")

# 1. Display the first five rows
print("FIRST FIVE BOOKS")
print(df.head())

# 2. Dataset size
print("\nDATASET SHAPE")
print("Rows and columns:", df.shape)

# 3. Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# 4. Check duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# 5. Analyze book prices
df["Price"] = (
    df["Price"].astype(str)
    .str.replace("£", "", regex=False)
    .str.replace("$", "", regex=False)
)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print("\nPRICE STATISTICS")
print(df["Price"].describe())

# 6. Create a price chart
df["Price"].dropna().plot(kind="bar", figsize=(10, 5))
plt.title("Book Price Analysis")
plt.xlabel("Book Index")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("book_prices.png")

print("\nChart saved as book_prices.png")
plt.show()