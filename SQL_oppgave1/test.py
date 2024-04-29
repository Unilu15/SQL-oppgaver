import pandas as pd
import sqlite3

data = pd.read_csv(r"SQL_oppgave1/randoms.csv")

conn = sqlite3.connect("SQL_oppgave1/Random.db")
c = conn.cursor()

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

for index, row in data.iterrows():
    c.execute(
        """
        INSERT INTO userData (fname, ename, epost, tlf, postnummer)
        VALUES (?,?,?,?,?)
        """,
        (row['fname'], row['ename'], row['epost'], row['tlf'], row['postnummer'])
    )

conn.commit()
conn.close()
