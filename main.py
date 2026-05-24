from fastapi import FastAPI, UploadFile, File   
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from orchestrator1 import run_agent
from document_parser import parse_uploaded_file
from question_extractor import extract_questions
from question_manager import sort_questions_by_difficulty

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

session_data = {

    "questions": [],

    "current_question": 0,

    "hint_level": 1,

    "manual_question": "",

    "current_pattern": ""
}


class ChatRequest(BaseModel):

    message: str


@app.get("/")
def home():

    return {
        "message": "Raiz Backend Running"
    }


@app.post("/chat")
def chat(req: ChatRequest):

    response = run_agent(
        req.message,
        session_data
    )

    return {
        "response": response
    }


@app.post("/upload")
async def upload(
    file: UploadFile = File(...)
):

    content = await file.read()

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as f:

        f.write(content)

    class TempFile:

        def __init__(
            self,
            path,
            filename,
            content_type
        ):

            self.path = path
            self.name = filename
            self.type = content_type

        def read(self):

            with open(self.path, "rb") as f:

                return f.read()

    temp_file = TempFile(
        temp_path,
        file.filename,
        file.content_type
    )

    parsed = parse_uploaded_file(
        temp_file
    )

    questions = extract_questions(
        parsed
    )

    questions = sort_questions_by_difficulty(
        questions
    )

    session_data["questions"] = questions

    session_data["current_question"] = 0

    session_data["hint_level"] = 1

    return {

        "count": len(questions),

        "questions": questions
    }