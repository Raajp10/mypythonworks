import optparse
import argparse
import scapy.all as sc

def args():
    parser=optparse.OptionParser()
    parser.add_option('-t', '--target',dest='ip',help='please enter the target address')
    [options, args]=parser.parse_args()
    if not options.ip:
        parser.error('Enter ip address')
    return options
    
def latest_args():#latest and generally used
    parser=argparse.ArgumentParser()
    parser.add_argument('-t', '--target',dest='ip',help='please enter the target address')
    options=parser.parse_args()
    if not options.ip:
        parser.error('Enter ip address')
    return options

def scan(ip):
    arp_req=sc.ARP(pdst=ip)
    broadcast=sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast=broadcast/arp_req
    answered_list=sc.srp(arp_req_broadcast,timeout=2,verbose=False)[0]
    clients_list=[]
    
    for element in answered_list:
        client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
        clients_list.append(client_dict)
        #print(element[1].psrc+"  "+element[1].hwsrc)
        #element[1].show()
    return clients_list

def results(res_dict):
    print('--------------------------------')
    print('IP address \t MAC address')
    print('--------------------------------')
    for client in res_dict:
        print(client["ip"]+"  "+client["mac"])


if __name__ == "__main__":
    results(scan(latest_args().ip))

#results(scan('192.168.0.1/24'))