CREATE OR REPLACE FUNCTION s_sql_dds.fn_etl_data_load(start_date DATE, end_date DATE)
RETURNS VOID AS $$
BEGIN
    
    DELETE FROM s_sql_dds.t_sql_source_structured 
    WHERE effective_from >= start_date AND effective_from <= end_date;

    INSERT INTO s_sql_dds.t_sql_source_structured (
        product_id, product_name, category, price, 
        stock_quantity, rating, supplier_email, status, 
        effective_from, effective_to
    )
    SELECT 
        product_id,
        COALESCE(product_name, 'Unknown'), 
        UPPER(category), 
        ABS(price),     
        CASE WHEN stock_quantity < 0 THEN 0 ELSE stock_quantity END,
        CASE WHEN rating > 5 THEN 5 WHEN rating < 0 THEN 0 ELSE rating END, -
        LOWER(supplier_email),
        status,
        effective_from,
        effective_to
    FROM s_sql_dds.t_sql_source_unstructured
    WHERE effective_from >= start_date AND effective_from <= end_date
      AND product_id IS NOT NULL;
END;
$$ LANGUAGE plpgsql;