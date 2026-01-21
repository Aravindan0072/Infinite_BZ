# Infinite BZ - Project Structure Analysis

## Overview
**Infinite BZ** is a full-stack event management platform built with a modern tech stack focused on performance and scalability.
- **Frontend**: React (Vite) + Tailwind CSS
- **Backend**: Python (FastAPI) + PostgreSQL (Async)
- **Scraping**: Playwright + BeautifulSoup

## 📂 Project Directory Breakdown

### 1. Frontend (`/frontend`)
The user interface is built with React and Vite for fast development.

*   `src/components/`: Modular UI components.
    *   **Core Pages**: `Dashboard.jsx`, `LandingPage.jsx`, `SettingsPage.jsx`.
    *   **Event Management**: `CreateEventPage.jsx`, `CreateEventModal.jsx`, `MyEvents.jsx`.
    *   **Shared UI**: `Sidebar.jsx`, `EventFeed.jsx`, `EventDetailModal.jsx`.
    *   **Auth**: `AuthPage.jsx` (Login/Signup).
*   `src/App.jsx`: Main application router setup.
*   `vite.config.js`: Configuration for the Vite build tool and dev server.

### 2. Backend (`/backend`)
A high-performance asynchronous API using FastAPI.

*   `app/`
    *   `api/`: API Endpoints.
        *   `routes.py`: Main event routes (list, create, sync).
        *   `auth_routes.py`: Authentication (Login, Signup, Google Auth).
    *   `core/`: Core configuration.
        *   `database.py`: Async Database connection setup.
        *   `security.py`: JWT token handling and password hashing.
    *   `models/`: Database Schemas (Table definitions).
        *   `schemas.py`: Defines `Event`, `User`, `UserRegistration` tables.
    *   `services/`: Business Logic.
        *   `scraper.py`: Playwright scraper for Eventbrite/Meetup.
        *   `auth_service.py`: User management logic.
*   **Root Scripts**:
    *   `run.py`: Entry point to start the server.
    *   `sync_patch.py`: **Critical** script for applying DB schema updates manually.
    *   `check_db_count.py`: Utility to verify database data.

### 3. Database (`PostgreSQL`)
*   **Tables**: `user`, `event`, `userregistration`.
*   **Status**: Schema is fully patched with recent updates (`first_name`, `category`, etc.).

## 🔄 Key Workflows
1.  **Event Aggregation**: `scraper.py` fetches external events -> `routes.py` (sync endpoint) saves to DB.
2.  **User Creation**: `AuthPage.jsx` -> `auth_routes.py` -> `DB`.
3.  **Event Creation**: `id` generated as `chk-{uuid}` -> stored as Internal Event (`source='InfiniteBZ'`).
