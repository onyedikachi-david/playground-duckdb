# DuckDB Playground

## Table of Contents
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Advanced Analytics](#advanced-analytics)
6. [Development Container](#development-container)
7. [Dependencies](#dependencies)
8. [License](#license)
9. [Contributing](#contributing)
10. [Troubleshooting](#troubleshooting)
11. [Future Enhancements](#future-enhancements)
12. [Acknowledgments](#acknowledgments)

## Introduction

This project is a DuckDB Playground, designed to provide a development environment for working with DuckDB, a high-performance analytical database system. It combines Python, DuckDB, and Pandas to perform data analysis and manipulation tasks.

## Project Structure

The project has the following structure:

```
.
├── .devcontainer/
│   └── devcontainer.json
├── venv/
├── Dockerfile
├── README.md
├── advanced_analytics.py
├── duckdb_example.py
├── requirements.txt
```

- `.devcontainer/`: Contains configuration for the Visual Studio Code development container.
- `venv/`: Python virtual environment (not tracked in version control).
- `Dockerfile`: Defines the Docker image for the development environment.
- `README.md`: This file, containing project documentation.
- `duckdb_example.py`: Python script demonstrating basic DuckDB operations.
- `advanced_analytics.py`: Python script for running DuckDB and Pandas operations.
- `requirements.txt`: Lists the Python package dependencies.

## Setup

1. Ensure you have Docker installed on your system.
2. Clone this repository to your local machine.
3. Open the project in Visual Studio Code with the Remote - Containers extension installed.
4. When prompted, click "Reopen in Container" to build and start the development container.

## Usage

The project includes two main scripts:

1. `duckdb_example.py`: Demonstrates basic DuckDB operations.
2. `advanced_analytics.py`: Showcases more advanced DuckDB and Pandas operations.

To run the basic DuckDB example:

1. Open a terminal in the development container.
2. Execute the following command:

```bash
python duckdb_example.py
```
This script demonstrates basic DuckDB operations, including:
- Creating a table
- Inserting data
- Querying data
- Closing the connection

To run the advanced DuckDB and Pandas operations:

1. Open a terminal in the development container.
2. Execute the following command:

```bash
python advanced_analytics.py
```

This script demonstrates basic DuckDB and Pandas operations, including:

- Creating a sample DataFrame
- Registering the DataFrame as a view in DuckDB
- Performing group-by operations
- Joining tables

## Advanced Analytics

The `advanced_analytics.py` script showcases several DuckDB and Pandas operations:

```python
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
```

Key features:
- Connects to an in-memory DuckDB database
- Creates a sample Pandas DataFrame
- Registers the DataFrame as a view in DuckDB
- Performs group-by operations to calculate sum and average values
- Demonstrates table creation and joining in DuckDB

## Development Container

The project uses a Visual Studio Code development container for a consistent development environment. The configuration is defined in the `devcontainer.json` file:

```json
{
  "name": "DuckDB Playground",
  "build": {
    "dockerfile": "../Dockerfile",
    "context": "..",
    "args": {
      "VARIANT": "3.10-bullseye",
      "NODE_VERSION": "lts/*"
    }
  },
  "features": {
    "ghcr.io/eitsupi/devcontainer-features/duckdb-cli:1": {}
  },
  "customizations": {
    "vscode": {
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "python.linting.enabled": true,
        "python.linting.pylintEnabled": true,
        "python.formatting.autopep8Path": "/usr/local/py-utils/bin/autopep8",
        "python.formatting.blackPath": "/usr/local/py-utils/bin/black",
        "python.formatting.yapfPath": "/usr/local/py-utils/bin/yapf",
        "python.linting.banditPath": "/usr/local/py-utils/bin/bandit",
        "python.linting.flake8Path": "/usr/local/py-utils/bin/flake8",
        "python.linting.mypyPath": "/usr/local/py-utils/bin/mypy",
        "python.linting.pycodestylePath": "/usr/local/py-utils/bin/pycodestyle",
        "python.linting.pydocstylePath": "/usr/local/py-utils/bin/pydocstyle",
        "python.linting.pylintPath": "/usr/local/py-utils/bin/pylint"
      }
    }
  }
}
```

Key features of the development container:
- Based on a Python 3.10 Debian Bullseye image
- Includes Node.js LTS version
- Installs the DuckDB CLI
- Configures Python-related VS Code settings
- Sets up linting and formatting tools

## Dependencies

The project's Python dependencies are listed in the `requirements.txt` file:

```
duckdb
pandas
matplotlib
```

These dependencies are:
- `duckdb`: The DuckDB database engine
- `pandas`: Data manipulation and analysis library
- `matplotlib`: Plotting library (not used in the current script, but available for future use)

## License

This project is licensed under the MIT License. The full license text can be found in the LICENSE file in the project root directory.

## Contributing

Contributions to this project are welcome. Please ensure that you follow the existing code style and add appropriate tests for any new features.

## Troubleshooting

If you encounter any issues while setting up or running the project, please check the following:

1. Ensure Docker is properly installed and running on your system.
2. Verify that you have the latest version of Visual Studio Code and the Remote - Containers extension.
3. Check that all required ports are available and not blocked by your firewall.

If problems persist, please open an issue on the project's GitHub repository with a detailed description of the problem and steps to reproduce it.

