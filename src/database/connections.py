import psycopg


def _connect_pg(
    user: str,
    password: str,
    host: str,
    port: int,
    database: str
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
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
    except Exception as e:
        raise Exception(f"Error connecting to PostgreSQL: {e}")
