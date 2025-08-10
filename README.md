# FastAPI Todo API

A simple Todo REST API built with FastAPI in Python, designed for learning and demonstration purposes. Includes comprehensive tests to ensure functionality.

---

## Features

- Create, read, update, and delete Todo items
- Auto-incrementing IDs for tasks
- Validation with Pydantic models
- Comprehensive test coverage using pytest
- FastAPI's automatic interactive API docs

---

## Requirements

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)
- pytest (for running tests)

---

## Setup & Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/janoskocs/python-fastapi.git
   cd python-fastapi
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the API server:

   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser and visit:

   ```
   http://127.0.0.1:8000/docs
   ```

   to explore the interactive API documentation.

---

## Running Tests

Ensure your virtual environment is activated, then run:

```bash
pytest
```

All tests are located in `test_main.py` and cover every endpoint.

---

## API Endpoints

| Method | Path          | Description             |
| ------ | ------------- | ----------------------- |
| GET    | `/`           | Welcome message         |
| GET    | `/todos`      | Retrieve all ToDos      |
| POST   | `/todos`      | Create a new Todo       |
| PUT    | `/todos/{id}` | Update an existing Todo |
| DELETE | `/todos/{id}` | Delete a Todo           |

---

## Notes

- Data is stored in-memory for simplicity; the API will reset on server restart.
- IDs are automatically assigned and incremented.
- Proper HTTP status codes are used (`201 Created` on POST).

---

## Contributions

Contributions and improvements are very welcome! Feel free to fork the repository and open a pull request.

---
