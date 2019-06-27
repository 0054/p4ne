import requests
import json

from flask import Flask
from flask import render_template, jsonify
requests.packages.urllib3.disable_warnings()



def get_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    config = {
            'username': 'devnetuser',
            'password': 'Cisco123!'
            }
    header = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(config), headers=header, verify=False)
    return r.json()['response']['serviceTicket']


def get_topology(ticket):
    url = 'https://devnetapi.cisco.com/sandbox/apic_em/api/v1/topology/physical-topology'
    header = {
            'content-type': 'application/json', 'X-Auth-Token': ticket
            }
    r = requests.get(url, headers=header, verify=False)
    return r.json()['response']

ticket = get_ticket()

net_topology = get_topology(ticket)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('topology.html')

@app.route('/api/topology')
def topology():
    return jsonify(net_topology)


if __name__ == "__main__":
    app.run(debug=True)


