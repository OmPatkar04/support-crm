from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, PlainTextResponse
import traceback
import models
from database import engine
from routers import tickets

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Support CRM")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(tickets.router)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    try:
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        return PlainTextResponse(traceback.format_exc(), status_code=500)

@app.get("/create", response_class=HTMLResponse)
def create_page(request: Request):
    try:
        return templates.TemplateResponse("create.html", {"request": request})
    except Exception as e:
        return PlainTextResponse(traceback.format_exc(), status_code=500)

@app.get("/ticket/{ticket_id}", response_class=HTMLResponse)
def detail_page(request: Request, ticket_id: str):
    try:
        return templates.TemplateResponse("detail.html", {"request": request, "ticket_id": ticket_id})
    except Exception as e:
        return PlainTextResponse(traceback.format_exc(), status_code=500)