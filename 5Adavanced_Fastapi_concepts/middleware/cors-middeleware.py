from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    # Frontend URLs allowed to access backend
    allow_origins=["https://my-frontend.com", "http://localhost:3000"],
    # Allow cookies/auth headers
    allow_credentials=True,
    # Allowed HTTP methods
    allow_methods=["GET", "POST"],
    # Allowed headers
    allow_headers=["*"],
)


# -----------------------------
# Sample Endpoints
# -----------------------------


# GET API
@app.get("/")
def home():
    return {"message": "FastAPI CORS Example Working"}


# GET API
@app.get("/students")
def get_students():

    students = [
        {"id": 1, "name": "Harsha"},
        {"id": 2, "name": "Rahul"},
    ]

    return students


# POST API
@app.post("/students")
def create_student(student: dict):

    return {"message": "Student Created Successfully", "student": student}


# PUT API
@app.put("/students/{student_id}")
def update_student(student_id: int, student: dict):

    return {
        "message": "Student Updated",
        "student_id": student_id,
        "updated_data": student,
    }


# DELETE API
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    return {"message": "Student Deleted", "student_id": student_id}
