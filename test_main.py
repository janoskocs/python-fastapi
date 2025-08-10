from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my todo app"}

def test_create_and_get_todo():
    todo_data = {"id": 0, "title": "Test todo", "completed": False}
    response = client.post("/todos", json=todo_data)
    assert response.status_code == 201
    todo = response.json()
    assert todo["title"] == "Test todo"
    assert todo["completed"] == False

def test_update_todo():
    todo_data = {"id": 0, "title": "Test todo", "completed": False}
    create_response = client.post("/todos", json=todo_data)
    todo = create_response.json()
    todo_id = todo["id"]

    updated_data = {"id": 0, "title": "Test todo updated", "completed": True}
    updated_response = client.put(f"/todos/{todo_id}", json=updated_data)
    assert updated_response.status_code == 200
    updated_todo = updated_response.json()
    assert updated_todo["title"] == "Test todo updated"
    assert updated_todo["completed"] == True

def test_delete_todo():
    todo_data = {"id": 0, "title": "Test todo", "completed": False}
    create_response = client.post("/todos", json=todo_data)
    todo_id = create_response.json()["id"]

    delete_response = client.delete(f"/todos/{todo_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"detail": "Todo deleted."}