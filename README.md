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

### My Events Page Revamp (Jan 2026)
*   **Premium Glassmorphic UI**: Completely overhauled visually to match the "Antigravity" aesthetic with gradient stats cards and transparent tables.
*   **Full Event Management**:
    *   **Edit Functionality**: Re-uses the Create Event wizard in "Time Travel" (Edit) mode to update event details.
    *   **Delete Functionality**: Secure, confirmation-gated deletion of events.
    *   **Analytics Integration**: Dedicated "Eye" view for detailed event statistics (Revenue, Sales Trends).
*   **Backend Enhancements**: Added secure `DELETE` and `PUT` endpoints with ownership verification.

## License
MIT

# SettingsPage Component

A comprehensive user profile settings page component built with React for the Infinite_BZ application.

## Overview

The SettingsPage component allows authenticated users to manage their profile information, upload profile pictures, and view their account statistics. It provides a clean, modern interface with real-time validation and profile completion tracking.

## Features

### Profile Management
- **Personal Information Editing**: First name, last name, email, phone, job title, company, and bio
- **Profile Image Upload**: Support for image uploads with validation (type and size)
- **Real-time Preview**: Instant profile image preview before saving
- **Auto-population**: Automatically fills fields with Google OAuth data and existing profile data

### User Statistics
- **Profile Completion Percentage**: Calculates completion based on filled fields
- **Account Status**: Shows active/inactive status with visual indicators
- **Activity Metrics**:
  - Events attended count
  - Auto-registrations count
  - Linked accounts count

### UI/UX Features
- **Responsive Design**: Works on desktop and mobile devices
- **Dark Theme**: Consistent with the application's dark theme
- **Success Feedback**: Shows confirmation message after successful saves
- **Navigation**: Back to dashboard button for easy navigation

## Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `user` | Object | Yes | User object containing authentication data (email, full_name, is_active) |
| `onNavigate` | Function | Yes | Navigation callback function to handle page transitions |


```

## State Management

The component manages the following state:

- `formData`: Object containing all form field values
- `profileImagePreview`: Base64 string for image preview
- `showSuccessMessage`: Boolean to control success message display

## API Integration

### Fetch Profile Data
- **Endpoint**: `GET /api/v1/user/profile`
- **Headers**: Authorization Bearer token
- **Purpose**: Loads existing profile data on component mount

### Update Profile Data
- **Endpoint**: `PUT /api/v1/user/profile`
- **Headers**: Authorization Bearer token, Content-Type application/json
- **Body**: Profile data object
- **Purpose**: Saves updated profile information

## Validation

### Image Upload Validation
- **File Type**: Must be an image (checked via MIME type)
- **File Size**: Maximum 5MB
- **Error Handling**: User-friendly error messages for invalid uploads

### Form Validation
- Relies on browser-native validation for email and phone fields
- All fields are optional but contribute to profile completion percentage

## Dependencies

- **React**: Core framework
- **Lucide React**: Icons (ArrowLeft, Check, X)
- **Tailwind CSS**: Styling framework

## Styling

- Uses Tailwind CSS classes for responsive design
- Dark theme with slate color palette
- Gradient backgrounds for profile image placeholders
- Hover effects and transitions for interactive elements

## Accessibility

- Proper label associations for form inputs
- Semantic HTML structure
- Keyboard navigation support
- Screen reader friendly icons and text

## Performance Considerations

- Lazy loading of profile data
- Efficient image preview using FileReader API
- Minimal re-renders through proper state management
- Base64 image handling for instant preview

## Error Handling

- Network request error handling with try-catch blocks
- User-friendly error messages for failed operations
- Console logging for debugging purposes

## Future Enhancements

Potential improvements for the component:

- Password change functionality
- Account deletion option
- Two-factor authentication settings
- Notification preferences
- Privacy settings
- Data export functionality

## Component Structure

```
SettingsPage/
├── Profile Card (Left Sidebar)
│   ├── Profile Image
│   ├── Image Upload
│   ├── User Info Display
│   ├── Profile Completion
│   └── Statistics Cards
└── Settings Form (Right Content)
    ├── Success Message
    └── Personal Information Form
        ├── Name Fields
        ├── Contact Fields
        ├── Professional Fields
        └── Bio Field
```
# My Registrations Page

## Overview

The My Registrations page is a dedicated interface for users to view and manage all their event registrations in the InfiniteBZ Event Management System. This page provides a comprehensive view of registered events with advanced filtering, QR code access, and calendar integration features.

## Features

### 📋 Event Listings
- **Grid Layout**: Events displayed in a responsive 1-3 column grid
- **Visual Cards**: Each event shown as an attractive card with event images, details, and status
- **Registration Status**: Clear "Registered" badges on confirmed events

### 🔍 Filtering & Search
- **Tab Navigation**:
  - **Going**: Upcoming events you've registered for
  - **Saved**: Events you've saved for later
  - **Past**: Previously attended events
- **Search Bar**: Real-time search through event titles and details
- **Date Filtering**: Filter events by specific dates

### 🎫 QR Code Access
- **QR Code Modal**: Click any event's QR Code icon to view
- **Professional Display**: Styled modal with event branding
- **Scan Instructions**: Clear guidance for QR code usage
- **Verification Ready**: QR codes contain all necessary verification data

### 📅 Calendar Integration
- **Google Calendar**: Click "Add to Calendar" to open Google Calendar
- **Pre-filled Details**: Event title, date, time, location, and description
- **One-click Addition**: Direct integration with Google Calendar

### 📱 Responsive Design
- **Mobile Optimized**: Perfect display on all device sizes
- **Adaptive Layout**: Columns adjust based on screen width
- **Touch Friendly**: Optimized for mobile interactions

## User Interface

### Header Section
```
InfiniteBZ | [Search Bar] | [Profile Menu] | [Buttons]
```

### Tab Navigation
```
✓ Going    📌 Saved    ↩ Past
```

### Event Cards
Each event displays:
- **Event Image**: Hero image with gradient overlay
- **Registration Badge**: Green "Registered" indicator
- **Event Title**: Prominent title display
- **Event Details**: Date, time, venue, registration date
- **Action Buttons**: QR Code and Calendar icons

### QR Code Modal
```
┌─────────────────────────────────────┐
│ 🎫 Event QR Code                    │
│ [Event Title]                       │
│                                     │
│ ┌─────────────────┐                 │
│ │    QR CODE      │ ← Scan Area     │
│ │                 │                 │
│ └─────────────────┘                 │
│                                     │
│ How to use:                         │
│ • Open camera app                   │
│ • Point at QR code                  │
│ • Details will display              │
│                                     │
│ [Close] [Download QR]               │
└─────────────────────────────────────┘
```

## API Integration

### Data Sources
- **User Registrations**: `/api/v1/user/registrations`
- **QR Code Generation**: `/api/v1/user/registrations/{event_id}/qr`
- **Calendar Integration**: Direct Google Calendar API

### Response Format
```json
{
  "registrations": [
    {
      "id": 123,
      "title": "Tech Conference 2024",
      "start_time": "2024-01-15T10:00:00Z",
      "venue_name": "Convention Center",
      "organizer_name": "Tech Corp",
      "registration_date": "2024-01-01T08:30:00Z",
      "confirmation_id": "SELF-1734071053"
    }
  ],
  "total": 1
}
```

## Technical Implementation

### Components
- **MyRegistrationsPage.jsx**: Main container component
- **State Management**: React hooks for data and UI state
- **API Integration**: Fetch user registrations and QR codes
- **Modal System**: QR code display modal

### Key Functions
```javascript
fetchUserRegistrations()     // Load user registrations
handleShowQr(eventId)        // Display QR code modal
handleAddToCalendar(event)   // Open Google Calendar
getFilteredRegistrations()   // Apply filters and search
```

### Styling
- **Tailwind CSS**: Utility-first styling framework
- **Responsive Design**: Mobile-first approach
- **Dark Theme**: Consistent with app branding
- **Custom Colors**: Primary (#148EAB) and accent colors

## Usage Guide

### Viewing Registrations
1. Navigate to the "My Registrations" section
2. Use tabs to filter between Going, Saved, and Past events
3. Use the search bar to find specific events
4. Scroll through the event grid

### Accessing QR Codes
1. Click the "QR Code" icon on any registered event
2. View the professional QR code modal
3. Use device camera to scan the code
4. QR contains: Ticket ID, Event, User, Valid date/time

### Adding to Calendar
1. Click the "Add to Calendar" icon
2. Google Calendar opens in new tab
3. Event details are pre-filled
4. Click "Save" in Google Calendar

## Security & Privacy

### Data Protection
- **User Authentication**: Required for accessing registrations
- **Personal Data**: Only user's own registrations displayed
- **QR Security**: Contains verification data, not sensitive information

### Privacy Features
- **Scoped Access**: Users only see their own registrations
- **Secure Tokens**: API calls require authentication
- **Data Encryption**: All data transmission encrypted

## Troubleshooting

### Common Issues

**QR Code Not Loading**
- Check internet connection
- Ensure event registration is confirmed
- Try refreshing the page

**Calendar Integration Not Working**
- Ensure Google account is logged in
- Check popup blocker settings
- Try in different browser

**Events Not Showing**
- Verify registration status
- Check internet connection
- Refresh the page

### Support
For technical issues, contact the InfiniteBZ support team or check the system logs for error details.

## Future Enhancements

### Planned Features
- **Bulk Actions**: Select multiple events for actions
- **Export Options**: Download registration lists
- **Push Notifications**: Event reminders
- **Social Sharing**: Share registered events
- **Advanced Filters**: Category and location filters

### Performance Improvements
- **Lazy Loading**: Load events on demand
- **Caching**: Cache frequently accessed data
- **Offline Support**: Basic functionality without internet

---

**InfiniteBZ Event Management System** | My Registrations Module
