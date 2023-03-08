import time
from sql_queries import create_table, get_repairing
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        repairing = get_repairing(conn)
        print("-------------------- >>")
        for repairing in repairing:
            print(repairing)
        print("-------------------- <<")
        time.sleep(5)