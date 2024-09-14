# PRODIGY_CY_Task-05

Network Packet Sniffer

This is a Python script that captures and analyzes network packets using the Scapy library. It displays relevant information such as source and destination IP addresses, protocols, and payload data.

## How to Run

1. **Clone the Repository**

   git clone https://github.com/KKGOKUL/PRODIGY_CY_TASK-05.git
  
2. ** Download ZIP file from my repository**

**Features**

1.Real-time Packet Sniffing: Monitors and captures network packets on a given interface.
2.Packet Processing: Each packet is processed and displayed with a summary using the Scapy library.
3.Customizable Interface: The user can specify the network interface to sniff packets from.

**Prerequisites**

1.Python 3.x
2.Scapy library

**Example**

==================================================
Sniffing packets on interface Wi-Fi...
Ether / IPv6 / TCP 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 > 2620:1ec:21::14:https A / Raw
Ether / IPv6 / TCP 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 > 2620:1ec:21::14:https A / Raw
Ether / IPv6 / TCP 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 > 2620:1ec:21::14:https A / Raw
Ether / IPv6 / TCP 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 > 2620:1ec:21::14:https A / Raw
Ether / IPv6 / TCP 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 > 2620:1ec:21::14:https PA / Raw
Ether / IPv6 / TCP 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 > 2620:1ec:21::14:https PA / Raw
Ether / IPv6 / TCP 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 > 2620:1ec:21::14:https PA / Raw
Ether / IPv6 / TCP 2620:1ec:21::14:https > 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 A
Ether / IPv6 / TCP 2620:1ec:21::14:https > 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 A
Ether / IPv6 / TCP 2620:1ec:21::14:https > 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 A
Ether / IPv6 / TCP 2620:1ec:21::14:https > 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 A
Ether / IPv6 / TCP 2620:1ec:21::14:https > 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 A
Ether / IPv6 / TCP 2620:1ec:21::14:https > 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 PA / Raw
Ether / IPv6 / TCP 2620:1ec:21::14:https > 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 A
Ether / IPv6 / TCP 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 > 2620:1ec:21::14:https A
Ether / IPv6 / TCP 2620:1ec:21::14:https > 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 PA / Raw
Ether / IPv6 / TCP 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 > 2620:1ec:21::14:https A
Ether / IPv6 / TCP 2620:1ec:21::14:https > 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 PA / Raw
Ether / IPv6 / TCP 2620:1ec:21::14:https > 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 PA / Raw
Ether / IPv6 / TCP 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 > 2620:1ec:21::14:https A
Ether / IPv6 / TCP 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 > 2620:1ec:21::14:https PA / Raw
Ether / IPv6 / TCP 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 > 2620:1ec:21::14:https PA / Raw
Ether / IPv6 / TCP 2620:1ec:21::14:https > 2409:408d:3308:4abf:ecdb:1834:6583:e04c:62468 A
Ether / IPv6 / ICMPv6ND_NS / ICMPv6 Neighbor Discovery Option - Source Link-Layer Address d2:a1:95:3f:22:51
Ether / IPv6 / ICMPv6ND_NA / ICMPv6 Neighbor Discovery Option - Destination Link-Layer Address 3e:91:0a:30:73:7c
Ether / IP / UDP / DNS Qry "b'browser-intake-datadoghq.com.'" 
Ether / IP / UDP / DNS Qry "b'browser-intake-datadoghq.com.'" 
Ether / IP / UDP / DNS Qry "b'browser-intake-datadoghq.com.'" 
Ether / IP / UDP / DNS Ans "2600:1f18:24e6:b901:72e3:1bfe:b271:96b2" 
Ether / IP / UDP / DNS Ans "3.233.158.26" 
Ether / IP / UDP / DNS Ans 

==================================================



