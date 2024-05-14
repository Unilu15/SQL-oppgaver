import sqlite3

def create_database():
    # Function to create the "kundeliste" database
    try:
        connection = sqlite3.connect('kundeliste.db')
        cursor = connection.cursor()
        
        # Create kundeinfo table
        cursor.execute('''CREATE TABLE IF NOT EXISTS kundeinfo (
                            kundenummer INTEGER PRIMARY KEY,
                            navn TEXT,
                            adresse TEXT,
                            telefonnummer TEXT
                            )''')
        
        # Create postnummer_tabell table
        cursor.execute('''CREATE TABLE IF NOT EXISTS postnummer_tabell (
                            postnummer TEXT PRIMARY KEY,
                            sted TEXT
                            )''')
        
        connection.commit()
        print("Database created successfully!")
    except sqlite3.Error as error:
        print("Error creating database:", error)
    finally:
        if connection:
            connection.close()

def fill_tables():
    # Function to fill tables with data from provided files
    try:
        connection = sqlite3.connect('kundeliste.db')
        cursor = connection.cursor()
        
        cursor.execute("INSERT INTO kundeinfo(kundenummer, navn, adresse, telefonnummer) VALUES(?,?,?,?)",
                       (1, "Bob", "Oslo", 394830482))
        
        connection.commit()
        print("Tables filled with data successfully!")
    except sqlite3.Error as error:
        print("Error filling tables with data:", error)
    finally:
        if connection:
            connection.close()

def display_customer_info():
    # Function to display all information about a customer
    try:
        connection = sqlite3.connect('kundeliste.db')
        cursor = connection.cursor()

        kundenummer = input("Enter customer number: ")
        
        # Code to retrieve and display customer information based on kundenummer
        
    except sqlite3.Error as error:
        print("Error:", error)
    finally:
        if connection:
            connection.close()

def main():
    create_database()
    fill_tables()
    display_customer_info()

if __name__ == "__main__":
    main()
