from fastapi import FastAPI, UploadFile
import os
import openai

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

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
async def ask_question(question: str):
    try:
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=question,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        return {"answer": answer}
    except Exception as e:
        return {"message": e.args}