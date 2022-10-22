import os

from sqlalchemy import create_engine


def engine_default(pool_size=None, max_overflow=None):
    try:
        user = os.getenv("POSTGRES_USER", "postgres")
        password = os.getenv("POSTGRES_PASSWORD", "postgres")
        host = os.getenv("POSTGRES_HOST", "postgres")
        port = os.getenv("POSTGRES_PORT", 5432)
        database = os.getenv("POSTGRES_DB", "flask")

        # configure this and others args as needed
        if not pool_size:
            pool_size = os.getenv("POSTGRES_POOL_SIZE", 5)
        if not max_overflow:
            max_overflow = os.getenv("POSTGRES_MAX_OVERFLOW", 10)

        url = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(url, pool_size=pool_size, max_overflow=max_overflow)

        return engine
    except Exception as e:
        raise Exception(f"Error creating engine - Default: {e}")
