import csv
import os

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from llm_client import ask_llm
from logger import logger
from auth import verify_api_key

app = FastAPI(title="University Student Support Assistant")


class Question(BaseModel):
    question: str


class Feedback(BaseModel):
    question: str
    answer: str
    rating: str


@app.get("/health")
def health():
    return {"status": "running"}


@app.post("/ask")
def ask(
    data: Question,
    api_key: str = Depends(verify_api_key)
):

    if not data.question.strip():
        logger.warning("Empty question received")
        return {"error": "Question cannot be empty"}

    try:

        logger.info(f"Question: {data.question}")

        answer = ask_llm(data.question)

        logger.info(f"Answer: {answer}")

        return {"answer": answer}

    except Exception as e:

        logger.exception(str(e))

        return {
            "error": "Model not available or backend error"
        }


@app.post("/feedback")
def save_feedback(
    data: Feedback,
    api_key: str = Depends(verify_api_key)
):

    feedback_dir = "feedback"
    os.makedirs(feedback_dir, exist_ok=True)

    file = os.path.join(feedback_dir, "feedback.csv")

    file_exists = os.path.isfile(file)

    with open(file, "a", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "Question",
                "Answer",
                "Rating"
            ])

        writer.writerow([
            data.question,
            data.answer,
            data.rating
        ])

    logger.info(
        f"Feedback received: {data.rating}"
    )

    return {
        "message": "Feedback saved successfully"
    }