def answer_query(query: str, outlets: list):
    query = query.lower()
    if "24 hours" in query:
        return [o for o in outlets if "24 Hours" in o["features"]]
    elif "birthday" in query:
        return [o for o in outlets if "Birthday Party" in o["features"]]
    return ["Sorry, I couldn't understand the query."]