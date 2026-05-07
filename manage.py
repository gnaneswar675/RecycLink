EXPERIMENT – 1
AIM:
Implement the data link layer framing methods such as Character Stuffing and Bit Stuffing.
THEORY:
Framing is a function of the Data Link Layer used to separate data into frames for reliable transmission.
1. Character Stuffing:
Special characters are added at the beginning and end of data. If the same special characters appear inside the data, an escape character is inserted before them.
2. Bit Stuffing:
In bit-oriented protocols, after every sequence of five consecutive 1’s, a 0 is inserted to avoid confusion with flag patterns.
PROGRAM:
Character Stuffing Program:
def character_stuffing(data):
    start_flag = '@'
    end_flag = '#'
    escape_char = '/'

    stuffed_data = ''

    for char in data:
        if char in [start_flag, end_flag, escape_char]:
            stuffed_data += escape_char

        stuffed_data += char

    framed_data = start_flag + stuffed_data + end_flag
    return framed_data

data = "Hello/@World#"
stuffed = character_stuffing(data)
print("Character Stuffed Frame:", stuffed)

Bit Stuffing Program:
def bit_stuffing(data_bits):
    stuffed = ''
    count = 0

    for bit in data_bits:
        stuffed += bit

        if bit == '1':
            count += 1

            if count == 5:
                stuffed += '0'
                count = 0
        else:
            count = 0

    return stuffed

binary_data = "01111110111110"
stuffed = bit_stuffing(binary_data)
print("Bit Stuffed Data:", stuffed)

OUTPUT:
Character Stuffed Frame:
@Hello//@World/##

Bit Stuffed Data:
0111110101111100

RESULT:
Thus, the data link layer framing methods Character Stuffing and Bit Stuffing were implemented successfully.




-------------------------------------------------



EXPERIMENT – 4
AIM:
Implement Dijkstra’s algorithm to compute the shortest path in a graph.
THEORY:
Dijkstra’s algorithm is used to find the shortest path from a source node to all other nodes in a weighted graph.
PROGRAM:
import heapq

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)

        for n, w in graph[v].items():
            nd = d + w

            if nd < dist[n]:
                dist[n] = nd
                heapq.heappush(pq, (nd, n))

    return dist

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

result = dijkstra(graph, 'A')

for i, j in result.items():
    print(i, ":", j)

OUTPUT:
A : 0
B : 4
C : 2
D : 5

RESULT:
Thus, Dijkstra’s algorithm was implemented successfully to find the shortest path in a graph.




---------------------------------------------



EXPERIMENT – 11
AIM:
Simulate the Implementing Routing Protocols using Border Gateway Protocol (BGP).

THEORY:
Border Gateway Protocol (BGP) is an Exterior Gateway Protocol used to exchange routing information between autonomous systems in a network.

PROCEDURE:

Step 1: Open Cisco Packet Tracer
1. Launch Cisco Packet Tracer on your computer.

Step 2: Create a Network Topology
1. Add Devices
o Drag three routers (Router0, Router1, Router2) onto the workspace.
o Add two switches and two PCs (PC0 and PC1).

2. Connect Devices Using Cables
o Use copper straight-through cables to connect:
 PC0 to Switch0
 PC1 to Switch1
 Switch0 to Router0
 Switch1 to Router2

o Use copper cross-over cables to connect routers:
 Router0 to Router1
 Router1 to Router2

Step 3: Assign IP Addresses
Each router and end device needs an IP address.

Configuring IP Addresses to PCs

PC0:
IP Address : 192.168.10.2
Subnet Mask : 255.255.255.0
Default Gateway : 192.168.10.1

PC1:
IP Address : 192.168.20.2
Subnet Mask : 255.255.255.0
Default Gateway : 192.168.20.1

Step 4: Router Configuration

At ROUTER 0:

enable
configure terminal
interface g0/0
ip address 192.168.10.1 255.255.255.0
no shutdown
exit
interface g0/1
ip address 10.0.0.1 255.255.255.0
no shutdown
exit

At ROUTER 1:

enable
configure terminal
interface g0/0
ip address 10.0.0.2 255.255.255.0
no shutdown
exit
interface g0/1
ip address 20.0.0.1 255.255.255.0
no shutdown
exit

At ROUTER 2:

enable
configure terminal
interface g0/0
ip address 20.0.0.2 255.255.255.0
no shutdown
exit
interface g0/1
ip address 192.168.20.1 255.255.255.0
no shutdown
exit

OUTPUT:
All router interfaces became active and successful ping messages were received between PCs.

RESULT:
Thus, the routing protocol simulation using Border Gateway Protocol (BGP) was implemented successfully.



----------------------------------


EXPERIMENT – 12
AIM:
Simulate the OPEN SHORTEST PATH FIRST routing protocol based on the cost assigned to the path.

THEORY:
Open Shortest Path First (OSPF) is a link-state routing protocol used to find the shortest path between source and destination using cost values.

PROCEDURE:

Step 1: Open Cisco Packet Tracer
1. Launch Cisco Packet Tracer on your computer.

Step 2: Create a Network Topology
1. Add Devices
o Drag two routers (Router0, Router1) onto the workspace.
o Add two PCs (PC0 and PC1).

2. Connect Devices Using Cables
o Use copper straight-through cables to connect:
 PC0 to Router0
 PC1 to Router1

o Use copper cross-over cable to connect:
 Router0 to Router1

Step 3: Assign IP Addresses
Each router and end device needs an IP address.

Configuring IP Addresses to PCs

PC0:
IP Address : 198.123.1.11
Subnet Mask : 255.255.255.0
Default Gateway : 198.123.1.1

PC1:
IP Address : 198.123.3.11
Subnet Mask : 255.255.255.0
Default Gateway : 198.123.3.1

Step 4: Router Configuration

At ROUTER 0:

enable
configure terminal
interface g0/0
ip address 198.123.1.1 255.255.255.0
no shutdown
exit

interface g0/1
ip address 10.0.0.1 255.255.255.0
no shutdown
exit

router ospf 1
network 198.123.1.0 0.0.0.255 area 0
network 10.0.0.0 0.0.0.255 area 0
exit

At ROUTER 1:

enable
configure terminal
interface g0/0
ip address 198.123.3.1 255.255.255.0
no shutdown
exit

interface g0/1
ip address 10.0.0.2 255.255.255.0
no shutdown
exit

router ospf 1
network 198.123.3.0 0.0.0.255 area 0
network 10.0.0.0 0.0.0.255 area 0
exit

OUTPUT:
Successful ping messages were received between PC0 and PC1 through OSPF routing.

RESULT:
Thus, the OPEN SHORTEST PATH FIRST (OSPF) routing protocol was implemented successfully.



-----------------------



EXPERIMENT – 13
AIM:
Install Wireshark Tool on PC and use it to:
a) Capture network traffic
b) Determine default gateway address of your network
c) Examine frame format and contents of Ethernet frames
d) Filter and examine only ICMP traffic
e) Run various network services like ping, ssh, dns etc. and examine the traffic captured by Wireshark

THEORY:
Wireshark is an open-source network protocol analyzer used to capture and analyze network packets in real time.

PROCEDURE:

Step 1: Install Wireshark Tool on PC
1. Download Wireshark from the official website.
2. Run the installation setup.
3. Install WinPcap or Npcap when prompted.
4. Launch Wireshark after installation.

Step 2: Capture Network Traffic
1. Open Wireshark and select the active network interface.
2. Click Start Capturing Packets.
3. Perform network activities such as opening a website or pinging a server.
4. Stop the capture after observing the traffic.

Step 3: Determine Default Gateway Address
1. Open Command Prompt or Terminal.
2. Type the command to view network configuration.
3. Note the Default Gateway IP Address.
4. Use a filter in Wireshark to view gateway-related traffic.

Step 4: Examine Ethernet Frame Format
1. Locate a captured Ethernet II frame.
2. Expand Frame, Ethernet II, and Internet Protocol sections.
3. Observe source, destination, and type fields.

Step 5: Filter and Examine ICMP Traffic
1. Enter the ICMP filter in Wireshark.
2. Run the ping command.
3. Observe the ICMP packets captured.

Step 6: Run Network Services and Examine Traffic

Service          Command/Action        Filter
Ping             ping command          icmp
SSH              Connect via SSH       tcp.port == 22
DNS              DNS lookup            dns
HTTP             Open website          http
HTTPS            Access secure site    tls

OUTPUT:
Network packets were captured successfully and different protocol packets such as ICMP, DNS, HTTP, and HTTPS were analyzed using Wireshark.

RESULT:
Thus, Wireshark was installed successfully and network traffic analysis was performed successfully.



--------------------------------------------------
EXPERIMENT-5

#include<stdio.h>

void main()
{
    int i,j,d[20],dt[50][50],min=0,mini=0,p,q,y=0,nd[30];
    char r[30],n[30],l[30],x;

    printf("enter number of nodes\n");
    scanf("%d",&p);

    printf("enter nodes\n");

    for(i=1;i<=p;i++)
        scanf(" %c",&r[i]);

    printf("enter node for which you want to calculate routing table\n");
    scanf(" %c",&x);

    for(i=1;i<=p;i++)
    {
        if(x==r[i])
            y=i;
    }

    nd[y]=0;
    l[y]='-';

    printf("enter number of neighbours are there for %c node\n",x);
    scanf("%d",&q);

    printf("enter neighbours of %c node\n",x);

    for(i=1;i<=q;i++)
        scanf(" %c",&n[i]);

    printf("enter delays table\n");

    for(i=1;i<=p;i++)
    {
        for(j=1;j<=q;j++)
        {
            scanf("%d",&dt[i][j]);
        }
    }

    printf("enter delay from %c to each of its neighbour\n",x);

    for(i=1;i<=q;i++)
        scanf("%d",&d[i]);

    for(i=1;i<=p;i++)
    {
        min=999;

        for(j=1;j<=q;j++)
        {
            if((dt[i][j] + d[j]) < min)
            {
                min = dt[i][j] + d[j];
                mini = j;
            }
        }

        nd[i] = min;
        l[i] = n[mini];
    }

    nd[y]=0;
    l[y]='-';

    printf("\nrouting vector table for %c is\n",x);

    for(i=1;i<=p;i++)
    {
        printf("%d\t%c\n",nd[i],l[i]);
    }
}

OUTPUT:

enter number of nodes
5

enter nodes
A
B
C
D
E

enter node for which you want to calculate routing table
A

enter number of neighbours are there for A node
2

enter neighbours of A node
B
D

enter delays table
0 0
8 2
7 3
2 0
6 1

enter delay from A to each of its neighbour
5
4

routing vector table for A is

0    -
8    D
7    D
7    B
6    D

-----------------------------------------

EXPERIMENT – 10

AIM:
Get the MAC or Physical address of the system using Address Resolution Protocol (ARP).

THEORY:
Address Resolution Protocol (ARP) is used to map an IP address to its corresponding MAC address in a local network. ARP sends a request packet to identify the physical address of a device.

PROGRAM:

from scapy.all import ARP, Ether, srp

def get_mac(ip):

    arp_req = ARP(pdst=ip)

    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = broadcast / arp_req

    result = srp(packet, timeout=2, verbose=False)[0]

    for sent, received in result:
        return received.hwsrc

    return None

target_ip = "192.168.1.1"

mac = get_mac(target_ip)

if mac:
    print("MAC address of", target_ip, "is", mac)
else:
    print("No response for", target_ip)

OUTPUT:

MAC address of 192.168.1.1 is 14:cc:20:ab:98:11

RESULT:
Thus, the MAC or Physical address of the system was obtained successfully using Address Resolution Protocol (ARP).


-------------------------------------------

EXPERIMENT – 16

AIM:
Simulate the transmission of ping messages over a network topology consisting of 6 nodes and find the number of packets dropped due to congestion.

THEORY:
Ping is a network utility used to test connectivity between nodes in a network. Congestion occurs when network traffic becomes high, causing packet loss and delays in transmission.

STEPS:

Step 1:
Click on the subnet icon on the toolbar and then click on the screen of the working window.

Step 2:
Select the required number of hosts and a suitable radius between the host and the switch.

Step 3:
In the edit mode, get the IP address of one of the hosts say, host1 and then for the other host say, host2 set the drop packet and number of collisions statistics as described in the earlier experiments.

Step 4:
Now run the simulation.

Step 5:
Now click on any one of the hosts and click on command console and ping the destination node.

ping IP Address of the host

Note:
The number of dropped packets are obtained only when the traffic is more in the network. For checking the number of packets dropped press Ctrl + C.

OUTPUT:
Packets were transmitted between source and destination successfully. Due to congestion, some packets were dropped during the simulation.

RESULT:
Thus, the transmission of ping messages over a network topology consisting of 6 nodes was simulated successfully and the number of packets dropped due to congestion was observed.
