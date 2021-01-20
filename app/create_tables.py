reateimport psycopg2

def create_tables():
     """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS teams (
            response_id SERIAL PRIMARY KEY,
            sportsdata_response jsonb
        )
        """,)
    conn = None
    try:
        # read the connection parameters
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
        host="localhost",
        database="analytics",
        user="analytics",
        password="analytics")
        cur = conn.cursor()
        # CREATE TABLE IF NOT EXISTS one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()