import datetime
import json
import random
import re
import traceback
import ast

from flask import request, jsonify

from app import app, db

@app.route('/')
def hello_world():
    return 'hello_world', 200

@app.route('/result/add', methods=['POST'])
def add_result():
    req = request.data.decode('utf-8')
    return str(req), 201