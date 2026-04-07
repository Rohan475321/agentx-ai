from gemini import ask_gemini
from database import cursor, conn

# -------- TASK AGENT --------
def task_agent(query):
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (query,))
    conn.commit()
    return "Task added successfully"

# -------- CALENDAR AGENT --------
def calendar_agent(query):
    return "Meeting scheduled"

# -------- NOTES AGENT --------
def notes_agent(query):
    cursor.execute("INSERT INTO notes (note) VALUES (?)", (query,))
    conn.commit()
    return "Note saved"

# -------- MAIN AGENT --------
def main_agent(query):
    try:
        decision = ask_gemini(query)
        print("Gemini decision:", decision)

        if decision == "task":
            return task_agent(query)
        elif decision == "meeting":
            return calendar_agent(query)
        elif decision == "note":
            return notes_agent(query)

    except Exception as e:
        print("Agent error:", e)

    # 🔥 fallback logic
    q = query.lower()

    if "task" in q or "complete" in q:
        return task_agent(query)
    elif "meeting" in q or "call" in q:
        return calendar_agent(query)
    elif "note" in q or "remember" in q:
        return notes_agent(query)

    return "No action detected"