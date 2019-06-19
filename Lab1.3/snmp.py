from pysnmp.hlapi import *



g = getCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('10.31.70.107', 161)),
        ContextData(),
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
        )

n = nextCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('10.13.70.107', 161)),
        ContextData(),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
        lexicographicMode=False)

def print_data(snmp):
    for i in snmp:
        errorIndication, errorStatus, errorIndex, varBinds = i
        if errorIndication:
            print ('Error Indication: {}'.format(errorIndication))
        elif errorStatus:
            print('Error Status: {}, Error Index: {}'.format(errorStatus, errorIndex))
        else:
            for i in varBinds:
                print(i.prettyPrint())

print_data(n)

