/* Table: task */


-- depends_on: `dlthub-analytics`.`salesforce_data_tst5_transformed`.`dlt_active_load_ids`

SELECT
/* select which columns will be available for table 'task' */
    id,
    who_id,
    what_id,
    subject,
    activity_date,
    status,
    priority,
    is_high_priority,
    owner_id,
    description,
    is_deleted,
    account_id,
    is_closed,
    created_date,
    created_by_id,
    last_modified_date,
    last_modified_by_id,
    system_modstamp,
    is_archived,
    is_reminder_set,
    is_recurrence,
    task_subtype,
    _dlt_load_id,
    _dlt_id,
    completed_date_time,
FROM `dlthub-analytics`.`salesforce_data_tst5`.`task`

/* we only load table items of the currently active load ids into the staging table */
WHERE _dlt_load_id IN ( SELECT load_id FROM  `dlthub-analytics`.`salesforce_data_tst5_transformed`.`dlt_active_load_ids` )