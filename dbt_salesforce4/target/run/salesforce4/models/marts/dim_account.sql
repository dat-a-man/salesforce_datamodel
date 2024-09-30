
  
    

    create or replace table `dlthub-analytics`.`salesforce_data_tst5_transformed`.`dim_account`
      
    
    

    OPTIONS()
    as (
      /* Table: account */

SELECT
    t.id,
    t.is_deleted,
    t.name,
    t.type,
    t.billing_street,
    t.billing_city,
    t.billing_state,
    t.shipping_street,
    t.phone,
    t.fax,
    t.account_number,
    t.website,
    t.photo_url,
    t.sic,
    t.industry,
    t.annual_revenue,
    t.number_of_employees,
    t.ownership,
    t.ticker_symbol,
    t.description,
    t.rating,
    t.owner_id,
    t.created_date,
    t.created_by_id,
    t.last_modified_date,
    t.last_modified_by_id,
    t.system_modstamp,
    t.clean_status,
    t.customer_priority_c,
    t.sla_c,
    t.active_c,
    t.numberof_locations_c,
    t.upsell_opportunity_c,
    t.sla_serial_number_c,
    t.sla_expiration_date_c,
    t._dlt_load_id,
    t._dlt_id,
    t.billing_postal_code,
    t.billing_country,
    t.shipping_city,
    t.shipping_postal_code,
    t.shipping_country,
    t.shipping_state,
    t.site,
    t.last_activity_date,
    t.last_viewed_date,
    t.last_referenced_date,
    t.parent_id,
FROM  `dlthub-analytics`.`salesforce_data_tst5_transformed`.`stg_account` as t
    );
  