#!/usr/bin/env python3
"""Pipeline to load Salesforce data."""
import dlt
from salesforce import salesforce_source
from dlt_plus.dbt_generator.utils import table_reference_adapter


def load() -> None:
    """Execute a pipeline from Salesforce."""

    p = dlt.pipeline(
        pipeline_name="salesforce_tst", destination='bigquery', dataset_name="salesforce_data_tst9", progress="log",
        dev_mode = True
    )
    # Execute the pipeline
    source = salesforce_source()
  

    # Run the pipeline
    load_info = p.run(source)

    # Print the load info
    print(load_info)

    # Account references itself via parent_id and references sf_user via owner_id
    table_reference_adapter(
        p,
        "account",
        references=[
            {
                "referenced_table": "sf_user",
                "columns": ["owner_id"],
                "referenced_columns": ["id"],
            },
        ],
    )

    # Contact references Account and SF_User
    table_reference_adapter(
        p,
        "contact",
        references=[
            {
                "referenced_table": "account",
                "columns": ["account_id"],
                "referenced_columns": ["id"],
            },
            {
                "referenced_table": "sf_user",
                "columns": ["owner_id"],
                "referenced_columns": ["id"],
            },
        ],
    )

    # Opportunity references Account, Campaign, and SF_User
    table_reference_adapter(
        p,
        "opportunity",
        references=[
            {
                "referenced_table": "account",
                "columns": ["account_id"],
                "referenced_columns": ["id"],
            },
            {
                "referenced_table": "campaign",
                "columns": ["campaign_id"],
                "referenced_columns": ["id"],
            },
            {
                "referenced_table": "sf_user",
                "columns": ["owner_id"],
                "referenced_columns": ["id"],
            },
        ],
    )

    # Opportunity Contact Role references Opportunity and Contact
    table_reference_adapter(
        p,
        "opportunity_contact_role",
        references=[
            {
                "referenced_table": "opportunity",
                "columns": ["opportunity_id"],
                "referenced_columns": ["id"],
            },
            {
                "referenced_table": "contact",
                "columns": ["contact_id"],
                "referenced_columns": ["id"],
            },
        ],
    )

    # Opportunity Line Item references Opportunity, Pricebook Entry, and Product2
    table_reference_adapter(
        p,
        "opportunity_line_item",
        references=[
            {
                "referenced_table": "opportunity",
                "columns": ["opportunity_id"],
                "referenced_columns": ["id"],
            },
            {
                "referenced_table": "pricebook_entry",
                "columns": ["pricebook_entry_id"],
                "referenced_columns": ["id"],
            },
            {
                "referenced_table": "product_2",
                "columns": ["product2_id"],
                "referenced_columns": ["id"],
            },
        ],
    )

    # Pricebook Entry references Pricebook2 and Product2
    table_reference_adapter(
        p,
        "pricebook_entry",
        references=[
            {
                "referenced_table": "pricebook_2",
                "columns": ["pricebook2_id"],
                "referenced_columns": ["id"],
            },
            {
                "referenced_table": "product_2",
                "columns": ["product2_id"],
                "referenced_columns": ["id"],
            },
        ],
    )

    # Campaign Member references Campaign, Contact, and Lead
    table_reference_adapter(
        p,
        "campaign_member",
        references=[
            {
                "referenced_table": "campaign",
                "columns": ["campaign_id"],
                "referenced_columns": ["id"],
            },
            {
                "referenced_table": "contact",
                "columns": ["contact_id"],
                "referenced_columns": ["id"],
            },
            {
                "referenced_table": "lead",
                "columns": ["lead_id"],
                "referenced_columns": ["id"],
            },
        ],
    )

    # Task references SF_User
    table_reference_adapter(
        p,
        "task",
        references=[
            {
                "referenced_table": "sf_user",
                "columns": ["owner_id"],
                "referenced_columns": ["id"],
            },
        ],
    )

    # Event references SF_User
    table_reference_adapter(
        p,
        "event",
        references=[
            {
                "referenced_table": "sf_user",
                "columns": ["owner_id"],
                "referenced_columns": ["id"],
            },
        ],
    )

    # User Role references itself via parent_role_id
    table_reference_adapter(
        p,
        "user_role",
        references=[
            {
                "referenced_table": "user_role",
                "columns": ["parent_role_id"],
                "referenced_columns": ["id"],
            },
        ],
    )





if __name__ == "__main__":
    load()
