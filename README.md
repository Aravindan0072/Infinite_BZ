# Infinite Tech AI - Event Aggregator Web Application

A comprehensive full-stack web application designed to aggregate, filter, and manage professional networking events. Built for "Infinite Tech AI", it features auto-registration capabilities using Playwright automation.

## 🚀 Technologies Used

### Frontend
*   **Framework**: React (Vite)
*   **Styling**: Tailwind CSS (Custom Dark/Cyan Theme)
*   **Icons**: Lucide React
*   **State Management**: React Hooks (useState, useEffect)
*   **HTTP Client**: Built-in Fetch API

### Backend
*   **Framework**: FastAPI (Python)
*   **Database**: PostgreSQL (via SQLModel/SQLAlchemy)
*   **Automation**: Playwright (for scraping and auto-registration)
*   **Authentication**: JWT (JSON Web Tokens) + Google OAuth
*   **Server**: Uvicorn

## 📂 Project Structure

```
Infinite_BZ/
├── backend/            # Python FastAPI Backend
│   ├── app/            # Main Application Code
│   │   ├── api/        # API Routes
│   │   ├── models/     # Database Models (SQL Model)
│   │   └── services/   # Business Logic (Scraper, Registrar)
│   ├── requirements.txt
│   └── run.py          # Entry point
│
├── frontend/           # React Frontend
│   ├── src/            # Source Code
│   └── tailwind.config.js
```

## 🛠️ Setup Instructions

### Prerequisites
*   Python 3.10+
*   Node.js & npm
*   PostgreSQL Database

### 1. Backend Setup
Navigate to the backend directory:
```bash
cd backend
```

Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
playwright install  # Install browser binaries
```

Run the server:
```bash
python run.py
```
*The backend runs on http://localhost:8000*

### 2. Frontend Setup
Navigate to the frontend directory:
```bash
cd frontend
```

Install dependencies:
```bash
npm install
```

Run the development server:
```bash
npm run dev
```
*The frontend runs on http://localhost:5173*

## ✨ Key Features
*   **Event Aggregation**: Scrapes and displays events from Eventbrite and other sources.
*   **Advanced Filtering**: Filter by City, Industry, Date, Cost, and Mode (Online/Offline).
*   **Auto-Registration**: Automates the checkout process for free events using Playwright.
*   **User Dashboard**: Track registered events and view statistics.
*   **Dark Mode Theme**: Premium "Infinite Tech AI" dark theme with Cyan accents.

## 🤝 Contribution
1.  Clone the repository.
2.  Create a feature branch.
3.  Commit your changes.
4.  Push to the branch and open a Pull Request.
