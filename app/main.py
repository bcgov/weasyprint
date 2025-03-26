from fastapi import FastAPI, Response
from pydantic import BaseModel
from weasyprint import HTML, CSS
from styles import default_css, font_config
import logging
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "default": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
    },
    "loggers": {
        "uvicorn.error": {
            "level": "DEBUG",
            "handlers": ["default"],
        },
        "uvicorn.access": {
            "level": "DEBUG",
            "handlers": ["default"],
        },
    },
}

logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def home():
    logger.info(f"request / endpoint!")
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
