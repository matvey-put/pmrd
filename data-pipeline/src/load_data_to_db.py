import pandas as pd
from sqlalchemy import create_engine
from config import DB_CONFIG

def load_data_to_db(df: pd.DataFrame, table_name: str, schema: str = 's_sql_dds'):
    """
    Загружает DataFrame в PostgreSQL в режиме 'append'.
    """
    try:
        conn_str = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        engine = create_engine(conn_str)

       
        print(f"Начинаю загрузку {len(df)} строк в таблицу {schema}.{table_name}...")
        df.to_sql(
            name=table_name,
            con=engine,
            schema=schema,
            if_exists='append', 
            index=False,
            method='multi'      
        )
        print("Загрузка успешно завершена.")
        
    except Exception as e:
        print(f"Ошибка при загрузке в БД: {e}")