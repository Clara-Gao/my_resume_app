import oyaml as yaml
from flask import Flask
from flask import Flask, render_template,jsonify,request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/run", methods=["POST"])
def run():
    from services.test_services import run_flow

    data = request.get_json()
    return run_flow(data)

@app.route('/')
def index():
    with open('_config.yaml', 'r', encoding='utf-8') as config_file:
        website_data = yaml.load(config_file, Loader=yaml.FullLoader)

    return render_template('index.html', data=website_data)


if __name__ == '__main__':
    app.run(debug=False, port=5000)
