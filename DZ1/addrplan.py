#!/usr/bin/env python3

import re
import glob
from ipaddress import IPv4Interface
import pandas as pd

gen_file = glob.iglob('/home/jet/seafile/Seafile/p4ne_training/config_files/*.txt')
#gen_file = glob.iglob('/home/mint/Dropbox/python/JET_PYTHON/config_files/*.txt')

regex = r'.*ip address (([0-9]{1,3}.?){4}) (([0-9]{1,3}.?){4})'


def parse_interface(s):
    match = re.match(regex, s)
    if match:
        ip, _, mask, _ = match.groups()
        return  IPv4Interface('/'.join([ip, mask]))


def get_int_list():
    int_set = set()
    for file in gen_file:
        with open(file) as f:
            for line in f:
                interface = parse_interface(line)
                if interface:
                    int_set.add(interface)
    return int_set

def get_report(data):
    report = []
    for interface in data:
        n = {}
        # n['ip'] = interface.ip.compressed
        n['netmask'] = interface.network.netmask.compressed
        n['network'] = interface.network.network_address.compressed
        report.append(n)
    return report

def print_report(data):
    print('{:>20} {:>20}'.format(data.columns[0], data.columns[1]))
    for network, netmask in data.values:
        print('{:>20} {:>20}'.format(network, netmask))

def safe_to_excel(data, filename='report'):
    data.set_index('network').to_excel('./{}.xlsx'.format(filename))



if __name__ == "__main__":
    report = get_report(get_int_list())
    df = pd.DataFrame(report)
    df = df.drop_duplicates(subset = 'network').sort_values('network')
    
    print_report(df)
    safe_to_excel(df)
    
