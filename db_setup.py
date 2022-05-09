import sqlite3

conn = sqlite3.connect('status.db')  # Warning: This file is created in the current directory
conn.execute("CREATE TABLE status (name TEXT PRIMARY KEY, status TEXT NOT NULL, link TEXT NOT NULL, detail TEXT)")
conn.execute("INSERT INTO status (name,status,link) VALUES ('testname','ok', 'example.com')")
conn.commit()
