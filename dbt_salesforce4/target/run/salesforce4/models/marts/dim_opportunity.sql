
  
    

    create or replace table `dlthub-analytics`.`salesforce_data_tst5_transformed`.`dim_opportunity`
      
    
    

    OPTIONS()
    as (
      /* Table: opportunity */

SELECT
    t.id,
    t.is_deleted,
    t.account_id,
    t.is_private,
    t.name,
    t.stage_name,
    t.amount,
    t.probability,
    t.expected_revenue,
    t.close_date,
    t.type,
    t.lead_source,
    t.is_closed,
    t.is_won,
    t.forecast_category,
    t.forecast_category_name,
    t.has_opportunity_line_item,
    t.owner_id,
    t.created_date,
    t.created_by_id,
    t.last_modified_date,
    t.last_modified_by_id,
    t.system_modstamp,
    t.push_count,
    t.fiscal_quarter,
    t.fiscal_year,
    t.has_open_activity,
    t.has_overdue_task,
    t.main_competitors_c,
    t._dlt_load_id,
    t._dlt_id,
    t.delivery_installation_status_c,
    t.current_generators_c,
    t.order_number_c,
    t.tracking_number_c,
    t.next_step,
    t.last_viewed_date,
    t.last_referenced_date,
    t.total_opportunity_quantity,
    t.pricebook2_id,
    t.last_amount_changed_history_id,
    t.campaign_id,
FROM  `dlthub-analytics`.`salesforce_data_tst5_transformed`.`stg_opportunity` as t
    );
  