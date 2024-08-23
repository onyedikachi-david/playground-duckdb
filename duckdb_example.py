import duckdb
import pandas as pd

# Connect to an in-memory database
conn = duckdb.connect()

# Create a sample pandas DataFrame
bird_data = pd.DataFrame({
    "species": ["Mallard", "Wood Duck", "Gadwall", "Pintail"],
    "count": [42, 17, 9, 31]
})

# Register the DataFrame as a view in DuckDB
conn.register("bird_sightings", bird_data)

# Query the DataFrame using SQL
result = conn.execute("SELECT species FROM bird_sightings WHERE count > 20").fetchdf()
print("Birds with more than 20 sightings:")
print(result)

# Create a table and insert data
conn.execute("CREATE TABLE migration_data (species STRING, distance_km INTEGER)")
conn.execute("INSERT INTO migration_data VALUES ('Mallard', 1500), ('Wood Duck', 800), ('Gadwall', 2000), ('Pintail', 2500)")

# Join tables and query
result = conn.execute("""
    SELECT b.species, b.count, m.distance_km
    FROM bird_sightings b
    JOIN migration_data m ON b.species = m.species
    WHERE m.distance_km > 1000
    ORDER BY m.distance_km DESC
""").fetchdf()
print("\nBirds that migrate more than 1000 km:")
print(result)