# Support CRM System

A full-stack customer support ticketing system built with FastAPI + SQLite + HTML/Tailwind.

## Features
- Create support tickets with customer info
- List and search all tickets
- Filter by status (Open / In Progress / Closed)
- View ticket details and add internal notes
- Update ticket status

## Tech Stack
- Backend: Python + FastAPI
- Database: SQLite (via SQLAlchemy)
- Frontend: HTML + Tailwind CSS
- Deploy: Railway.app

## Setup Instructions

1. Clone the repository
   git clone https://github.com/YOUR_USERNAME/support-crm.git
   cd support-crm

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the application
   uvicorn main:app --reload

5. Open browser
   Visit http://127.0.0.1:8000

## API Endpoints

- POST   /api/tickets              - Create a new ticket
- GET    /api/tickets              - List all tickets (supports ?search= and ?status=)
- GET    /api/tickets/{ticket_id}  - Get ticket details
- PUT    /api/tickets/{ticket_id}  - Update status or add note

## Project Structure

support-crm/
├── main.py          - FastAPI app entry point
├── database.py      - Database connection setup
├── models.py        - SQLAlchemy table models
├── schemas.py       - Pydantic request/response schemas
├── routers/
│   └── tickets.py   - All ticket API routes
├── templates/
│   ├── index.html   - Home page (ticket list)
│   ├── create.html  - Create ticket form
│   └── detail.html  - Ticket detail & update page
├── static/          - Static assets
├── requirements.txt
└── .env.example