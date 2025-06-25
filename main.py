from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from parser.cv_reader import parse_cv
from parser.cv_analyzer import analyze_cv
from parser.job_scraper import search_jobs
from parser.excel_exporter import create_excel_with_links

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload_cv/", response_class=HTMLResponse)
async def upload_cv(request: Request, file: UploadFile = File(...)):
    contents = await file.read()

    try:
        text = parse_cv(contents, file.filename)
        analysis = analyze_cv(text)
        location = analysis.get("location", "Istanbul")
        keywords = analysis.get("keywords", [])

        print("🔍 Anahtar kelimeler:", keywords)
        print("📍 Konum:", location)

        jobs = search_jobs(keywords, location)

        return templates.TemplateResponse(
            "results.html",
            {
                "request": request,
                "job_matches": jobs,
                "filename": file.filename
            }
        )

    except Exception as e:
        return HTMLResponse(content=f"<h3>❌ Hata: {str(e)}</h3>", status_code=500)

@app.post("/download_excel/")
async def download_excel(file: UploadFile = File(...)):
    contents = await file.read()

    try:
        text = parse_cv(contents, file.filename)
        analysis = analyze_cv(text)
        location = analysis.get("location", "Istanbul")
        keywords = analysis.get("keywords", [])
        jobs = search_jobs(keywords, location)
        excel_file = create_excel_with_links(jobs)

        return StreamingResponse(
            excel_file,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": "attachment; filename=job_links.xlsx"}
        )

    except Exception as e:
        return {"error": str(e)}
