from ipaddress import IPv4Interface
import re
import glob


gen_file = glob.iglob('/home/jet/seafile/Seafile/p4ne_training/config_files/*.txt')
# gen_file = glob.iglob('/home/mint/Dropbox/python/JET_PYTHON/config_files/*.txt')

regex_ip = r'.*ip address (([0-9]{1,3}.?){4}) (([0-9]{1,3}.?){4})' 
regex_int = r'^interface (.*)'
regex_host = r'^hostname (.*)'



def classify(s):
    
    match = re.match(regex_ip, s)
    if match:
        ip, _, mask, _ = match.groups()
        int = '/'.join([ip,mask])
        return { 'ip': IPv4Interface(int) }

    if re.match(regex_int, s):
        return { 'int': s.split()[1] }
    
    if re.match(regex_host, s):
        return { 'host': s.split()[1] }

    return {}

def main():
    interfaces = list()
    ips = list()
    hosts = list()

    for file in gen_file:
        with open(file) as f:
            for line in f:
                data = classify(line)
                if bool(data):
                    if data.get('ip'):
                        ips.append(data['ip'])
                    elif data.get('int'):
                        interfaces.append(data['int'])
                    elif data.get('host'):
                        hosts.append(data['host'])
    return [interfaces, ips, hosts] 


if __name__ == "__main__":
    data = dict(zip(['interface','ip','host'], main()))

    print(data['interface'])
    print(data['ip'])
    print(data['host'])
