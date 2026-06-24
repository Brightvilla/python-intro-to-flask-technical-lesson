# Lab Process: Introduction to Flask

## Environment Setup

### Problem: `pipenv` broken with Python 3.13
The Pipfile was locked to Python 3.8.13, but the system had Python 3.13 installed. The `pipenv` vendored pip was incompatible with Python 3.13, causing:
```
AttributeError: module 'functools' has no attribute 'cache'
```

**Fix:** Installed dependencies directly via `pip3 install` (Flask 2.2.3, Werkzeug 2.2.3, importlib-metadata, importlib-resources) using the existing pipenv virtualenv that already had Flask.

```bash
pip3 install flask==2.2.3 werkzeug==2.2.3 importlib-metadata==6.0.0 importlib-resources==5.12.0
```

---

## Flask App Implementation

**File:** `server/app.py`

### Step 1: Initialize Flask
```python
from flask import Flask
app = Flask(__name__)
```

### Step 2: Build the `/` (index) route
```python
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'
```

### Step 3: Build the `/<username>` (variable) route
```python
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'
```

### Step 4: Add auto-run block
```python
if __name__ == '__main__':
    app.run(port=5555, debug=True)
```

---

## Testing

### Problem: No test files existed
The placeholder test (`server/testing/codegrade_test.py`) had been removed in a previous commit (`rm cg placeholder test`).

### Solution: Created comprehensive test suite
**File:** `server/testing/test_app.py`

Tests cover:
- `'/'` returns 200 status and the correct welcome message
- `'/<username>'` returns 200 status and renders the username in the profile heading
- Works with any username (e.g. "Brightvilla")
- Returns HTML content type

### Problem: `ModuleNotFoundError: No module named 'server'`
Running `pytest` from the project root failed because:
1. `server/` directory lacked an `__init__.py` (not recognized as a package)
2. Python couldn't find the `server` module on `sys.path`

**Fixes:**
- Created `server/__init__.py` (empty package marker)
- Created `conftest.py` at the project root to add the project root to Python's module search path:

```python
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
```

### Final test results
```bash
$ pytest
============================================ test session starts ============================================
platform linux -- Python 3.8.13, pytest-8.3.5, pluggy-1.5.0
collected 6 items

server/testing/test_app.py ......                                                                    [100%]
============================================ 6 passed in 0.30s =============================================
```

All 6 tests pass in both Python 3.8.13 (pipenv venv) and Python 3.13 (system).

---

## Git Workflow

```bash
# Create feature branch
git checkout -b flask_routes

# Stage and commit changes
git add server/app.py README.md
git commit -m "Finish / and username route"

# Add fork remote
git remote add fork https://github.com/Brightvilla/python-intro-to-flask-technical-lesson.git

# Push to fork
git push fork flask_routes

# Add tests and fix imports
git add server/testing/test_app.py server/__init__.py conftest.py
git commit -m "Add test suite and fix module imports"
git push fork flask_routes
```

---

## Files Created/Modified

| File | Change |
|------|--------|
| `server/app.py` | Flask app with `/` and `/<username>` routes |
| `server/__init__.py` | Package marker (new) |
| `server/testing/test_app.py` | 6 test cases covering both routes (new) |
| `conftest.py` | Adds project root to `sys.path` (new) |
| `README.md` | Lab instructions (modified) |
| `labprocess.md` | This file (new) |

## Next Steps

1. **Create a Pull Request** on GitHub from `flask_routes` → `main`
2. **Merge the PR**
3. **Pull merged main locally:**
   ```bash
   git checkout main
   git pull fork main
   ```
4. **Delete the feature branch:**
   ```bash
   git branch -d flask_routes
