import os

import psycopg


def _connect_pg(
    user: str, password: str, host: str, port: int, database: str
) -> psycopg.Connection:
    """Connect to a PostgreSQL database.

    Args:
        user (str): Postgres username.
        password (str): Postgres password.
        host (str): Hostname or IP address.
        port (int): Database port.
        database (str): Database name.

    Returns:
        psycopg.Connection: A connection to the database.
    """
    try:
        return psycopg.connect(
            user=user, password=password, host=host, port=port, database=database
        )
    except Exception as e:
        raise Exception(f"Error connecting to PostgreSQL: {e}")


def conn_default() -> psycopg.Connection:
    """Connect to the default database, uses .env variables.

    default:
        user: os.getenv("POSTGRES_USER", "postgres")
        password: os.getenv("POSTGRES_PASSWORD", "postgres")
        host: os.getenv("POSTGRES_HOST", "postgres")
        port: os.getenv("POSTGRES_PORT", 5432)
        database: os.getenv("POSTGRES_DB", "flask")

    Returns:
        psycopg.Connection: A connection to the database.
    """
    try:
        user = os.getenv("POSTGRES_USER", "postgres")
        password = os.getenv("POSTGRES_PASSWORD", "postgres")
        host = os.getenv("POSTGRES_HOST", "postgres")
        port = os.getenv("POSTGRES_PORT", 5432)
        database = os.getenv("POSTGRES_DB", "flask")

        conn = _connect_pg(
            user=user, password=password, host=host, port=int(port), database=database
        )
        return conn
    except Exception as e:
        raise Exception(f"Error connecting to PG - Default: {e}")
