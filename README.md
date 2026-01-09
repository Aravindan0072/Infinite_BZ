# InfiniteBZ - Community Event Platform

InfiniteBZ is a comprehensive event management platform tailored for local communities (currently Chennai). It aggregates events from multiple sources (like Eventbrite) and allows users to create and manage their own listing directly on the platform.

## Features

*   **Aggregated Feed**: Automatically scrapes and displays tech and networking events from external sources.
*   **User Events**: detailed "Create Event" wizard for users to host their own meetups.
*   **My Events Dashboard**: A personalized dashboard for organizers to track active events and registrations.
*   **Rich Event Details**: Premium, immersive event detail views with agenda, speakers, and location maps.
*   **Authentication**: Secure JWT-based signup and login system.
*   **Admin Analytics**: Backend stats for track platform growth.

## Tech Stack

### Frontend
*   **React (Vite)**: Fast, modern UI library.
*   **Tailwind CSS**: For a sleek, dark-themed responsive design.
*   **Lucide React**: Beautiful, consistent iconography.

### Backend
*   **FastAPI**: High-performance Python framework.
*   **SQLModel / SQLAlchemy**: Async ORM for Postgres interaction.
*   **PostgreSQL**: Robust relational database.
*   **Playwright**: For advanced web scraping capabilities.
*   **APScheduler**: For background tasks and data synchronization.

## Setup & Run

### Prerequisites
*   Node.js & npm
*   Python 3.10+
*   PostgreSQL Database

### 1. Backend Setup
```bash
cd backend
python -m venv venv
# Activate venv (Windows: .\venv\Scripts\activate, Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
playwright install
python run.py
```
*   Server runs on `http://localhost:8000`
*   Docs available at `http://localhost:8000/docs`

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
*   App runs on `http://localhost:5173` (or similar port)

## Project Structure
*   `/backend`: FastAPI application, database models, and scraper logic.
*   `/frontend`: React application, components, and assets.

## License
MIT

## Latest Updates (Jan 2026) -> "Antigravity" Refactor

### Create Event Page Overhaul
*   **Split-Screen Layout**: Implemented a responsive 60/40 grid layout with a scrollable form and sticky live preview.
*   **Antigravity Design**: Floating dock, glassmorphism effects, glowing borders, and smooth slide-down animations.
*   **Pro Features**:
    *   **Ticketing**: Support for Free vs Paid events, capacity limits, and registration deadlines.
    *   **Smart Location**: Dynamic toggle between Physical Venue and Virtual Meeting Link.
    *   **Time Zone**: Persistent time zone selector for global event planning.
    *   **Rich Text**: Custom WYSIWYG editor with Lucide-icon toolbar for event descriptions.

### Event Detail UI Refactor
*   **Pro-Level Dashboard Modal**: Internal "InfiniteBZ" events now open in a premium, glassmorphic modal instead of redirecting externally.
*   **Smart Layout**: 
    *   **Desktop**: Sticky sidebar keeps engagement actions (Price, Register) always visible.
    *   **Mobile**: Fluid scrolling layout prevents content overlap.
*   **Auto-Registration**: Seamless one-click registration integration with the backend API.
*   **Source Differentiation**: Visual indicators (Eye vs External Link) to distinguish between Community Events and External Listings (Eventbrite/Meetup).
*   **Image Upload**: Integrated local file upload support for custom event cover images.

### My Events & Interaction Refactor (Jan-2 2026)
*   **My Events Dashboard**:
    *   **Dynamic Data**: Replaced static placeholders with real-time data fetching from `/api/v1/events/my-events`.
    *   **Live Stats**: Client-side calculation for "Active Events", "Pending", and "Total Registrations".
    *   **Actionable UI**: Integrated Search, Sort (Newest/Oldest), and Delete functionality with immediate UI updates.
*   **Create Event Refinement**:
    *   **Dark Theme Enforcement**: Strict adherence to `bg-slate-900`/`text-white` with `cyan-500` accents.
    *   **Rich Content**: Added support for comprehensive **Agenda** and **Speaker** profiles.
*   **Backend Flexibility**: 
    *   Updated `Event` model to store rich content (Agenda/Speakers) in a flexible `raw_data` JSONB column, avoiding rigid schema migrations.
*   **Unified Navigation**: `EventFeed` now consistently opens the detailed internal modal for *all* events, improving the user journey.
