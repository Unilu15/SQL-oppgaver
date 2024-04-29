import pandas as pd
import sqlite3

# Read datad from excel file
data = pd.read_csv(r"SQL_oppgave1/randoms.csv")

# Connect to database
conn = sqlite3.connect("SQL_oppgave1/Random.db")
c = conn.cursor()

def funcCreateTable():
    # Create a table with required columns and primary key so there wouldn't be duplicates
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS userData (
        fname str,
        ename str,
        epost str,
        tlf int,
        postnummer int,
        PRIMARY KEY(epost)
        )
        """
        )

def funcInsertData():
    # for loop for inserting everything from csv file in corect rows
    for index, row in data.iterrows():
        c.execute(
            """
            INSERT INTO userData (fname, ename, epost, tlf, postnummer)
            VALUES (?,?,?,?,?)
            """,
            (row['fname'], row['ename'], row['epost'], row['tlf'], row['postnummer'])
        )

def main():
    funcCreateTable()
    funcInsertData()

if __name__ == "__main__":
    main()

# committing everything into database and closing connection
conn.commit()
conn.close()