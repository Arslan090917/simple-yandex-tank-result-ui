'''
Script for sending result of loadtest
Must be in the same directory with loadtest
Script has additional params --url_arg

Example: python3 result_sender.py --url_arg "http://<any url>:<any port>/result/add"
'''

import os
import ast
import re
import json
import datetime
import requests
import argparse


def get_file() -> str:
    current_location = os.path.abspath(os.path.dirname(__file__))
    current_time = datetime.datetime.today()

    list_dir = os.listdir(current_location)

    for dir in list_dir:
        if re.search('\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}\.\d{6}', dir):
            date_folder = datetime.datetime.strptime(dir, '%Y-%m-%d_%H-%M-%S.%f')
            if (current_time - date_folder) < datetime.timedelta(hours=15):
                return f'{current_location}/{dir}/test_data.log'
            else:
                raise Exception('There is not file with logs')
        else:
            continue

def parse_file() -> str:
    result = {
        'load_result': {
            'rps': [],
            'ts': []
        }
    }
    with open(get_file(), 'r') as f:
        for i in f:
            dict_f = ast.literal_eval(i)
            result['load_result']['rps'].append(dict_f['stats']['metrics']['reqps'])
            result['load_result']['ts'].append(dict_f['stats']['ts'])
    assert len(result['load_result']['rps']) == len(result['load_result']['ts']), 'Заебца'
    return json.dumps(result)

def send_request(url : str, body : str) -> None:
    res = requests.post(url, data=body)
    try:
        assert res.status_code == 201
    except:
        raise Exception('Service is unavailable')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Setup url for sending result')
    # Required positional argument
    parser.add_argument('--url_arg', type=str,
                        help='A required url address of service load result')
    args = parser.parse_args()
    if args.url_arg:
        send_request('http://localhost:44551/result/add', parse_file())
    else:
        raise Exception('There is no a url address')

