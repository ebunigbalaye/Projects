# **Network Latency & Port Monitor**

A simple one-page Streamlit tool that measures network latency and checks if a port is reachable. Built to demonstrate practical networking and software engineering skills.

## Features

* Real-time latency measurement (average latency, packet loss, packets received)
* Network Status Check: Available or Not Available
* Port status check: Open or  Closed
* Live chart plotting latemcy and percentage packet loss 


## How it works

Every interval (e.g., 1–5 seconds), the app:

1. Sends a small batch of probe packets
2. Measures round-trip time for replies
3. Checks port state using a TCP SYN probe
4. Records results with a timestamp
5. Updates the live chart only while “Start Monitoring” is active


## Tech stack

* Python
* Streamlit
* Scapy
* Pandas


## To run the app

pip install streamlit scapy pandas
streamlit run app.py
