# myAPIs
A generic repository for general API tests with Flask.

# Requirements

- Python 3.12
- PIP 25.1.1

# Installation

1. Clone the repository:
```sh
git clone https://github.com/akai-keisanki/myAPIs.git
```

2. Start a python virtual environment:
```
python -m venv .venv
source ./.venv/bin/activate
```

3. Copy the environment variable examples and edit them:
```
cp .env.example .env
sed -i "s/yoursecretkey/$(python3 -c 'import secrets; print(secrets.token_hex())')/" .env
```

4. Configure the database:
```
python -m flask db init
python -m flask db migrate
python -m flask db upgrade
```

5. Run
```
python -m flask run
```