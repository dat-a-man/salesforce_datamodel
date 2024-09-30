import dlt
from dlt_plus.dbt_generator.utils import table_reference_adapter


# Example countries table
@dlt.resource(name="countries", primary_key="id", write_disposition="merge")
def countries():
    yield from [
        {"id": 1, "name": "USA"},
        {"id": 2, "name": "Germany"},
    ]


# Example companies table
@dlt.resource(name="companies", primary_key="id", write_disposition="merge")
def companies():
    yield from [
        {"id": 1, "name": "GiggleTech", "country_id": 2},
        {"id": 2, "name": "HappyHacks", "country_id": 1},
    ]


# Example customers table which references company
@dlt.resource(name="customers", primary_key="id", write_disposition="merge")
def customers():
    yield from [
        {"id": 1, "name": "andrea", "company_id": 1},
        {"id": 2, "name": "violetta", "company_id": 2},
        {"id": 3, "name": "marcin", "company_id": 1},
    ]


# Example orders table which references customer
@dlt.resource(name="orders", primary_key="id", write_disposition="merge")
def orders():
    yield from [
        {"id": 1, "date": "1-2-2020", "customer_id": 1},
        {"id": 2, "date": "14-2-2020", "customer_id": 2},
        {"id": 3, "date": "18-2-2020", "customer_id": 1},
        {"id": 4, "date": "1-3-2020", "customer_id": 3},
        {"id": 5, "date": "2-3-2020", "customer_id": 3},
    ]

# run your pipeline
p = dlt.pipeline(pipeline_name="example_shop1", destination="bigquery", dataset_name="test_example_shop")
p.run([customers(), companies(), orders(), countries()])

# Define relationships in your schema
table_reference_adapter(
    p,
    "companies",
    references=[
        {
            "referenced_table": "countries",
            "columns": ["country_id"],
            "referenced_columns": ["id"],
        }
    ],
)

table_reference_adapter(
    p,
    "customers",
    references=[
        {
            "referenced_table": "companies",
            "columns": ["company_id"],
            "referenced_columns": ["id"],
        }
    ],
)

table_reference_adapter(
    p,
    "orders",
    references=[
        {
            "referenced_table": "customers",
            "columns": ["customer_id"],
            "referenced_columns": ["id"],
        }
    ],
)
