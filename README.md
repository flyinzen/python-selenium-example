# python-selenium-example
Here's an example of GUI autotest framework, based on pytest and selenium libraries. 

## Setup

Perform following commands from root directory of project:

```
python -m venv venv
cd .venv/Scripts
activate
pip install -r requirements.txt
```

Also, there should be replaced test users in ```data/users/users.py``` (users present in this file are invalid).

## Run

Once installed, you could run standatd Pytest command with arguments:

```python -m pytest [pytest args]```

## Logging
Currently, no logging present, except pytest console output.
