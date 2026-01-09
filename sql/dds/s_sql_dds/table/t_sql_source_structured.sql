CREATE TABLE IF NOT EXISTS s_sql_dds.t_sql_source_structured (
    product_id          INT,
    product_name        TEXT,
    category            TEXT,
    price               NUMERIC,
    stock_quantity      INT,
    rating              NUMERIC,
    supplier_email      TEXT,
    status              TEXT,
    effective_from      DATE,
    effective_to        DATE,
    transformed_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);