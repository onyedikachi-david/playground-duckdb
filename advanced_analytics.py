import duckdb
import pandas as pd

# Connect to an in-memory database
conn = duckdb.connect()

# Create a sample pandas DataFrame
data = {
    "category": ["A", "B", "C", "A", "B", "C", "A", "B", "C"],
    "value": [10, 20, 30, 40, 50, 60, 70, 80, 90]
}
df = pd.DataFrame(data)

# Register the DataFrame as a view in DuckDB
conn.register("data", df)

# Group by category and calculate the sum of values
result = conn.execute("SELECT category, SUM(value) AS sum_value FROM data GROUP BY category").fetchdf()
print("Sum of values by category:")
print(result)

# Calculate the average value for each category
result = conn.execute("SELECT category, AVG(value) AS avg_value FROM data GROUP BY category").fetchdf()
print("\nAverage value by category:")
print(result)

# Join two tables based on a common column
conn.execute("CREATE TABLE categories (category STRING, description STRING)")
conn.execute("INSERT INTO categories VALUES ('A', 'Category A'), ('B', 'Category B'), ('C', 'Category C')")

result = conn.execute("""
    SELECT d.category, d.value, c.description
    FROM data d
    JOIN categories c ON d.category = c.category
""").fetchdf()
print("\nJoined data with categories:")
print(result)