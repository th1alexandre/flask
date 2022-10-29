import psycopg


def _connect_pg(
    user: str, password: str, host: str, port: int, database: str
) -> psycopg.Connection:
    try:
        return psycopg.connect(
            user=user, password=password, host=host, port=port, database=database
        )
    except Exception as e:
        raise Exception(f"Error connecting to PostgreSQL: {e}")
