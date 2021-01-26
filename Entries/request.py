from Models.Mood import Mood
from sqlite3.dbapi2 import connect
from Models.Entry import Entry
import sqlite3
import json

def get_all_entries():
    with sqlite3.connect("./dailyJournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor= conn.cursor()

        db_cursor.execute(""" 
        SELECT
            e.id,
            e.entry,
            e.concept,
            e.date,
            e.moodId,
            m.mood
        from Entry E
        JOIN Mood m on m.id = e.moodId
        """)

        entries = []
    
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['date'] , row['moodId'])
            mood = Mood(row['moodId'], row['mood']).__dict__
            entry.mood = mood
            entries.append(entry.__dict__)
            
    return json.dumps(entries)

def get_entries_by_search_term(search_term):

    with sqlite3.connect("./dailyJournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            e.id,
            e.entry,
            e.concept,
            e.date,
            e.moodId,
            m.mood
        from Entry E
        JOIN Mood m on m.id = e.moodId
        WHERE e.entry LIKE ? 
        """, ( "%" + search_term + "%", ))

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['date'] , row['moodId'])
            mood = Mood(row['moodId'], row['mood']).__dict__
            entry.mood = mood
            entries.append(entry.__dict__)

    return json.dumps(entries)