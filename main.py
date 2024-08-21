from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import os
from openai import OpenAI
import shutil


app = FastAPI()
client = OpenAI()

# Get the OpenAI API key from environment variables
# openai.api_key = os.getenv("OPENAI_API_KEY")

class AskQuestionModel(BaseModel):
    question: str

@app.get("/")
def root():
    return "Hello RAG fellow!"

@app.post("/uploadfile/")
async def uploadfile(file: UploadFile = File(...)):
    # Define allowed file extensions
    allowed_extensions = ["txt", "pdf"]

    # Check if the file extension is allowed
    file_extension = file.filename.split(".")[-1].lower()

    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400, detail="File type not allowed. Only TXT and PDF files are accepted.")
    
    folder = "documents"
    current_directory = os.getcwd()
    print(current_directory)

    try:
        # Ensure the directory exists
        if not os.path.exists(folder):
            os.makedirs(folder)

        file_path = os.path.join(current_directory, folder, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return {"info": "File saved", "filename": file.filename}
    except Exception as e:
        return {"message": e.args}
        

@app.post("/ask/")
async def ask_question(data: AskQuestionModel):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": data.question
                }
            ]
        )
        answer = completion.choices[0].message.content
        return {"answer": answer}
    except Exception as e:
        return {"message": e.args}