import form
from fastapi import FastAPI, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.params import Form, File

app = FastAPI()

templates = Jinja2Templates(directory="htmldirectory")

@app.get("/enterform", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})

@app.post("/submitform", response_class=HTMLResponse)
async def form_post(request: Request, FirstName : str = Form(...), uploadfile : UploadFile = File(...)):
    print(FirstName)
    content_assignment = await uploadfile.read()
    print(content_assignment)
    return templates.TemplateResponse('form.html', context={'request': request})

