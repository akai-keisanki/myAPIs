# myAPIs

Repository for my test APIs and web tools with Flask.

Repositório para minhas APIs de teste e ferramentas web com Flask.

# Requirements

Recommended:

- Python 3.12.3

- PIP 24.0

# Installation:

- Go to the working directory. (E. g. with `cd /path/to/myAPIs`)

- Start a virtual environment and source it. (E. g. `python3 -m venv .venv && source .venv/bin/activate`)

- Install the requirements with pip. (E. g. `pip install -r requirements.txt`)

- Copy or move `.env.example` to `.env`. (E. g. `cp .env.example .env`)

- Edit `.env` to change the `SECRET_KEY`. (E. g. `sed -i "s/yoursecretkey/$(python3 -c 'import secrets; print(secrets.token_hex())')/" .env`)

Quick installation bash for Linux:

```sh
# Change path/to/myAPIs to the actual path to the working directory.
cd /path/to/myAPIs

# NOTE: `python3` could also be `python` for some systems.
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

# NOTE: `python3` could also be `python` for some systems.
sed -i "s/yoursecretkey/$(python3 -c 'import secrets; print(secrets.token_hex())')/" .env
```

# Routes:

### Root:

- Check: `/`

### FileSystem:

- Check: `/fs`

- File access: `/fs/access/<path:item_path>`; Args/Params: `r`, `w`, `a` (operations), `encoding`: string; Data: text to be written when using the `w` or `a` parameter.

