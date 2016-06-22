import nmap

def funcao_nmap(ip_addr):

    nm = nmap.PortScanner()
    nm.scan( ip_addr, '22-1000')
    nm.command_line()
    # 'nmap -oX - -p 22-443 -sV 127.0.0.1'
    nm.scaninfo()
    # {'tcp': {'services': '22-443', 'method': 'connect'}}
    nm.all_hosts()
    # ['127.0.0.1']
    nm[ip_addr].hostname()
    # 'localhost'
    nm[ip_addr].state()
    # 'up'
    nm[ip_addr].all_protocols()
    # ['tcp']
    nm[ip_addr]['tcp'].keys()
    # [80, 25, 443, 22, 111]
    nm[ip_addr].has_tcp(22)
    # True
    nm[ip_addr].has_tcp(23)
    # False
    nm[ip_addr]['tcp'][22]
    # {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh'}
    nm[ip_addr].tcp(22)
    # {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh'}
    nm[ip_addr]['tcp'][22]['state']
    # 'open'

    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)

            lport = nm[host][proto].keys()
            # lport.sort()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))


if __name__ == '__main__':
    funcao_nmap()