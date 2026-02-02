from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 1. Static files (CSS/JS/Images) ko mount karein
app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. Templates folder ka path batayein
templates = Jinja2Templates(directory="templates")

# 3. Custom context processor for static files - REMOVE THIS, it's causing issues
# @app.middleware("http")
# async def add_static_context(request: Request, call_next):
#     request.state.static = "/static"
#     response = await call_next(request)
#     return response

# Home page route
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# About page route
@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# Rooms page route
@app.get("/rooms", response_class=HTMLResponse)
async def room(request: Request):
    return templates.TemplateResponse("room.html", {"request": request})

# Amenities page route
@app.get("/amenities", response_class=HTMLResponse)
async def amenities(request: Request):
    return templates.TemplateResponse("amenities.html", {"request": request})

# Booking page route
@app.get("/booking", response_class=HTMLResponse)
async def booking(request: Request):
    return templates.TemplateResponse("booking.html", {"request": request})

# Contact page route
@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

# Login page route
@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# News website home page route - Use index copy.html for news home
@app.get("/news", response_class=HTMLResponse)
async def news_home(request: Request):
    return templates.TemplateResponse("index copy.html", {"request": request})

# News contact page route - Use contact.html for news contact
@app.get("/news/contact", response_class=HTMLResponse)
async def news_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})