from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import sqlite3
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

db_file = 'health_dashboard.db'

# Database setup
if not os.path.exists(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        medical_history TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE SymptomCheck (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        symptoms TEXT,
        diagnosis TEXT,
        FOREIGN KEY(user_id) REFERENCES User(id)
    )
    ''')
    cursor.execute('''
    CREATE TABLE Insight (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        data TEXT,
        recommendations TEXT,
        FOREIGN KEY(user_id) REFERENCES User(id)
    )
    ''')
    # Seed data
    cursor.execute("INSERT INTO User (name, age, gender, medical_history) VALUES ('John Doe', 30, 'Male', '[]')")
    conn.commit()
    conn.close()

# Models
class User(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    medical_history: List[str]

class SymptomCheck(BaseModel):
    id: int
    user_id: int
    symptoms: List[str]
    diagnosis: str

class Insight(BaseModel):
    id: int
    user_id: int
    data: str
    recommendations: str

# Routes
@app.get('/', response_class=HTMLResponse)
async def home():
    return open('templates/index.html').read()

@app.get('/diagnosis', response_class=HTMLResponse)
async def diagnosis_page():
    return open('templates/diagnosis.html').read()

@app.get('/profile', response_class=HTMLResponse)
async def profile_page():
    return open('templates/profile.html').read()

@app.get('/insights', response_class=HTMLResponse)
async def insights_page():
    return open('templates/insights.html').read()

@app.get('/about', response_class=HTMLResponse)
async def about_page():
    return open('templates/about.html').read()

@app.post('/api/diagnose')
async def diagnose(symptoms: List[str]):
    # Mock diagnosis logic
    if 'fever' in symptoms:
        return {'diagnosis': 'Common Cold'}
    return {'diagnosis': 'Unknown'}

@app.get('/api/user/{user_id}')
async def get_user(user_id: int):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM User WHERE id=?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return {
            'id': user[0],
            'name': user[1],
            'age': user[2],
            'gender': user[3],
            'medical_history': eval(user[4])
        }
    raise HTTPException(status_code=404, detail='User not found')

@app.put('/api/user/{user_id}')
async def update_user(user_id: int, user: User):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE User SET name=?, age=?, gender=?, medical_history=? WHERE id=?
    ''', (user.name, user.age, user.gender, str(user.medical_history), user_id))
    conn.commit()
    conn.close()
    return {'message': 'User updated successfully'}

@app.get('/api/insights')
async def get_insights():
    # Mock insights logic
    return {'data': 'Sample insights data', 'recommendations': 'Sample recommendations'}
