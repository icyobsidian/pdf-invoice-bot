from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "pdf-invoice-bot backend is alive"}

@app.post("/parse-invoice")
async def parse_invoice(file: UploadFile = File(...)):
    # Пока просто возвращаем имя файла и тип
    return JSONResponse(content={
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Здесь будет парсинг PDF!"
    })
