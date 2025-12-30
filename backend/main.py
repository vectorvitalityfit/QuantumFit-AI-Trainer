from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app=FastAPI()

# Data models
class User(BaseModel):
    id: int
    name: str
    email: str

class Feedback(BaseModel):
    session_id: int
    message: str
    timestamp: Optional[str]

class Session(BaseModel):
    id: int
    user_id: int
    active: bool

class Workout(BaseModel):
    id: int
    user_id: int
    exercises: List[str]

# In-memory "database"
users=[]
sessions=[]
feedbacks=[]
workouts=[]

# User Endpoints
@app.post("/users/")
def create_user(user_id: int):
    for user in users:
        if user.id==user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Session Endpoints
@app.post("/sessions/")
def start_session(session: Session):
    sessions.append(session)
    return session

@app.patch("/sessions/{session_id}/end")
def end_session(session_id: int):
    for session in sessions:
        if session.id==session_id:
            session.active=False
            return session
    raise HTTPException(status_code=404, detail="Session not found")

# Feedback endpoints
@app.post("/feedback/")
def add_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return feedback

@app.get("/feedback/{session_id}")
def get_feedback(session_id: int):
    session_feedbacks=[f for f in feedbacks if f.session_id==session_id]
    return session_feedbacks

# Workout Endpoints
@app.post("/workouts/{user_id}")
def get_workouts(user_id: int):
    user_workouts=[w for w in workouts if w.user_id==user_id]
    return user_workouts

