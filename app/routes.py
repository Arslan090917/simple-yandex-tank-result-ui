import datetime
import json
import traceback

from flask import request, jsonify, render_template
from jinja2 import Environment, PackageLoader, select_autoescape

from app import app, db
from app.models import Result

# env = Environment(
#     loader=PackageLoader('simple-yandex-tank-result-ui', 'templates'),
#     autoescape=select_autoescape(['html'])
# )

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/result/add', methods=['POST'])
def add_result():
    req = request.data.decode('utf-8')
    json_data = json.loads(req)
    avg_rps = sum(json_data['load_result']['rps']) // len(json_data['load_result']['rps'])
    db_result = Result(
        LoadResult=req,
        AvgRPS=avg_rps
    )
    db.session.add(db_result)
    db.session.commit()
    return json.dumps({'Status': 'Result added'}), 201

@app.route('/result', methods=['GET'])
def get_result():
    results = {}
    db_results = db.session.query(Result).all()
    for db_result in db_results:
        results[db_result.Id] = [str(db_result.CreateDateUtc), db_result.AvgRPS]
    return render_template('result.html', load_results=results)
    # try:
    #     db_result = db.session.query(Result).all()
    #     return db_result.LoadResult, 200
    # except Exception:
    #     answer = traceback.format_exc()
    #     app.logger.error(answer)
    #     return answer,  500

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard/loadResult', methods=['GET'])
def dashboard_get_by_id():
    id = request.args.get('id')
    db_result = db.session.query(Result).filter_by(Id=id).first()
    return db_result.LoadResult, 200