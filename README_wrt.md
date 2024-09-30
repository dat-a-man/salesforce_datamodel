# Salesforce dlt-dbt-generator package
This package uses a dlt-dbt-generator to model data that is loaded from your dlt pipeline.

## In a nutshell

- It automatically inspects the pipeline schema and generates a baseline dbt project, complete with staging and mart layers. The generator is able to create staging, dimensional, and fact models.

- Additionally, the dlt-dbt-generator lets you define relationships between the schema tables, which can be used to create fact tables automatically.

The resulting project can be executed using the credentials already provided to the pipeline and is capable of processing incoming data incrementally.

## How it works?
1. Setup and run your dlt-salesforce pipeline.
2. Install and execute the dlt-dbt-generator to automatically create the initial set of mart and staging tables.
3. Before running the generator, make sure the primary keys are defined. These keys are essential for accurately linking data across tables.
4. Execute the generator and examine the baseline dbt project created.
5. To add customized fact tables, define how different tables relate to each other based on your specific data needs. This involves setting up custom relationships that reflect your data model.
6. After defining all necessary relationships, re-run the pipeline to apply the changes. This step processes the data with the updated configurations.
7. Use the dlt-dbt-generator again to create dimension and fact tables. This finalizes the structure of your data model, allowing for comprehensive analysis and insights.

## Install `dlt-dbt-generator`
Install the latest version on `dlt-dbt-generator` using the following command:

```sh
pip install https://dlt-packages.fra1.digitaloceanspaces.com/dlt-plus/dlt_plus-0.2.0-py3-none-any.whl
```

To install the latest nightly build with Poetry, first uninstall any existing version you have installed, then run:

```sh
poetry add https://dlt-packages.fra1.digitaloceanspaces.com/dlt-plus/dlt_plus-0.2.0-py3-none-any.whl
```
### Licensing
To use the dlt+ tools, you need to obtain a valid license from dltHub. Once you have received your license, you can make it available to dlt+ by adding it to your environment:

```sh
export RUNTIME__LICENSE="eyJhbGciOiJSUz...vKSjbEc==="
```
Or by adding it to your global or local `secrets.toml` file:

```toml
[runtime]
license="eyJhbGciOiJSUz...vKSjbEc==="
```

You can verify that the license was installed correctly and is valid by running:

```sh
$ dlt-license
```

The full guide to read for generating fact and dimension tables using `dlt-dbt-generator`: [here](https://dlt-plus.netlify.app/docs/plus/dlt_dbt_generator/).


## Database support
We support 
- Redshift, 
- BigQuery,
- Snowflake, 
- Athena, 
- Postgres.

## How to use this package

We recommend that you add this package as a dependency to your own `dbt` package.


### How to run the `dlt` pipeline

To deploy dlt Salesforce pipeline, please read the full documentation [here](https://dlthub.com/docs/dlt-ecosystem/verified-sources/salesforce). 

### Install `dlt`
Install dlt with destination dependencies, e.g. [BigQuery](https://dlthub.com/docs/dlt-ecosystem/destinations/bigquery):

```shell
pip install dlt[bigquery]
```
or
```shell
pip install -r requirements.txt
```

> If you use [Redshift](https://dlthub.com/docs/dlt-ecosystem/destinations/redshift) as a destination, then run `pip install dlt[redshift]`. 
> 
> If you use [Snowflake](https://dlthub.com/docs/dlt-ecosystem/destinations/snowflake) as a destination, then run `pip install dlt[snowflake]`. 
> 
> If you use [Athena](https://dlthub.com/docs/dlt-ecosystem/destinations/athena) as a destination, then run `pip install dlt[athena]`. 
> 
> If you use [Postgres](https://dlthub.com/docs/dlt-ecosystem/destinations/postgres) as a destination, then run `pip install dlt[postgres]`. 

More about installing dlt: [Installation](https://dlthub.com/docs/reference/installation).

### Configuration

## Add credentials

In `.dlt` folder add your credentials to `secrets.toml`.  
It's where you store sensitive information securely, like access tokens, private keys, etc. 
Keep this file safe, do not commit it.

**Credentials for source data**

Add the Salesforce credentials:

    ```toml
    # put your secret values and credentials here. do not share this file and do not push it to github
    [sources.salesforce]
    user_name = "please set me up!" # Salesforce user name
    password = "please set me up!" # Salesforce password
    security_token = "please set me up!" # Salesforce security token generated
    ```
    
Enter credentials for your chosen destination as per the [docs.](https://dlthub.com/docs/dlt-ecosystem/destinations/)

### Define primary keys
To generate fact tables, you will first need to add additional relationship hints to your pipeline. This requires ensuring that each table has a primary key defined, as relationships are based on these keys:

```py
import dlt 

@dlt.resource(name="deals", primary_key="id")
def deals():
    ...
```
or 

```py
source = hubspot()
source.deals.apply_hints(primary_key="id")
```