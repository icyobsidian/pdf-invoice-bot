from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from model.parser import parse_invoice_pdf

app = FastAPI()

@app.post("/parse-invoice")
async def parse_invoice(file: UploadFile = File(...)):
    file_bytes = await file.read()
    parsed = parse_invoice_pdf(file_bytes)
    return JSONResponse(content=parsed)
