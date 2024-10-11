PostgreSQL server is supposed to be started.

Create virtual environment and activate it:

```
python3 -m venv venv
source ./venv/bin/activate
```

Upgrade pip in your environment and install dependencies:

```
pip install --upgrade pip
pip install -r requirements.txt
```

Launch the app:

```
cd ./src

python3 webapp.py
```

You can access it through your web browser to the address `http://localhost:5000`.
