import duckdb
from google.colab import data_table
data_table.enable_dataframe_formatter()

conn = duckdb.connect(f"{pipeline_name}.duckdb")

conn.sql(f"SET search_path = '{dataset_name}'")

display(conn.sql("DESCRIBE"))

