import time
from sql_queries import create_table, complete_repairing
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        complete_repairing(conn)
        print("completed")
        time.sleep(20)
