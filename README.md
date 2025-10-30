# goit-pycore-hw-05

Small collection of Python exercises (closures, generators, CLI log analyzer) and a simple console bot with error-handling decorators. Designed to practice core Python concepts and writing tests.

Repository layout

- `src/` - source code for tasks and bot
  - `src/tasks/task1.py` - `caching_fibonacci()` returns a closure that calculates Fibonacci numbers using recursion and internal cache
  - `src/tasks/task2.py` - `generator_numbers(text)` extracts numeric income values from text
  - `src/logs_analizator/analizator.py` - helpers for printing directory tree from a CLI argument.
  - `src/logs_analizator/main_script.py` - CLI entry point for log analysis (using command-line arguments)
  - `src/bot/contact_handler.py` - in-memory contacts manager with commands add/change/phone/all and input validation via @input_error decorator
  - 
- `tests/` - pytest test files and sample data used by tests
  - `test_task1.py` — tests for caching Fibonacci functionality
  - `test_task2.py` - task2 test fixtures
  - `tests/bot/` - tests for the bot/contact handler


## Installation & Usage
See [INSTALL.md](INSTALL.md) for detailed setup instructions, including environment creation, dependency installation, running the main script, and executing tests.
