#!/usr/bin/env python3
"""Pipeline to load Salesforce data."""
import dlt
from salesforce import salesforce_source


def load() -> None:
    """Execute a pipeline from Salesforce."""

    pipeline = dlt.pipeline(
        pipeline_name="salesforce1", destination='bigquery', dataset_name="salesforce_data_tst2", progress="log"
    )
    # Execute the pipeline
    load_info = pipeline.run(salesforce_source())

    # Print the load info
    print(load_info)


if __name__ == "__main__":
    load()
