import pandas as pd
import sqlite3

# Read data from excel file
data = pd.read_excel(r"SQL_oppgave2/Postnummerregister.xlsx")

# Connect to database
conn = sqlite3.connect("Random.db")
c = conn.cursor()

def funcCreateTable():
    # Create a table with required columns and primary key so there wouldn't be duplicates
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS postnummerBasen (
        Postnummer TEXT,
        Poststed TEXT,
        Kommunenummer TEXT, 
        Kommunenavn TEXT,
        Kategori TEXT,
        PRIMARY KEY(Postnummer)
        )
        """
        )

def funcInsertData():
    # Loop to insert data from the Excel file into the table
    for index, row in data.iterrows():
        postnummer = str(row['Postnummer']).zfill(4)
        komunenummer = str(row['Kommunenummer']).zfill(4)
        c.execute(
            """
            INSERT INTO postnummerBasen (Postnummer, Poststed, Kommunenummer, Kommunenavn, Kategori)
            VALUES (?,?,?,?,?)
            """,
            (postnummer, row['Poststed'], komunenummer, row['Kommunenavn'], row['Kategori'])
        )

def main():
    funcCreateTable()
    funcInsertData()
    # committing everything into database and closing connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
