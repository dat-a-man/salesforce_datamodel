
  
    

    create or replace table `dlthub-analytics`.`salesforce_data_tst5_transformed`.`dim_event`
      
    
    

    OPTIONS()
    as (
      /* Table: event */

SELECT
    t.id,
    t.who_id,
    t.what_id,
    t.subject,
    t.location,
    t.is_all_day_event,
    t.activity_date_time,
    t.activity_date,
    t.duration_in_minutes,
    t.start_date_time,
    t.end_date_time,
    t.end_date,
    t.account_id,
    t.owner_id,
    t.is_private,
    t.show_as,
    t.is_deleted,
    t.is_child,
    t.is_group_event,
    t.created_date,
    t.created_by_id,
    t.last_modified_date,
    t.last_modified_by_id,
    t.system_modstamp,
    t.is_archived,
    t.is_recurrence,
    t.is_reminder_set,
    t.event_subtype,
    t.is_recurrence2_exclusion,
    t.is_recurrence2,
    t.is_recurrence2_exception,
    t._dlt_load_id,
    t._dlt_id,
    t.description,
FROM  `dlthub-analytics`.`salesforce_data_tst5_transformed`.`stg_event` as t
    );
  