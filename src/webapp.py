import flask
from flask import request, redirect
from db_query import get_last_results
from os import getcwd
from pathlib import Path
import yaml
import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = False

parent_path = Path(getcwd()).parent.absolute()

with open(f"{parent_path}/config/configuration.yml") as f:
    web_vars = yaml.safe_load(f)['railway']

@app.route('/')
def welcome():
    return f'''Hi!<br><br>You first need to set the variables environment by sending the <b>variables.yml</b> file by sending a POST request to <a href="http://127.0.0.1:5000/post/variables">this address</a>.<br><br>
    Then, you need to define your soda checks in SodaCL by sending the <b>checks.yml</b> file by sending a POST request to <a href="http://127.0.0.1:5000/post/checks">this address</a>.<br><br>
    You can check if they have been correctly loaded by printing out:
     <ul><li>the <a href="/get/variables"><b>variables.yml</b></a></li> 
     <li>the <a href="/get/checks"><b>checks.yml</b></a></li></ul><br>
    When these two files have been sent,  you can <a href="/run/scan">run a Soda scan</a>.<br><br>
    Finally, you can check the results of the latest Soda scan at <a href="/get/results">this address</a>.<br><br><br>
    Have fun!'''

@app.route('/run/scan', methods=['GET'])
def run_soda_scan_results():
    import db
    status = {"status": "success",
         "datetime": datetime.datetime.now()}
    return status

@app.route('/get/results', methods=['GET'])
def last_results():
    results = get_last_results()
    return results

@app.route('/get/checks', methods=['GET'])
def get_checks():
    with open(f'{parent_path}/config/checks.yml', 'r') as f:
        checks_file = yaml.safe_load(f)
    return checks_file

@app.route('/get/configuration', methods=['GET'])
def get_configuration():
    with open(f'{parent_path}/config/configuration.yml') as f:
        configuration_file = yaml.safe_load(f)
    return configuration_file

@app.route('/get/variables', methods=['GET'])
def get_variables():
    with open(f'{parent_path}/config/variables.yml') as f:
        variables_file = yaml.safe_load(f)
    return variables_file

@app.route('/post/checks', methods=['POST'])
def post_soda_checks():
    data = request.get_data()

    with open(f'{parent_path}/config/checks.yml', 'w') as f:
        f.write(data.decode("utf-8"))

    return "Successfully loaded 'checks.yml' file."

@app.route('/post/configuration', methods=['POST'])
def post_soda_configuration():
    data = request.get_data()

    with open(f'{parent_path}/config/configuration.yml', 'w') as f:
        f.write(data.decode("utf-8"))

    return "Successfully loaded 'configuration.yml' file."

@app.route('/post/variables', methods=['POST'])
def post_soda_variables():
    data = request.get_data()

    with open(f'{parent_path}/config/variables.yml', 'w') as f:
        f.write(data.decode("utf-8"))

    return "Successfully loaded 'variables.yml' file."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
