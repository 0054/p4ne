from pysnmp.hlapi import *


snmp_obj1 = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_obj2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')


g = getCmd(SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('10.31.70.107', 161)),
        ContextData(),
        ObjectType(snmp_obj1))

n = nextCmd(SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('10.31.70.107', 161)),
        ContextData(),
        ObjectType(snmp_obj2),
        lexicographicMode=False
        )

def print_data(snmp):
    for i in snmp:
        errorIndication, errorStatus, errorIndex, varBinds = i
        if errorIndication:
            print('errorIndication: {}'.format(errorIndication))
        elif errorStatus:
            print('errorStatus: {} errorIndex: {}'.format(errorStatus, errorIndex))
        else:
            for i in varBinds:
                print(i.prettyPrint())

print_data(g)
print_data(n)
