# 🍟 Outlet-Navigator

This project is a full-stack web application that scrapes McDonald's outlet data in Kuala Lumpur from the official website and provides:

- ✅ Automated web scraping using Playwright
- ✅ Structured data parsing with BeautifulSoup
- ✅ Backend API with FastAPI & SQLite
- ✅ Interactive map frontend with Leaflet.js
- ✅ Chatbot-ready filtering layer

---

## 📦 Project Structure
```
Outlet-Navigator/
├── scraper/           # Scraping logic, parser, and service
├── api/               # FastAPI backend with CORS
├── database/          # SQLAlchemy DB setup
├── frontend/          # HTML + Leaflet map
├── chatbot/           # Query mock layer
├── main.py            # Run scraper + populate DB
├── requirements.txt   # Dependencies
└── README.md          # You're here :)
```