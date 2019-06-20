from ipaddress import IPv4Network
import random



class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        self.ip = random.randint(184549376, 3741319168)
        self.mask = random.randint(8, 24)
        super(IPv4RandomNetwork, self).__init__((self.ip, self.mask), strict=False)
    
    def regular(self):
        return self.is_global()

    def key_value(self):
        ip = int(self.ip)
        mask = int(self.netmask) << 32
        return mask + ip


iplist = []
for x in range(0, 50):
    iplist.append(IPv4RandomNetwork())

def keyfunc(x):
    return x.key_value()

for net in sorted(iplist, key=keyfunc):
    print(net)

