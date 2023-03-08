from sqlalchemy.engine import Connection
from sqlalchemy import text

from repairing import Repairing


def create_table(conn: Connection):
    query = """
    CREATE TABLE IF NOT EXISTS repairings_askar (
        id SERIAL PRIMARY KEY,
        description VARCHAR(255) NOT NULL,
        city VARCHAR(255) NOT NULL,
        price INTEGER NOT NULL,
        loss_estimate INTEGER NOT NULL,
        amount INTEGER,
        created DATE DEFAULT NOW(),
        status VARCHAR(255) DEFAULT 'new'
        )
    """


    conn.execute(text(query))
    conn.commit()


def insert_repairing(conn: Connection, repairing: Repairing):
    query = """
    INSERT INTO repairings_askar (description, city, price, loss_estimate, amount)
    VALUES (:description, :city, :price, :loss_estimate, :amount)
    """


    conn.execute(
        text(query),
        parameters={
            "description": repairing.description,
            "city": repairing.city,
            "price": repairing.price,
            "loss_estimate": repairing.loss_estimate,
            "amount": repairing.amount,
        },
    )
    conn.commit()


def update_repairing(conn: Connection):
    query = "UPDATE repairings_askar SET amount=price*loss_estimate, status='paid' WHERE status='new';"

    conn.execute(text(query))
    conn.commit()


def complete_repairing(conn: Connection):
    query = "UPDATE repairings_askar SET status='done' WHERE status='paid';"
    conn.execute(text(query))
    conn.commit()

def get_repairing(conn: Connection) -> list[Repairing]:
    query = "SELECT * FROM repairings_askar;"
    print("good")
    repairing = conn.execute(text(query)).fetchall()
    print("very_good")
    return [Repairing(
        id=repairing[0],
        description=repairing[1],
        city=repairing[2],
        price=repairing[3],
        loss_estimate=repairing[4],
        amount=repairing[5],
        created=repairing[6],
        status=repairing[7]
    ) for repairing in repairing]


