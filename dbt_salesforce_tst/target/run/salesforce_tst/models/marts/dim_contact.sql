
  
    

    create or replace table `dlthub-analytics`.`salesforce_data_tst9_20240930010342_transformed`.`dim_contact`
      
    
    

    OPTIONS()
    as (
      /* Table: contact */

SELECT
    t.id,
    t.is_deleted,
    t.account_id,
    t.last_name,
    t.first_name,
    t.salutation,
    t.name,
    t.mailing_street,
    t.phone,
    t.fax,
    t.mobile_phone,
    t.email,
    t.title,
    t.department,
    t.lead_source,
    t.birthdate,
    t.owner_id,
    t.created_date,
    t.created_by_id,
    t.last_modified_date,
    t.last_modified_by_id,
    t.system_modstamp,
    t.is_email_bounced,
    t.photo_url,
    t.clean_status,
    t.is_priority_record,
    t.level_c,
    t.languages_c,
    t._dlt_load_id,
    t._dlt_id,
    t.mailing_city,
    t.mailing_state,
    t.mailing_postal_code,
    t.mailing_country,
    t.other_street,
    t.other_city,
    t.other_postal_code,
    t.other_country,
    t.assistant_phone,
    t.assistant_name,
    t.other_state,
    t.other_phone,
    t.description,
    t.last_activity_date,
    t.last_viewed_date,
    t.last_referenced_date,
    t.home_phone,
FROM  `dlthub-analytics`.`salesforce_data_tst9_20240930010342_transformed`.`stg_contact` as t
    );
  