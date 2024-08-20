from fastapi import FastAPI, UploadFile
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Please upload your file"}

@app.post("/uploadfile/")
async def uploadfile(file: UploadFile):
    folder = "documents"
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_path = f"/usercode/documents/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
            return {"info": "File saved", "filename": file.filename}
    except Exception as e:
        return {"message": e.args}
    