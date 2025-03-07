from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get('/')
def read_root():
    return {"message":"Task manager API"}

@app.post('/tasks')
def create_task(task: str):
    tasks.append(task)
    return {'message': 'task added', 'tasks':tasks}

@app.get('/tasks')
def get_tasks():
    return {'tasks': tasks}
