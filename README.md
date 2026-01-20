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

# Settings Page

## Overview

The Settings Page provides users with comprehensive profile management capabilities, allowing them to update personal information, upload profile images, and view account statistics. The page features a clean, two-column layout with a profile sidebar and detailed form section.

## Features

### Profile Management

#### Personal Information Form
Users can update the following fields:
- **First Name & Last Name**: From Google authentication or manual entry
- **Email Address**: Primary contact email (from authentication)
- **Phone Number**: Contact information
- **Job Title**: Professional designation
- **Company**: Organization/employer name
- **Bio/Intro**: Personal description or introduction

#### Profile Image Upload
- **File Validation**: Accepts only image files (PNG, JPG, JPEG, GIF, etc.)
- **Size Limit**: Maximum 5MB file size
- **Preview**: Real-time image preview before saving
- **Fallback**: Automatic initials-based avatar if no image is uploaded

#### Profile Completion Tracking
- **Progress Calculation**: Automatic calculation based on filled fields
- **Visual Indicator**: Percentage display (0-100%)
- **Field Tracking**: Monitors 8 key profile fields

### Account Statistics

#### Profile Card Metrics
- **Profile Completion**: Percentage of completed profile fields
- **Account Status**: Active/Inactive indicator with visual status badge
- **Plan Type**: Current subscription plan (Pro/Free)

#### Activity Statistics
1. **Events Attended**: Total events participated in
   - Weekly growth indicator
   - Real-time count updates

2. **Auto-Registrations**: Events automatically registered for
   - System-generated registrations
   - Historical tracking

3. **Linked Accounts**: Connected third-party accounts
   - Social media integrations
   - Authentication providers

### Followers Management

#### Followers Count Display
- **Live Counter**: Real-time follower count in profile sidebar
- **Clickable Link**: Opens detailed followers modal

#### Followers Modal
- **Complete List**: Shows all followers with profile information
- **Profile Images**: Displays follower avatars or initials
- **Contact Details**: Email and full name display
- **Empty State**: Friendly message when no followers exist

## Technical Implementation

### Component Structure

```
SettingsPage.jsx
├── Sidebar Navigation
├── Main Content Area
│   ├── Profile Sidebar
│   │   ├── Profile Image & Upload
│   │   ├── Personal Information
│   │   ├── Account Statistics
│   │   └── Activity Metrics
│   └── Settings Form
│       ├── Personal Information Fields
│       ├── Professional Information
│       ├── Bio Section
│       └── Save Button
└── Followers Modal
    ├── Modal Header
    ├── Followers List
    └── Empty State
```

### Key Features

#### Form State Management
```javascript
const [formData, setFormData] = useState({
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  jobTitle: '',
  company: '',
  bio: '',
  profileImage: null
});
```

#### Image Upload Validation
- **File Type Check**: `file.type.startsWith('image/')`
- **Size Validation**: `file.size > 5 * 1024 * 1024` (5MB limit)
- **Preview Generation**: FileReader API for instant previews

#### Profile Completion Algorithm
```javascript
const calculateProfileCompletion = () => {
  const fields = [formData.firstName, formData.lastName, /* ... */];
  const filledFields = fields.filter(field => field?.trim()).length;
  return Math.round((filledFields / fields.length) * 100);
};
```

### API Integration

#### Endpoints Used
- `GET /api/v1/user/profile` - Fetches existing profile data
- `PUT /api/v1/user/profile` - Updates profile information
- `GET /api/v1/user/followers` - Retrieves followers list and count

#### Data Flow
1. **Page Load**: Fetch existing profile data and followers
2. **Form Updates**: Real-time state management
3. **Save Action**: PUT request with form data
4. **Success Feedback**: 3-second success message display

### Responsive Design

#### Layout Breakpoints
- **Mobile (< lg)**: Single column layout
- **Desktop (≥ lg)**: Two-column grid (1:3 ratio)
- **Sidebar**: Fixed width with responsive margins

#### Component Responsiveness
- **Profile Card**: Collapsible on smaller screens
- **Form Fields**: Full-width on mobile, grid on desktop
- **Modal**: Centered with max-width constraints

## Usage Guidelines

### For Users

#### Updating Profile Information
1. Navigate to Settings from the sidebar
2. Fill in personal and professional information
3. Upload a profile image (optional, max 5MB)
4. Click "Save Changes" to update profile
5. Success confirmation appears for 3 seconds

#### Viewing Followers
1. Click the "X following" link in the profile sidebar
2. View complete list of followers in modal
3. Each follower shows profile image, name, and email
4. Close modal using X button

#### Understanding Statistics
- **Profile Completion**: Higher percentage indicates more complete profile
- **Events Attended**: Total events participated in
- **Auto-Registrations**: System-assisted registrations
- **Linked Accounts**: Connected external accounts

### For Developers

#### Adding New Form Fields
1. Add field to `formData` state object
2. Include in profile completion calculation
3. Add input element to form JSX
4. Update API payload in `handleSave` function

#### Customizing Validation
```javascript
const validateField = (name, value) => {
  switch (name) {
    case 'email':
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    case 'phone':
      return /^\+?[\d\s-()]+$/.test(value);
    default:
      return value?.trim().length > 0;
  }
};
```

#### Extending Statistics
1. Add new metric to profile card
2. Fetch data in `useEffect` hook
3. Update state management
4. Style with consistent design patterns

## Accessibility Features

- **Keyboard Navigation**: Full tab order support
- **Screen Readers**: Proper ARIA labels and semantic HTML
- **Form Validation**: Real-time error messaging
- **Color Contrast**: High contrast ratios for readability
- **Focus Management**: Clear focus indicators

## Browser Compatibility

- **File Upload**: Modern File API support required
- **Image Preview**: FileReader API for instant previews
- **Form Validation**: HTML5 validation with custom JavaScript
- **Responsive**: CSS Grid and Flexbox support

## Security Considerations

- **File Upload**: Server-side validation for file types and sizes
- **Data Sanitization**: Input validation and XSS prevention
- **Authentication**: Token-based API requests
- **Image Storage**: Secure file upload handling

## Future Enhancements

- **Advanced Profile Fields**: Additional customization options
- **Privacy Settings**: Granular control over profile visibility
- **Notification Preferences**: Settings for email and push notifications
- **Account Deletion**: Self-service account management
- **Two-Factor Authentication**: Enhanced security options
- **Theme Customization**: Dark/light mode preferences
- **Language Settings**: Multi-language support
- **Data Export**: Profile data download functionality

## Error Handling

### Form Validation Errors
- **File Type**: "Please select a valid image file"
- **File Size**: "Image size should be less than 5MB"
- **Save Failure**: "Failed to update profile. Please try again"

### API Error Handling
- Network failures with retry mechanisms
- Authentication errors with re-login prompts
- Server errors with user-friendly messages

## Performance Optimization

- **Lazy Loading**: Modal content loads on demand
- **Image Optimization**: Preview generation without full upload
- **State Management**: Efficient re-renders with proper state updates
- **API Calls**: Debounced saves and cached profile data

# My Registrations Page

## Overview

The My Registrations Page provides users with a comprehensive view of their event registrations, organized by status and timeline. Users can view upcoming events, past events, and manage their registrations with QR code access and calendar integration.

## Features

### Event Organization

#### Tab-Based Navigation
- **Going Tab**: Shows upcoming registered events (events with future dates)
- **Saved Tab**: Displays all registered events regardless of date
- **Past Tab**: Shows completed/attended events (events with past dates)

#### Smart Filtering
- **Date-Based Filtering**: Automatic categorization based on event start time
- **Search Functionality**: Real-time search across event titles
- **Combined Filters**: Tab selection + search term filtering

### Event Display

#### Event Cards
Each registration displays:
- **Event Image**: Background gradient with optional event image overlay
- **Registration Status**: Green "Registered" badge with checkmark icon
- **Event Title**: Truncated title with full text on hover
- **Event Details**:
  - Date (full weekday format)
  - Time (12-hour format)
  - Venue (for offline events)
  - Registration date
- **Event Type**: Free/Paid indicator with color coding
- **Action Buttons**: QR Code and Calendar integration

#### Responsive Grid
- **Mobile**: Single column layout
- **Tablet**: 2-column grid
- **Desktop**: 3-column grid

### QR Code Management

#### QR Code Generation
- **Dynamic Generation**: QR codes generated per registration
- **Unique Codes**: Each registration has its own QR code
- **Base64 Encoding**: QR codes stored as base64 images

#### QR Modal Features
- **Full-Screen Modal**: Gradient header with event branding
- **QR Display**: Large, centered QR code with white background
- **Usage Instructions**: Step-by-step scanning guide
- **Download Functionality**: PNG export with descriptive filename
- **Local Storage**: QR codes cached in browser storage

### Calendar Integration

#### Google Calendar Integration
- **One-Click Addition**: Direct integration with Google Calendar
- **Automatic Formatting**: Proper date/time formatting for calendar events
- **Event Details**: Includes title, description, and location
- **Duration Estimation**: Assumes 2-hour default duration

### Search and Navigation

#### Real-Time Search
- **Live Filtering**: Instant results as user types
- **Case-Insensitive**: Searches work regardless of case
- **Title-Based**: Searches through event titles only

#### Navigation Controls
- **Back Button**: Return to dashboard/home page
- **Tab Switching**: Smooth transitions between event categories
- **Date Filtering**: Future enhancement for date range filtering

## Technical Implementation

### Component Structure

```
MyRegistrationsPage.jsx
├── Header Section
│   ├── Navigation Bar
│   ├── Search Input
│   └── User Profile
├── Main Content
│   ├── Back Navigation
│   ├── Page Title
│   ├── Tab Navigation
│   ├── Filter Controls
│   └── Events Grid
│       ├── Event Cards
│       │   ├── Image Header
│       │   ├── Event Details
│       │   └── Action Buttons
│       └── Empty States
└── QR Code Modal
    ├── Modal Header
    ├── QR Display
    ├── Instructions
    └── Action Buttons
```

### Key Features

#### State Management
```javascript
const [activeTab, setActiveTab] = useState('going');
const [registrations, setRegistrations] = useState([]);
const [searchTerm, setSearchTerm] = useState('');
const [qrModal, setQrModal] = useState({ show: false, qr: '', title: '', eventId: '' });
```

#### Smart Filtering Logic
```javascript
const getFilteredRegistrations = () => {
  const now = new Date();
  return registrations.filter(event => {
    // Tab filtering
    const eventDate = new Date(event.start_time);
    let tabMatch = false;
    if (activeTab === 'going') tabMatch = eventDate > now;
    else if (activeTab === 'past') tabMatch = eventDate < now;
    else tabMatch = true; // saved tab

    // Search filtering
    const searchMatch = searchTerm === '' ||
      event.title.toLowerCase().includes(searchTerm.toLowerCase());

    return tabMatch && searchMatch;
  });
};
```

#### QR Code Handling
```javascript
const handleShowQr = async (eventId) => {
  const res = await fetch(`/api/v1/user/registrations/${eventId}/qr`);
  const data = await res.json();
  setQrModal({ show: true, qr: data.qr_code, title: data.event_title, eventId });
};
```

### API Integration

#### Endpoints Used
- `GET /api/v1/user/registrations` - Fetches all user registrations
- `GET /api/v1/user/registrations/{eventId}/qr` - Generates QR codes

#### Data Structure
```javascript
// Registration object structure
{
  id: "event_id",
  title: "Event Title",
  start_time: "2024-01-20T10:00:00Z",
  venue_name: "Venue Name",
  online_event: false,
  is_free: true,
  image_url: "image_url",
  registration_date: "2024-01-15T08:00:00Z"
}
```

### Responsive Design

#### Breakpoint Strategy
- **Mobile (< 768px)**: Single column, stacked layout
- **Tablet (768px - 1024px)**: 2-column grid
- **Desktop (> 1024px)**: 3-column grid, full header

#### Component Adaptations
- **Search Bar**: Hidden on mobile, visible on desktop
- **Event Cards**: Flexible sizing with consistent aspect ratios
- **Modal**: Centered with responsive padding

## Usage Guidelines

### For Users

#### Viewing Registrations
1. Navigate to "My Registrations" from the sidebar
2. Use tabs to filter between Going, Saved, and Past events
3. Search for specific events using the search bar
4. Click on QR Code to view/download tickets
5. Use "Add to Calendar" for Google Calendar integration

#### Managing Events
1. **QR Codes**: Scan for event check-in or share tickets
2. **Calendar**: Add events to personal calendar
3. **Status Tracking**: Monitor registration confirmations
4. **History**: Review past attended events

### For Developers

#### Adding New Filters
```javascript
const getFilteredRegistrations = () => {
  return registrations.filter(event => {
    // Add new filter conditions
    const customFilter = event.customField === selectedValue;
    return tabMatch && searchMatch && customFilter;
  });
};
```

#### Extending Event Cards
```javascript
<div className="event-card">
  {/* Existing content */}
  <div className="new-feature">
    {/* Add new event information */}
  </div>
</div>
```

#### Custom QR Actions
```javascript
const customQrAction = async (eventId) => {
  // Implement custom QR functionality
  const response = await fetch(`/api/custom-qr/${eventId}`);
  // Handle response
};
```

## Accessibility Features

- **Keyboard Navigation**: Tab order through all interactive elements
- **Screen Reader Support**: Proper ARIA labels and semantic HTML
- **Color Contrast**: High contrast for status indicators and text
- **Focus Management**: Clear focus indicators on buttons and inputs
- **Alt Text**: Descriptive alt text for all images

## Browser Compatibility

- **QR Code Display**: Base64 image support in all modern browsers
- **Calendar Integration**: Google Calendar URL scheme support
- **Download Functionality**: HTML5 download attribute support
- **Local Storage**: Modern browser storage APIs

## Security Considerations

- **Token Authentication**: Bearer token for all API requests
- **Data Sanitization**: Input validation for search terms
- **Secure Storage**: QR codes stored securely in localStorage
- **API Rate Limiting**: Proper error handling for API failures

## Performance Optimization

- **Lazy Loading**: Event cards render only when visible
- **Efficient Filtering**: Client-side filtering with minimal re-renders
- **Image Optimization**: Conditional image loading
- **State Management**: Minimal state updates to prevent unnecessary renders

## Error Handling

### API Error States
- **Loading State**: Spinner with descriptive text
- **Error State**: User-friendly error messages with retry options
- **Empty State**: Contextual messages based on active tab

### User Feedback
- **Success Messages**: Confirmation for successful actions
- **Error Alerts**: Clear error messages for failed operations
- **Loading Indicators**: Visual feedback during async operations

## Future Enhancements

- **Advanced Filtering**: Date range, location, and category filters
- **Bulk Actions**: Select multiple events for batch operations
- **Export Functionality**: Export registration data to CSV/PDF
- **Reminder System**: Automatic notifications before events
- **Social Sharing**: Share event registrations on social media
- **Rating System**: Rate and review attended events
- **Waitlist Management**: Handle waitlisted registrations
- **Group Registrations**: Manage group/family registrations
- **Integration APIs**: Third-party calendar integrations (Outlook, Apple Calendar)
- **Offline Support**: View registrations without internet connection

# Notifications Page and Following Feature

## Overview

The Notifications Page provides users with a comprehensive view of their activities, including event registrations, created events, and follower interactions. The page features a clean, full-screen design with hidden scrollbars for optimal user experience.

## Features

### Notifications Page

#### Access
- Click the bell icon in the dashboard header to open the notifications dropdown
- Click "Show More" in the dropdown to navigate to the full notifications page
- The notifications page displays as a separate, full-screen page without affecting other navigation

#### Design
- **Full Screen Layout**: The page uses the entire viewport without padding or gaps
- **Hidden Scrollbars**: Custom CSS hides scrollbars while maintaining scrolling functionality
- **Clean UI**: Dark theme with slate colors matching the application design

#### Content Display
The notifications page shows the following activity types:

1. **Event Created** (✅)
   - Shows when a user creates a new event
   - Displays event title and creation details

2. **Event Registered** (✅)
   - Shows successful event registrations
   - Includes QR code access for ticket viewing

3. **New Follower** (🔔)
   - Displays when someone starts following the user
   - Shows follower name, email, and profile information

4. **Event Deleted** (⚠️)
   - Shows when an event is deleted
   - Includes deletion details

#### Activity Details
Each notification includes:
- **Icon**: Visual indicator based on activity type
- **Title**: Main activity description
- **Subtitle**: Additional context (venue, follower info, etc.)
- **Time**: Relative timestamp (e.g., "2h ago", "1d ago")
- **Action Button**: Context-specific actions (View Event, View Profile, View Ticket)

### Following Button

#### Location
- Available on event detail pages and user profile views
- Prominent placement for easy access

#### Functionality
- **Follow/Unfollow Toggle**: Single button that switches between follow and unfollow states
- **Real-time Updates**: Immediately reflects follow status changes
- **Visual Feedback**: Clear icons and text indicating current state

#### States
- **Follow**: Shows plus icon (+) with "Follow" text
- **Following**: Shows checkmark icon (✓) with "Following" text
- **Loading**: Shows spinner during API calls

## Technical Implementation

### Components Structure

```
NotificationsPage.jsx
├── Main Container (full-screen, hidden scrollbars)
├── Header Section
│   ├── Page Title
│   └── Search Input
├── Notifications List
│   ├── Individual Notification Cards
│   │   ├── Icon/Image
│   │   ├── Content (title, subtitle, time)
│   │   └── Action Button
│   └── Modals (Follower Profile, QR Code, Event Details)
└── Navigation Integration
```

### Key Features

#### Scrollbar Hiding
```css
.no-scroll::-webkit-scrollbar {
  display: none;
}
.no-scroll {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
```

#### Full Screen Layout
- Uses `min-h-screen` and `max-h-screen` for viewport coverage
- Removes default padding for edge-to-edge display
- Maintains responsive design across devices

#### Modal Integration
- **Follower Profile Modal**: Shows detailed follower information
- **QR Code Modal**: Displays event tickets with confirmation IDs
- **Event Details Modal**: Provides comprehensive event information

### API Integration

#### Endpoints Used
- `GET /api/v1/user/activities` - Fetches user notifications
- `GET /api/v1/user/registrations/{eventId}/qr` - Gets QR codes
- `GET /api/v1/events/{eventId}` - Fetches event details

#### Data Flow
1. Page loads → Fetch user activities
2. User clicks notification → Open relevant modal
3. Modal fetches additional data as needed
4. Real-time updates for follow/unfollow actions

## Usage Guidelines

### For Users
1. **Accessing Notifications**: Click the bell icon in the top navigation
2. **Viewing Details**: Click "Show More" for full notification list
3. **Taking Actions**: Use action buttons on notifications (View Event, View Profile, etc.)
4. **Following Users**: Click follow button on profiles to follow/unfollow users

### For Developers
1. **Adding New Notification Types**: Extend the `getNotificationType` and `getNotificationAction` functions
2. **Customizing UI**: Modify the notification card structure in the map function
3. **Adding Modals**: Follow the existing modal pattern for new interaction types

## Accessibility

- **Keyboard Navigation**: Full keyboard support for all interactive elements
- **Screen Reader Support**: Proper ARIA labels and semantic HTML
- **Color Contrast**: High contrast ratios for readability
- **Focus Management**: Proper focus indicators and management

## Browser Compatibility

- **Chrome/Edge**: Full scrollbar hiding support
- **Firefox**: Scrollbar hiding via `scrollbar-width`
- **Safari**: WebKit scrollbar hiding
- **Mobile**: Touch-friendly interactions and responsive design

## Future Enhancements

- Real-time notifications via WebSocket
- Notification filtering and search
- Bulk notification actions
- Push notification integration
- Notification preferences and settings
