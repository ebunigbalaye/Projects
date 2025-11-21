from scapy.all import IP,ICMP,TCP
from scapy.all import *
conf.use_npcap
def test_cycle(device_ip:str,no_of_packets:int):
    """This function takes a device's ip address as input and returns
      a list containing the average latency and the % packet loss and the test time"""
    packets = [IP(dst=device_ip)/ICMP(seq=i) for i in range(no_of_packets)]

    #Storing the time the packets were sent
    from datetime import datetime
    start_time = datetime.now()
    test_time = start_time.isoformat().split(".")[0]

    answered, unanswered = sr(packets, timeout=2, verbose=0) 
    no_of_answered = len(answered)
    no_of_unanswered = len(unanswered)

    #Calculating the average latency
    total_latency = 0
    for sent, received in answered:
        latency_in_s = (received.time - sent.sent_time)* 1000
        total_latency += latency_in_s 
    try :
        average_latency = total_latency /no_of_answered
        average_latency = round(average_latency,2)
    except ZeroDivisionError:
        average_latency = 0

    #Calculating the packet loss percentage
    packet_loss = (no_of_unanswered/(no_of_unanswered + no_of_answered)) * 100

    return [average_latency,packet_loss,test_time]

def check_port(device_ip,port_no):
    """This function checks the availability of a port/service"""
    pkt = IP(dst=device_ip)/TCP(dport=port_no, flags="S")
    response = sr1(pkt, timeout=2,verbose = 0)
    if response is None :
        return False
    elif response[TCP].flags == "SA":
        return True

def test_connectivity(device_ip):
    """This function checks the availability of a device by
    sending a single test packet."""
    if test_ip_address(device_ip):
        packet = IP(dst=device_ip)/ICMP()
        response = sr1(packet,timeout = 2,verbose=0)
        return response
    else:
        return None

def test_ip_address(device_ip):
    """This functions ensures the users imput matches the pattern for an ip address"""
    import re
    ipv4_pattern = re.compile(
    r'^('
    r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])'  # first octet
    r'\.){3}'                                        # dot, repeat 3 times
    r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])'  # last octet
    r'$')
    if re.match(ipv4_pattern,device_ip):
        return True
    else:
        return False