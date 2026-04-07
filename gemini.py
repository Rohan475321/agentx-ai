import google.generativeai as genai

genai.configure(api_key="AIzaSyClCFsPEHz8PXtG_P5F-jp-j-Ykk3zLyG8")

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(query):
    prompt = f"""
    Classify the user query into one word ONLY:

    task
    meeting
    note

    Respond with ONLY ONE WORD.
    No sentence. No explanation.

    Query: {query}
    """

    try:
        response = model.generate_content(prompt)
        text = response.text.strip().lower()

        # clean output
        if "task" in text:
            return "task"
        elif "meeting" in text:
            return "meeting"
        elif "note" in text:
            return "note"
        else:
            return ""

    except Exception as e:
        print("Gemini error:", e)
        return ""