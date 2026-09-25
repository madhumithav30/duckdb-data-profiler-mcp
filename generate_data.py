import duckdb

print("Generating sample_orders.parquet...")
duckdb.sql("""
    COPY (
        SELECT 
            range as order_id,
            (range % 10) + 1 as customer_id,
            round(random() * 200, 2) as amount,
            CASE WHEN range % 5 = 0 THEN 'PENDING' ELSE 'COMPLETED' END as status
        FROM range(1000)
    ) TO 'sample_orders.parquet' (FORMAT PARQUET);
""")
print("✅ Done! Created sample_orders.parquet with 1,000 rows.")
