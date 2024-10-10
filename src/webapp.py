import flask
from db_query import get_last_results

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/soda_scan', methods=['GET'])
def run_soda_scan_results():
    import db
    results = get_last_results()
    return results

@app.route('/', methods=['GET'])
def last_results():
    results = get_last_results()
    return results

app.run()