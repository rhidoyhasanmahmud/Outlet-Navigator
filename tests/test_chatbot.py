from chatbot import gpt_chatbot

sample_outlets = [
    {
        "name": "McDonald's Bukit Bintang",
        "address": "120-120A Jalan Bukit Bintang, KL",
        "phone": "03-12345678",
        "latitude": 3.14,
        "longitude": 101.71,
        "features": ["24 Hours", "Birthday Party"],
        "waze_link": "https://waze.com/test"
    }
]


def test_answer_query(monkeypatch):
    class FakeResponse:
        choices = [{"message": {"content": "Test GPT response"}}]

    monkeypatch.setattr(gpt_chatbot.openai.ChatCompletion, "create", lambda **kwargs: FakeResponse())
    result = gpt_chatbot.answer_query("Which outlets are 24 hours?", sample_outlets)
    assert "Test GPT response" in result