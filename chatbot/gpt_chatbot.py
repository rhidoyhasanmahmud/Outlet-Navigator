import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def format_outlet(outlet: dict) -> str:
    return f"\n- {outlet['name']} | {outlet['address']} | Features: {', '.join(outlet['features'])}"

def answer_query(query: str, outlets: list) -> str:
    context = "".join([format_outlet(o) for o in outlets])
    prompt = f"""
You are an assistant that helps users find McDonald's outlets in Kuala Lumpur based on their query.

User's query:
"{query}"

Available outlet data:
{context}

Provide a concise, friendly response listing the matching outlet names and details. If none match, say so.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message['content']
