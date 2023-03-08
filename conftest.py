from typing import Generator
import pytest
from sqlalchemy import Connection, create_engine
from testcontainers.postgres import PostgresContainer

from sql_queries import create_table, insert_repairing
from repairing import Repairing


@pytest.fixture()
def postgres_container1() -> Generator[PostgresContainer, None, None]:
    with PostgresContainer(image="postgres:latest") as container:
        container.get_container_host_ip = lambda: 'localhost'
        container.start()
        yield container


@pytest.fixture()
def postgres_container() -> PostgresContainer:
    container = PostgresContainer(image="postgres:latest")
    container.get_container_host_ip = lambda: 'localhost'
    container.start()
    return container


@pytest.fixture()
def postgres_url(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    return postgres_container.get_connection_url()


@pytest.fixture(scope="function")
def conn_with_data(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    repairing = [
        Repairing(
            description="test_description 1",
            city = 2,
            price=1,
            loss_estimate=3,
            amount=0,
        ),
        Repairing(
            description="test_description 2",
            city = 3,
            price=2,
            loss_estimate=5,
            amount=0,
        ),
        Repairing(
            description="test_description 3",
            city = 4,
            price=3,
            loss_estimate=8,
            amount=0,
        ),
    ]
    for repairing in repairing:
        insert_repairing(conn, repairing)
    return postgres_container.get_connection_url()