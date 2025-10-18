from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse
import shutil

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body style="background-color:#001F3F;color:gold;font-family:sans-serif;text-align:center;padding-top:100px;">
            <h1>Welcome Back Brian Kamau 💎</h1>
            <h2>Kamau AI Vault</h2>
            <form action="/upload" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <button type="submit">Upload File</button>
            </form>
        </body>
    </html>
    """

@app.post("/upload")
async def upload(file: UploadFile):
    with open(f"uploaded_{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": f"File '{file.filename}' uploaded successfully!"}
