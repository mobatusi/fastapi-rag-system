# fastapi-rag-system
This repository contains a complete implementation of a Retrieval-Augmented Generation (RAG) system using FastAPI and OpenAI’s API. The project provides a practical example of how to build and integrate a sophisticated AI-driven system that combines retrieval and generation techniques.

# Key Technologies:

•	**FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

•	**OpenAI**: A powerful AI model API for natural language processing, enabling advanced text generation and comprehension capabilities.

•	**PostgreSQL**: An open-source relational database system used for storing and managing application data.

## Directory Structure

### Files

- **main.py**: The entry point of the FastAPI application. It contains the API endpoints and the main logic for handling requests and responses.

- **db.py**: Contains the database configuration and setup using SQLAlchemy. It includes the database engine, session, and base model.

- **file_parser.py**: Implements a PDF document parser, and also handles PDFs containing images using optical character recognition (OCR).

- **file_parser_tests.py**: Test the implementation of PDF parser in file_parser.py.

- **background_tasks.py**: Used to run background tasks for chunking text into sentences, generating embeddings, and storing these in the database.

- **requirements.txt**: Lists all the dependencies required for the project. These can be installed using `pip install -r requirements.txt`.

- **.env**: Environment variables file that contains sensitive information such as database credentials. This file should not be committed to version control.

- **api_test.sh**: A script to test the API endpoints. It sequentially:
	- Uploads a test file to populate the database.
	- Queries the root endpoint to list available files.
  	- Waits 30 seconds to allow background tasks to process the uploaded file.
  	- Tests the `/ask/` endpoint by submitting a question related to the content of the uploaded file.
  	- Tests the `/find-similar-chunks/{file_id}` endpoint to retrieve chunks similar to a provided question.

# Getting Started
1.	Clone the Repository
``` 
git clone https://github.com/mobatusi/fastapi-rag-system.git
cd fastapi-rag-system 
```
2.	Install Dependencies
```
pip install -r requirements.txt
```
3.	Set Up Environment Variables
	•	Create a .env file and add your OpenAI API key and database configuration.
4.	Run the Application
```
uvicorn main:app --reload
```
5.	Access the API
	•	Open your browser and navigate to http://localhost:8000/docs to view the interactive API documentation.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments
•	Special thanks to the FastAPI and OpenAI communities for their outstanding tools and resources.
•	This project is based on the educative course Building a [Retrieval-Augmented Generation System Using FastAPI](https://www.educative.io/projects/building-a-retrieval-augmented-generation-system-using-fastapi), which provided valuable guidance and inspiration.