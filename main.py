from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import os
from openai import OpenAI


app = FastAPI()
client = OpenAI()

# Get the OpenAI API key from environment variables
# openai.api_key = os.getenv("OPENAI_API_KEY")

class AskQuestionModel(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"Hello": "Please upload your file"}

@app.post("/uploadfile/")
async def uploadfile(file: UploadFile):
    folder = "documents"
    current_directory = os.getcwd()
    print(current_directory)
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_path = os.path.join(current_directory, folder, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
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