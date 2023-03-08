import time
from sql_queries import create_table, update_repairing
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        update_repairing(conn)
        print("updated")
        time.sleep(20)
