import datetime
import json
import random
import re
import traceback

from flask import request, jsonify

from app import app, db


@app.route('/')
def hello_world():
    return 'hello_world', 200