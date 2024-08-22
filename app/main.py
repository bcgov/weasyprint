from fastapi import FastAPI, Response
from pydantic import BaseModel
from weasyprint import HTML, CSS
from styles import default_css, font_config

app = FastAPI()


@app.get("/")
def home():
    return {"status": True}


class PdfBody(BaseModel):
    html: str
    css: str = ""
    filename: str = "download.pdf"


@app.post("/pdf")
def generate_pdf(body: PdfBody):
    html = HTML(string=body.html)
    css = CSS(string=body.css, font_config=font_config)

    # See https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#weasyprint.HTML.write_pdf
    pdf = html.write_pdf(stylesheets=[default_css, css], font_config=font_config)
    headers = {"Content-Disposition": "attachment; filename='{}'".format(body.filename)}
    return Response(pdf, headers=headers, media_type="application/pdf")
