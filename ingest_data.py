import dlt
from dlt.sources.sql_database import sql_database


pipeline = dlt.pipeline(
    pipeline_name='sakila_loader',
    destination='duckdb',
    dataset_name='sakila'
)


source = sql_database("sqlite:///sakila.db")


info = pipeline.run(source, write_disposition="replace")

print("--- Data Ingestion Finish ---")
print(info)