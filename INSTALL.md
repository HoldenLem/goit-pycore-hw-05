# Installation Instructions

Follow these steps to set up and run the project:

## 1. Prerequisites
- Python 3.12 or newer
- pip (Python package manager)

## 2. Clone the Repository
Clone the project to your local machine:
```bash
git clone <repository-url>
cd goit-pycore-hw-05
```

## 3. Create a Virtual Environment (Recommended)
```bash
source .venv/bin/activate
```

## 4. Install Dependencies
Install required packages from requirements.txt:
```bash
pip install -r requirements.txt
```

## 5. Run the Main Script for 1-2tasks
To execute the main program:
```bash
 python -m src.tssk.main
```

## 5. Run the Main Script for BOT
To execute the main program:
```bash
 python -m src.bot.main
```

## 5. Run the Main Script for analyze log file
To execute the main program:
```bash
 python -m src.logs_analizator.main_script ./logs.txt info
```

## 7. Run Tests
To run all tests using pytest:
```bash
pytest -q
```
Or to run a specific test file:
```bash
pytest tests/test_task1.py
```

## 8. Deactivate the Virtual Environment
When finished, deactivate with:
```bash
deactivate
```

---
For any issues, please check your Python version and ensure all dependencies are installed. If you need further help, consult the project README or contact the author.
