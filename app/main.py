from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

app = FastAPI()
class Url(BaseModel):
    url_string:str

url_dict={}

@app.post("/shorten")
def shorten_url(url:Url):
    base = url.url_string
    short :str = url.url_string[:6]
    comp_url =  ""
    for i in short:

        comp_url+=(chr(ord(i)+7))
    url_dict[comp_url]=base

    return {"compressed url": comp_url}

@app.get("/{comp_url}")
def redirect_url(comp_url):
    if comp_url not in url_dict:
        raise HTTPException(status_code=404,detail="url not found")
    else:
        return RedirectResponse(url=f"{url_dict[comp_url]}",status_code=302)
    
