from fastapi import FastAPI
from backend import workflow
from datetime import datetime
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development; can be tightened later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Blog_Requirements(BaseModel):
    topic : str

@app.post('/create-blog')
def create_blog(body : Blog_Requirements):
    response = workflow.invoke({
        'topic' : body.topic,
        'as_of' : datetime.now().strftime("%m/%d/%Y")
    })

    return {'response': response}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=4000)