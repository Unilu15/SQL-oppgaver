import sqlite3

# Database file name
DB_NAME = 'kundeliste.db'

def funcCreateDatabase():
    """Create the database and tables."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Create kundeinfo table
    c.execute('''CREATE TABLE IF NOT EXISTS kundeinfo (
                    kundenummer INTEGER PRIMARY KEY,
                    navn TEXT NOT NULL,
                    adresse TEXT NOT NULL,
                    postnummer INTEGER,
                    FOREIGN KEY(postnummer) REFERENCES postnummer_tabell(postnummer)
                )''')

    # Create postnummer_tabell table
    c.execute('''CREATE TABLE IF NOT EXISTS postnummer_tabell (
                    postnummer INTEGER PRIMARY KEY,
                    poststed TEXT NOT NULL
                )''')

    conn.commit()
    conn.close()

# Function for inserting data in tables
def funcInsertData():
    """Populate tables with data from files."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Sample data for postnummer_tabell
    postnummer_data = [
        (1234, 'Oslo'),
        (5678, 'Bergen'),
        (9101, 'Trondheim')
    ]

    # Sample data for kundeinfo
    kundeinfo_data = [
        (1, 'Ola Nordmann', 'Gate 1', 1234),
        (2, 'Kari Nordmann', 'Gate 2', 5678),
        (3, 'Per Hansen', 'Gate 3', 9101)
    ]

    c.executemany('INSERT OR IGNORE INTO postnummer_tabell VALUES (?, ?)', postnummer_data)
    c.executemany('INSERT OR IGNORE INTO kundeinfo VALUES (?, ?, ?, ?)', kundeinfo_data)

    conn.commit()
    conn.close()

# Function for displaying information about person
def funcDisplayInfo(kundenummer):
    """Fetch and display all information about a customer."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # This command joins two tables and displays all of the info known about that person
    c.execute('''SELECT kundeinfo.kundenummer, kundeinfo.navn, kundeinfo.adresse, postnummer_tabell.poststed
                 FROM kundeinfo
                 JOIN postnummer_tabell ON kundeinfo.postnummer = postnummer_tabell.postnummer
                 WHERE kundeinfo.kundenummer = ?''', (kundenummer,))
    result = c.fetchone()
    conn.close()

    if result:
        print(f"Kundenummer: {result[0]}\nNavn: {result[1]}\nAdresse: {result[2]}\nPoststed: {result[3]}")
    else:
        print("Kunde ikke funnet.")

# Function for removing data from table
def funcRemoveData(kundenummer):
    """Delete a customer by kundenummer."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('DELETE FROM kundeinfo WHERE kundenummer = ?', (kundenummer,))
    conn.commit()
    conn.close()

def main():
    funcCreateDatabase()
    funcInsertData()

    # Infinite loop of menu unless the choice is 3, then it ends
    while True:
        print("\n1. Vis kundeinformasjon")
        print("2. Slett kunde")
        print("3. Avslutt")
        choice = input("Velg et alternativ: ")

        if choice == '1':
            kundenummer = int(input("Skriv inn kundenummer: "))
            funcDisplayInfo(kundenummer)
        elif choice == '2':
            kundenummer = int(input("Skriv inn kundenummer å slette: "))
            funcRemoveData(kundenummer)
            print("Databasen er nullstilt og fylt med standard data.")
        elif choice == '3':
            break
        else:
            print("Ugyldig valg, prøv igjen.")

if __name__ == '__main__':
    main()
