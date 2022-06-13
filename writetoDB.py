
def writetoDB(engine, tablename, df, operation, schema_nm):
    df.to_sql(
        tablename,
        engine,
        schema = schema_nm,
        if_exists=operation,
        index=False,
    chunksize = 500,
    method = 'multi'
    )
