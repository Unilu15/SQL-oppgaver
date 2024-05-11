import pandas as pd
import sqlite3

# Read datad from excel file
data = pd.read_excel(r"SQL_oppgave2/Postnummerregister.xlsx")

# Connect to database
conn = sqlite3.connect("Random.db")
c = conn.cursor()

def funcCreateTable():
    # Create a table with required columns and primary key so there wouldn't be duplicates
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS postnummerBasen (
        Postnummer int(4),
        Poststed str,
        Kommunenummer int(4), 
        Kommunenavn str,
        Kategori str,
        PRIMARY KEY(postnummer)
        )
        """
        )

def funcInsertData():
    # Loop to insert data from the CSV file into the table
    for index, row in data.iterrows():
        
        c.execute(
            """
            INSERT INTO postnummerBasen (Postnummer, Poststed, Kommunenummer, Kommunenavn, Kategori)
            VALUES (?,?,?,?,?)
            """,
            (row['Postnummer'], row['Poststed'], row['Kommunenummer'], row['Kommunenavn'], row['Kategori'])
        )



def main():
    funcCreateTable()
    funcInsertData()

if __name__ == "__main__":
    main()

# committing everything into database and closing connection
conn.commit()
conn.close()