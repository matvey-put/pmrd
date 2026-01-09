import os
from datetime import datetime
from pathlib import Path
from sqlalchemy import create_engine, text
from config import DB_CONFIG, DEFAULT_PERIOD

BASE_DIR = Path(__file__).resolve().parent.parent

def _run_sql_file(conn, relative_path: str) -> None:
    """Считывает SQL-файл и выполняет его."""
    sql_path = BASE_DIR / relative_path
    if sql_path.exists():
        print(f"Выполняю скрипт: {relative_path}")
        conn.execute(text(sql_path.read_text(encoding="utf-8")))
    else:
        print(f"ВНИМАНИЕ: Файл не найден: {sql_path}")

def fill_structured_table(start_date: str = None, end_date: str = None):
    conn_url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    engine = create_engine(conn_url)

    s_date = start_date or DEFAULT_PERIOD["start_date"]
    e_date = end_date or DEFAULT_PERIOD["end_date"]

    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS s_sql_dds;"))
        
        _run_sql_file(conn, "sql/dds/s_sql_dds/table/t_sql_source_unstructured.sql")
        _run_sql_file(conn, "sql/dds/s_sql_dds/table/t_sql_source_structured.sql")

        _run_sql_file(conn, "sql/dds/s_sql_dds/function/fn_etl_data_load.sql")
        
        conn.execute(text("TRUNCATE TABLE s_sql_dds.t_sql_source_structured"))
        
        print(f"Запуск SQL трансформации за период {s_date} - {e_date}...")
        conn.execute(
            text("SELECT s_sql_dds.fn_etl_data_load(:start, :end)"),
            {"start": s_date, "end": e_date}
        )
        
        conn.commit()

    print("--- Данные успешно трансформированы и загружены ---")