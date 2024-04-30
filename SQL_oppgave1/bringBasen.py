import pandas as pd
import sqlite3

# Read datad from excel file
data = pd.read_csv(r"SQL_oppgave1/Postnummerregister.csv")

# Connect to database
conn = sqlite3.connect("SQL_oppgave1/Random.db")
c = conn.cursor()

def funcCreateTable():
    # Create a table with required columns and primary key so there wouldn't be duplicates
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS postnummerBasen (
        postnummer int,
        poststed TEXT,
        kommunenummer int,
        kommunenavn TEXT,
        kategori TEXT,
        PRIMARY KEY(postnummer)
        )
        """
        )

def funcInsertData():
    # for loop for inserting everything from csv file in corect rows
    for index, row in data.iterrows():
        c.execute(
            """
            INSERT INTO userData (postnummer, poststed, kommunenummer, kommunenavn, kategori)
            VALUES (?,?,?,?,?)
            """,
            (row['postnummer'], row['poststed'], row['kommunenummer'], row['kommunenavn'], row['kategori'])
        )

def main():
    funcCreateTable()
    funcInsertData()

if __name__ == "__main__":
    main()

# committing everything into database and closing connection
conn.commit()
conn.close()