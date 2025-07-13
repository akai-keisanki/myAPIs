# myAPIs

Repository for my test APIs and web tools with Flask.

Repositório para minhas APIs de teste e ferramentas web com Flask.

# Requirements

Recomenda-se:

- Python 3.12.3
- PIP 24.0

# Installation:

- Go to the working directory. (E. g. with `cd /path/to/myAPIs`)

- Start a virtual environment and source it. (E. g. `python3 -m venv .venv && source .venv/bin/activate`)

- Install the requirements with pip. (E. g. `pip install -r requirements.txt`)

- Copy or move `.env.example` to `.env`. (E. g. `cp .env.example .env`)

- Edit `.env` to change the `SECRET_KEY`. (E. g. `sed -i "s/yoursecretkey/$(python3 -c 'import secrets; print(secrets.token_hex())')/" .env`)
