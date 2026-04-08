# SDN Traffic Monitoring and Statistics Collector (POX + Mininet)

## Problem Statement

This project implements a Software Defined Networking (SDN) controller using POX to monitor and collect traffic statistics from network switches. The controller periodically retrieves flow and port statistics, displays packet and byte counts, and generates simple reports.

---

## Objectives

* Implement controller–switch interaction using OpenFlow
* Retrieve and display flow statistics (packet count, byte count)
* Perform periodic monitoring of network traffic
* Generate simple alerts based on traffic patterns

---

## Technologies Used

* Mininet (network emulation)
* POX Controller (SDN controller)
* OpenFlow 1.0
* Python 3.x

---

## Setup Instructions

### 1. Install Dependencies

```bash
sudo apt update
sudo apt install -y mininet git python3
```

### 2. Clone POX Controller

```bash
git clone https://github.com/noxrepo/pox.git
cd pox
```

### 3. Add Monitoring Module

Place `traffic_monitor.py` inside:

```bash
pox/pox/misc/
```

### 4. Run Controller

```bash
cd pox
./pox.py openflow.of_01 forwarding.l2_learning misc.traffic_monitor
```

### 5. Run Mininet (New Terminal)

```bash
sudo mn --topo single,3 --controller remote
```

---

## Execution

### Test 1: Connectivity

```bash
mininet> pingall
```

### Test 2: Generate Traffic

```bash
mininet> iperf h1 h2
```

---

## Features Implemented

### Flow Statistics Monitoring

* Packet count per flow
* Byte count per flow

### Port Statistics Monitoring

* RX and TX packet counts per port

### Periodic Monitoring

* Statistics requested every 5 seconds

### Traffic Alerts

* Detects high traffic flows using thresholds

---

## Output Screenshots

Include the following screenshots in the `screenshots/` folder:

1. Controller startup (POX terminal showing listening port)
2. Mininet topology initialization
3. Ping test results (0% packet loss)
4. Flow statistics output
5. Port statistics output
6. Iperf traffic generation
7. Increasing packet/byte counts over time

---

## Working Explanation

The controller:

1. Detects switch connections using ConnectionUp
2. Periodically sends flow and port statistics requests
3. Receives responses from switches
4. Logs packet and byte counts
5. Generates alerts for high traffic

---

## Validation and Testing

* Verified connectivity using ping
* Measured throughput using iperf
* Observed increasing packet and byte counts
* Confirmed periodic updates every 5 seconds

---

## Performance Observations

* Higher traffic results in increased byte counts
* Iperf generates significantly more traffic than ping
* Flow and port statistics reflect real-time activity

---

## Known Issues

* POX may display a Python version warning, which does not affect functionality
* Port 6633 must be free before running the controller

---

## References

* POX Controller Documentation
* Mininet Documentation
* OpenFlow Specification

---

## Author

* Name: [Your Name]
* Course: SDN / Networking Lab
* Project Type: Individual

---

## Conclusion

This project demonstrates the use of SDN principles for monitoring network traffic. The controller successfully collects, analyzes, and reports network statistics in real time.
