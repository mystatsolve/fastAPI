from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/concat_words")
async def concat_words(request: Request, word1: str = Form(...), word2: str = Form(...)):
    concatenated_words = word1 + word2
    return templates.TemplateResponse("index.html", {"request": request, "result": concatenated_words})
