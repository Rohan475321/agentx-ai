import google.generativeai as genai

genai.configure(api_key="AIzaSyClCFsPEHz8PXtG_P5F-jp-j-Ykk3zLyG8")

model = genai.GenerativeModel("gemini-pro")

def ask_gemini(query):
    prompt = f"""
    Decide action:
    task / meeting / note

    Query: {query}
    """

    response = model.generate_content(prompt)
    return response.text.strip().lower()