import os

DB_CONFIG = {
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "password"),
    "host": os.getenv("DB_HOST", "db"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "etl_db")
}

DEFAULT_PERIOD = {
    "start_date": "2023-01-01",
    "end_date": "2025-12-31"
}