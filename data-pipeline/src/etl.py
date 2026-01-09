from src.get_dataset import generate_synthetic_data
from src.load_data_to_db import load_data_to_db
from src.fill_structured_table import fill_structured_table
from config import DEFAULT_PERIOD

def etl():
    print(">>> Запуск процесса ETL...")
    
    df = generate_synthetic_data(num_rows=1000)
    
    load_data_to_db(df, 't_sql_source_unstructured')
    
    fill_structured_table(
        start_date=DEFAULT_PERIOD["start_date"], 
        end_date=DEFAULT_PERIOD["end_date"]
    )
    
    print(">>> ETL процесс успешно завершен.")
