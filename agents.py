from database import cursor, conn

# ---------------- TASK AGENT ----------------
def task_agent(query):
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (query,))
    conn.commit()
    return "Task added successfully"

# ---------------- CALENDAR AGENT ----------------
def calendar_agent(query):
    return "Meeting scheduled"

# ---------------- NOTES AGENT ----------------
def notes_agent(query):
    cursor.execute("INSERT INTO notes (note) VALUES (?)", (query,))
    conn.commit()
    return "Note saved"

# ---------------- MAIN AGENT ----------------
def main_agent(query):
    q = query.lower()

    if "task" in q:
        return task_agent(query)

    elif "meeting" in q or "schedule" in q:
        return calendar_agent(query)

    elif "note" in q:
        return notes_agent(query)

    else:
        return "No action detected"