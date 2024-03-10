import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
task = []

def test_create_task():
    new_task_data ={
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/task", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    task.append(response_json['id'])

def test_get_task():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_single_task():
    if task:
        task_id = task[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']

def test_update_task():
    if task:
        task_id = task[0]
        payload = {
            "completed": True,
            "description": "Nova descrição",
            "title": "Titulo atualizado"
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["message"] == "Task updated successfully"