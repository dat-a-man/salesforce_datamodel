
  
    

    create or replace table `dlthub-analytics`.`salesforce_data_tst5_transformed`.`dim_task`
      
    
    

    OPTIONS()
    as (
      /* Table: task */

SELECT
    t.id,
    t.who_id,
    t.what_id,
    t.subject,
    t.activity_date,
    t.status,
    t.priority,
    t.is_high_priority,
    t.owner_id,
    t.description,
    t.is_deleted,
    t.account_id,
    t.is_closed,
    t.created_date,
    t.created_by_id,
    t.last_modified_date,
    t.last_modified_by_id,
    t.system_modstamp,
    t.is_archived,
    t.is_reminder_set,
    t.is_recurrence,
    t.task_subtype,
    t._dlt_load_id,
    t._dlt_id,
    t.completed_date_time,
FROM  `dlthub-analytics`.`salesforce_data_tst5_transformed`.`stg_task` as t
    );
  