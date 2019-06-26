from flask import Flask, jsonify
import json
import glob
import re

app = Flask(__name__)


config_files = glob.glob('/home/jet/seafile/Seafile/p4ne_training/config_files/*.txt')


def classify_configs():
    regex_host = r'^hostname (.*)'
    regex_ip = r'.*ip address (([0-9]{1,3}.?){4}) (([0-9]{1,3}.?){4})'
    hosts = {}
    for file in config_files:
        with open(file) as f:
            for line in f:
                if re.match(regex_host, line):
                    hostname = line.split()[1]
                    hosts[hostname] = []
                match = re.match(regex_ip, line)
                if match:
                    ip, *_ = match.groups()
                    hosts[hostname].append(ip)
    return hosts

def get_help():
    help = {'/': 'show help',
            '/config': 'list hosts with config files',
            '/config/(hostname)': 'get ip list'}
    return help

@app.route('/')
def index():
    return jsonify(get_help())

@app.route('/configs')
def config():
    return jsonify(list(classify_configs().keys()))

@app.route('/config/<hostname>')
def get_hosts_ip(hostname):
    ip_list = classify_configs()[hostname]
    return jsonify(ip_list)

if __name__ == "__main__":
    app.run()
