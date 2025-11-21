import streamlit as st
from metrics import *
import time 
import pandas as pd

st.title("Network Health Monitor")
st.text("Real-time ICMP and port availability monitoring for field devices, PLCs, and network hosts.")
with st.container():
    device_ip_column, port_no_column, monitoring_interval_column,no_of_packets_column = st.columns(4)
    with device_ip_column:
        device_ip = st.text_input("Device IP",max_chars=16)

    with port_no_column:
        port_no = st.number_input("Port No",step = 1)
        
    with monitoring_interval_column:
        monitoring_interval = st.number_input("Monitoring Interval",value = 60)
    
    with no_of_packets_column:
        no_of_packets = st.number_input("No of Packets",step = 1,value = 4 )

with st.container():
    st.header("Network Device Parameters")
    host_status_column, port_status_column, packet_loss_column ,time_of_last_test_column,average_latency_column = st.columns(5)
    with host_status_column:
        st.write("Host Status")
        if test_connectivity(device_ip) is None:
            st.warning("Host Not Available")
        else :
            st.success("Host Available")

    with port_status_column:
        st.write("Port Status")
        if check_port(device_ip,port_no) :
             st.success("Port Active")
        else:
            st.warning("Port Closed or Filtered")

    with packet_loss_column:
        try:
            pkt_loss = test_cycle(device_ip,no_of_packets)[1]
            if pkt_loss < 50:
                st.text("Packet Loss")
                st.success(f"{int(pkt_loss)}%")
            else:
                st.text("Packet Loss")
                st.error(f"{pkt_loss}%")

        except Exception as e :
            st.write(e)

    with average_latency_column:
        try : 
            st.write("Average Latency(ms)")
            st.success(test_cycle(device_ip,no_of_packets)[0])
        except Exception as e:
            st.write(e)

    with time_of_last_test_column:
        try : 
            st.write("Last test time")
            st.success(test_cycle(device_ip,no_of_packets)[2])
        except Exception as e:
            st.write(e)

with st.container():
    start_column, stop_column = st.columns(2)
    with start_column:
        start = st.button("Start Monitoring")
    with stop_column:
        stop = st.button("Stop Monitoring")

latency = []   
packetloss = []
st.header("Latency and Pakcet Loss Over Time Chart")   
df = pd.DataFrame({'Latency': latency,'Packet Loss':packetloss})
latency_and_packet_loss_chart = st.line_chart(df,use_container_width=True) 

while start:
    """This loop displays the chart when the start monitoring button has been clicked and 
    makes the chart disapperar when you click stop monitoring."""
    latency.append(test_cycle(device_ip,no_of_packets)[0])
    packetloss.append(test_cycle(device_ip,no_of_packets)[1])
    new_row = { "Latency": [latency[-1]],"Packet Loss": [packetloss[-1]]}
    latency_and_packet_loss_chart.add_rows(new_row)
    time.sleep(monitoring_interval)
    if start is False:
        break


