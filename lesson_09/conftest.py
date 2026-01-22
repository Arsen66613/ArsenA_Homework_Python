import pytest
from sqlalchemy import create_engine


@pytest.fixture(scope="session")
def engine():
    connection_string = (
        "postgresql+psycopg2://qa:66613@5.101.50.27:5432/x_clients"
    )
    engine = create_engine(connection_string)
    yield engine
    engine.dispose()
