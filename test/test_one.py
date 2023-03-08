from sqlalchemy import create_engine
from repairing import Repairing
from sql_queries import insert_repairing, create_table, get_repairing, update_repairing, complete_repairing


def test_service1(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    repairing = Repairing(
        description="test_description",
        city=5,
        price=100,
        loss_estimate=5,
        amount=0,
    )
    insert_repairing(conn, repairing)

    repairing = get_repairing(conn)
    assert len(repairing) == 4
    repairing = repairing[-1]
    assert repairing.description == "test_description"

    update_repairing(conn)
    repairing = get_repairing(conn)
    for repairing in repairing:
        assert repairing.price * repairing.loss_estimate == repairing.amount
        assert repairing.status == "paid"

    complete_repairing(conn)
    repairing = get_repairing(conn)
    for repairing in repairing:
        assert repairing.status == "done"