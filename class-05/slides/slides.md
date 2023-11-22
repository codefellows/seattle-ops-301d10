<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 05

NOTE:


---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 05 - VPN Tunnel
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Virtual Private Network
  - Internet Protocol Security
- Demo

---

<!-- .element class="split-screen-with-title" -->

## Course Overview

<div>

<div align="left" style="font-size: 35px">

**Modules:**
- &shy;<!-- .element style="color: red;" -->**Module 1** Networking Tools, Concepts, and Fundamentals
- **Module 2** Network Infrastructure Design and Implementation
- **Module 3** Server Administration, Active Directory, and User Management
- **Module 4** Project

</div>

<div>

![Image](/ops-301-guide/curriculum/class-02/slides/assets/0_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->

## Module 1 - Networking Tools, Concepts, and Fundamentals

<div>

<div align="left" style="font-size: 40px">

**Class 01** Network Traffic Analysis

**Class 02** Network Enumeration

**Class 03** Network Segmentation

**Class 04** Routing

&shy;<!-- .element style="color: red;" -->**Class 05** VPN Tunnel


</div>

<div>

![Image](/ops-301-guide/curriculum/class-02/slides/assets/0_02.png)
<!-- .element style="width: 70%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->


## Module 1 Challenges: Bash

<div>

<div align="left" style="font-size: 50px">


**Class 01** N/A

**Class 02** Append + Date and Time

**Class 03** File Permissions

**Class 04** Conditionals in Menu Systems

&shy;<!-- .element style="color: red;" -->**Class 05** Clearing Logs

</div>

<div>

![Image](/ops-301-guide/curriculum/class-02/slides/assets/0_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 05 - VPN Tunnel
- Course Overview
- Warmup <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Review
- Ops Challenge
- Lecture:
  - Virtual Private Network
  - Internet Protocol Security
- Demo

---

<!-- .element class="main-title" -->

# Warmup

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 05 - VPN Tunnel
- Course Overview
- Warmup
- Review <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Ops Challenge
- Lecture:
  - Virtual Private Network
  - Internet Protocol Security
- Demo

---

<!-- .element class="main-title" -->
# Review:

# Network Design &

# Routing Protocols


NOTE:
Let's review some key concepts from the previous class.

---

<!-- .element class="split-screen " -->
<div>

# Network Design

- Generally performed by network designers, engineers and IT administrators before the implementation of a network infrastructure.
- Key aspects of network design:
  - Network requirements
  - Network topology
  - Hardware and software selection

</div>

> "Network design refers to the planning of the implementation of a computer network infrastructure.”
![Image](/ops-301-guide/curriculum/class-04/slides/assets/11_0.png)

NOTE:

- The following are some of the key aspects of network design:
  - Network requirements
    - The first step in network design is to identify the requirements of the network. This includes the number of users, the types of applications that will be used, the amount of data that will be transmitted, and the level of security required.
  - Network topology
    - The network topology is the physical layout of the network. There are many different network topologies, each with its own advantages and disadvantages. The best topology for a particular network will depend on the requirements of the network.
  - Hardware and software selection
    - The next step is to select the appropriate hardware and software for the network. This includes routers, switches, firewalls, servers, and workstations. The hardware and software must be compatible with each other and must meet the requirements of the network.

Source: mcqquestions

---

<!-- .element class="split-screen " -->
<div>

# Network Topologies

- How we choose to connect the devices determines the topology type:
  - Logical topology
    - Two main types of logical topologies:
      - Broadcast
      - Point-to-point
  - Physical topology
    - Cabling physically exists as depicted


</div>

> A network topology is the arrangement of the elements that form a communication network.
![Image](/ops-301-guide/curriculum/class-04/slides/assets/12_0.png)

NOTE:
- Logical
  - a logical topology refers to the way that data flows through the network, regardless of the physical layout of the devices.
  - There are two main types of logical topologies:
    - Broadcast: In a broadcast topology, all devices on the network can see all of the traffic on the network. This is the simplest type of logical topology, but it can also be the least efficient, as all devices must process all of the traffic, even if it is not intended for them.
    - Point-to-point: In a point-to-point topology, each device is only connected to one other device. This is the most efficient type of logical topology, as only the devices that are communicating with each other need to process the traffic.

- Physical
  - is when the cabling is literally as depicted
  - a physical network topology refers to the actual physical layout of the network devices and how they are connected to each other.
  - The physical topology is important for determining factors such as performance, scalability, and fault tolerance.
  - There are many different types of physical topologies.

- Note that CompTIA considers VLAN a form of virtual segmentation, not physical.
  > "In a virtually segmented network, VLANs identify separate segments. An admin may configure the VLANs in such a way that it achieves virtual system isolation.
  > In a physically segmented network, switches connect segments. The switches may connect in such a way that it achieves system isolation. This method is an approach that results in an air gap." - The Official CompTIA CySA+ Student Guide (Exam CS0-002)
  > You'll need to know all six network topologies to pass CompTIA Network+. Check the corresponding exam objectives.

Source: mcqquestions

---

<!-- .element class="split-screen " -->
<div>

# Routing Protocols

- Distributed denial of service (DDoS) is an attack technique whereby multiple hosts overwhelm a web server with a flood of requests.
- Network routing is the process of choosing a path across one or more networks
  - In static routing you set a predefined single path to the destination.
    - Saved to the router
    - Takes precedence over dynamic routes


</div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/19_0.png)

NOTE:
- Distributed Denial of Service (DDoS) is a cyber attack that involves overloading a system or network with a flood of traffic. This can cause the system or network to crash, making it unavailable to legitimate users.
  - In some cases, DDoS attacks can impact routing protocols. For instance, if a DDoS attack targets specific network segments or routers, it might result in routing instability or changes as routers attempt to reroute traffic to avoid affected areas.
- Network routing is the process of determining the best path for data packets to travel from their source to their destination. It is a critical function in any network, as it ensures that data is delivered efficiently and reliably.
  - Static routing is a type of routing in which the router is manually configured with a list of routes to the destinations. This is typically done in small networks, where the topology of the network does not change frequently.

##  Who is Cloudflare and how does their solution work?

Cloudflare is a content delivery network (CDN) and DDoS mitigation service. It provides a number of features to protect websites and applications from DDoS attacks, including:

  - Edge caching: Cloudflare caches static content, such as images and JavaScript files, at its edge nodes. This reduces the amount of traffic that needs to be sent to the origin server, which can help to mitigate DDoS attacks.
  - DDoS mitigation: Cloudflare uses a variety of techniques to mitigate DDoS attacks, including rate limiting, blackholing, and scrubbing.
  - Web application firewall (WAF): Cloudflare's WAF can be used to block malicious traffic, such as bots and scripts.
  - SSL/TLS offloading: Cloudflare can be used to offload SSL/TLS traffic from the origin server. This can help to improve performance and security.

Cloudflare's DDoS mitigation solution works by using its global network of edge nodes to detect and mitigate DDoS attacks. When an attack is detected, Cloudflare can take a number of measures to mitigate the attack, such as:

  - Rate limiting: Cloudflare can limit the rate at which traffic is sent to the origin server. This can help to prevent the origin server from being overwhelmed.
  - Blackholing: Cloudflare can block traffic from known malicious sources. This can help to prevent the attack from reaching the origin server.
  - Scrubbing: Cloudflare can scan traffic for malicious content and remove it before it reaches the origin server.

Source: superuser

---

<!-- .element class="main-title" -->
# Review
## Lab 04: Routing


---

<!-- .element class="main-title" -->
# Review
## Challenge 04: Conditionals in Menu Systems


---

<!-- .element class="main-title" -->
# Virtual Private Networking

NOTE:
- Virtual Private Networking (VPN) is a critical technology widely employed in the modern digital landscape for enhancing security, safeguarding privacy, and expanding online access.
- By creating encrypted tunnels that shield data from unauthorized access and concealing users' true identities through IP address masking, VPNs are instrumental in protecting sensitive information, evading geo-restrictions, and fortifying the overall online experience.
- In an era marked by increasing cybersecurity threats and concerns over digital privacy, VPNs have become indispensable tools for both individuals and organizations striving to navigate the internet securely and anonymously.

---

<!-- .element class="split-screen " -->
<div>

# Virtual Private Networking

- A virtual private network (VPN) is a private network that is built over public infrastructure
  - Use encryption to maintain confidentiality of data in motion
- VPN use cases
  - Intersite connectivity
  - Securely access a private cloud
  - Confidentiality of data in motion
  - Defensive security
  - Offensive security


</div>

![Image](/ops-301-guide/curriculum/class-05/slides/assets/11_0.png)

NOTE:
A virtual private network (VPN) is a private network that is built over public infrastructure, utilizing encryption to maintain the confidentiality of data in motion.

VPNs serve various essential use cases, including:

**Intersite Connectivity:** VPNs enable secure communication and data exchange between different geographical locations or remote offices within an organization. This ensures that sensitive information remains protected while being transmitted over public networks.

**Securely Access a Private Cloud:** Organizations can use VPNs to securely access and interact with their private cloud infrastructure. This allows for the seamless transfer of data and applications while maintaining the integrity and security of the data in transit.

**Confidentiality of Data in Motion:** One of the primary purposes of VPNs is to ensure the confidentiality of data while it is in transit over the internet or other public networks. By encrypting data, VPNs safeguard it from potential eavesdropping and interception by unauthorized parties.

**Defensive Security:** VPNs are an essential tool for bolstering an organization's defensive security posture. They establish a secure communication channel for remote employees, protecting sensitive corporate data from potential cyber threats and ensuring that remote access is secure.

**Offensive Security:** In the realm of offensive security and penetration testing, VPNs are often used to conceal the origin of network traffic. This is particularly useful for security professionals and ethical hackers who need to hide their identity and location while conducting security assessments.


OLD NOTES:
Intersite connectivity
- Securely access a private cloud
Confidentiality
- Confidentiality is one part of the CIA Triad.
- The CIA Triad consists of Confidentiality, Integrity, and Availability of information.
- Most information security processes facilitate one of these three pillars of the Triad.
Defensive security
- Extending your private network geographically
Offensive security
- Evading detection
  - A VPN can be used aggressively to evade IDS/IPS detection by scrambling the traffic you're sending into the victim network.

David's Story: For one organization I worked for, we needed access to an AWS private cloud which hosted a critical piece of software used by many parts of the company. In order to establish secure access, we deployed a site-to-site VPN tunnel from our router to AWS. To forbid unauthorized access to the system, it was possible to restrict the AWS cloud server to users of the VPN tunnel. VPN tunnel was connected to the on-site router. Therefore, for an employee to work from home, they'd need to VPN into the on-site VPN server first. From there, they could hop over to AWS. What always amazed me is how many options there are in configuring a VPN. It felt overwhelming the first time! Once I understood encryption better, it made more sense why VPN tunnels always had a speed bottleneck to them.

Key takeaways:

- VPN Tunnels have LOTS of options, don't be intimidated by the complexity
- VPN Tunnels are great for establishing secure site-to-site communications
- VPN Tunnels can be a bottleneck, because each end must encrypt or decrypt traffic

Source: Wikimedia Commons

---

<!-- .element class="split-screen " -->
<div>

# Virtual Private Networking

- What traffic gets encrypted?
  - Traffic in the tunnel between VPN client and VPN server gets encrypted
  - Traffic extending beyond the VPN server (a “proxy”) does not get encrypted
- MITM (man in the middle) attack would succeed against the latter, not the former

</div>

![Image](/ops-301-guide/curriculum/class-05/slides/assets/12_0.png)

NOTE:
When using a Virtual Private Network (VPN), the traffic that gets encrypted primarily consists of:

**Traffic in the Tunnel:** The data that travels between the VPN client (your device) and the VPN server is encrypted within the secure tunnel. This includes all data transmitted between your device and the VPN server, such as web browsing, file downloads, emails, and application data.

However, it's important to note:

2. **Traffic Beyond the VPN Server (Proxy):** Traffic that extends beyond the VPN server, once it exits the VPN server and continues its journey to its final destination on the internet, does not remain encrypted by the VPN. At this point, it behaves like regular internet traffic.

Regarding Man-in-the-Middle (MITM) attacks:

- A MITM attack is more likely to succeed against the traffic that extends beyond the VPN server (the proxy), as it is no longer encrypted and can potentially be intercepted or tampered with by an attacker who is positioned between the VPN server and the final destination.

- In contrast, the traffic within the tunnel between the VPN client and server is encrypted end-to-end, making it much more resistant to MITM attacks. To decrypt this traffic, an attacker would need to compromise the encryption keys used in the VPN connection, which is a challenging task if strong encryption methods are employed.

In essence, VPNs provide a secure and encrypted pathway for data between your device and the VPN server. Once data exits the VPN server and continues its journey to its final destination on the internet, it is no longer protected by the VPN's encryption, potentially leaving it vulnerable to interception or manipulation by malicious actors. Therefore, it's crucial to ensure that the websites and services you use beyond the VPN server also employ encryption, especially for sensitive information like login credentials and financial transactions.

OLD NOTES:
Do VPN services actually conceal my activities?
- Who do you trust more, your ISP or the VPN provider?
- Activities over VPN can still be traced by a determined investigator with adequate time/resources, especially if they can subpoena the VPN provider for data, like activity logs. VPN servers are ultimately proxies, and proxies can still point back to their originating IPs.

Source: Wikimedia Commons

---

<!-- .element class="split-screen " -->
<div>

# Virtual Private Networking

- Client-server VPN is what most consumers think of when VPN is used in products like NordVPN, ExpressVPN, etc.
  - SSL encryption
  - Endpoints (PCs) toggle the VPN service on and off
  - Data routes through a proxy server (the VPN server) before interacting with the internet, concealing source IP

</div>

![Image](/ops-301-guide/curriculum/class-05/slides/assets/13_0.png)

NOTE:
A client-server VPN, such as those offered by popular VPN services like NordVPN and ExpressVPN, is the most commonly used type of VPN by consumers.

Key characteristics and features of client-server VPNs:

**SSL Encryption:** Client-server VPNs typically use SSL (Secure Sockets Layer) encryption or its successor, TLS (Transport Layer Security), to secure the communication between the client (user's device) and the server (VPN provider's server). This encryption ensures that data transmitted between the two endpoints remains confidential and secure.

**Toggle VPN Service:** Users have the flexibility to toggle the VPN service on and off as needed. This allows users to choose when to establish a secure connection through the VPN and when to use their regular, unencrypted internet connection.

**Data Routing:** When the VPN service is active, data from the client device is routed through a proxy server operated by the VPN provider (the VPN server) before interacting with the internet. This routing process conceals the client's source IP address, making it appear as if the traffic is originating from the VPN server's location. This helps protect the user's identity and location.

**Concealing Source IP:** As mentioned, the VPN server acts as an intermediary between the client and the internet. This conceals the client's source IP address from websites and online services, enhancing privacy and allowing users to access region-restricted content by appearing as if they are browsing from the VPN server's location.

**Secure Browsing:** By encrypting internet traffic and routing it through a VPN server, client-server VPNs provide an additional layer of security, especially when using public Wi-Fi networks. This helps protect users from potential eavesdropping, data interception, and cyber threats.

**Server Selection:** Most client-server VPNs offer a choice of VPN server locations in various countries. Users can select a server location to optimize connection speed or access content that may be geo-restricted in specific regions.

Source: Wikimedia Commons

---

<!-- .element class="split-screen-with-title" -->

# Virtual Private Networking

<div>

<div>

  - Computer resources can be shared over this tunnel as if they were on the same LAN.
  - Tunnelling uses a series of "handshakes" to establish the persistent connection
  - Any disagreements during these handshakes, such as disagreement over a shared passkey, will sever the connection or prevent it from taking place.

</div>

<div>

> Site-to-site VPN tunneling allows two VPN-capable routers to agree upon encryption standards and establish a private network connection, or VPN tunnel.
![Image](/ops-301-guide/curriculum/class-05/slides/assets/14_0.png)

</div>

</div>

NOTE:
Site-to-site VPN tunneling is a technology that enables two VPN-capable routers to establish a secure and encrypted connection, creating a virtual private network (VPN) tunnel between two geographically separate locations.

Key points about site-to-site VPN tunneling:

**Private Network Connection:** Site-to-site VPN tunneling allows two distant networks to connect securely over the internet or another public network. This connection is established using encryption standards and protocols agreed upon by both routers, creating a private and secure channel for data transmission.

**Resource Sharing:** Once the VPN tunnel is established, computer resources and devices on both networks can communicate as if they were on the same local area network (LAN). This means that devices from one site can access resources at the other site, such as shared files, printers, and servers, seamlessly and securely.

**Handshakes:** The establishment of a site-to-site VPN tunnel involves a series of negotiation steps or "handshakes" between the two VPN-capable routers. These handshakes are used to set up the encryption parameters, establish authentication methods, and agree on other connection parameters.

**Persistent Connection:** Site-to-site VPN tunnels are designed to be persistent, maintaining a continuous and stable connection between the two sites. This ensures that data can flow between the sites securely and without interruption.

**Disagreements and Connection Issues:** During the handshaking process, if there are any disagreements or failures in the negotiation, such as a mismatched shared passkey or authentication issues, the connection may be severed, or it may fail to establish in the first place. These security mechanisms are in place to ensure that only authorized parties can establish the VPN tunnel.

> Why is your activity traceable on VPN? While it does make it harder to track your original IP, using a VPN server is like using a proxy, except now you're wrapping the connection with encryption. Your activity still has an origin and a destination. Determined entities (such as the government) can and will track down the source. Using a VPN service therefore does not equate to perfect privacy. However, it can be a wise layer of defense in a scenario like being forced to use open Wi-Fi.

Source: Wikimedia Commons

---

<!-- .element class="main-title" -->
# Internet Protocol Security


NOTE:
- Internet Protocol Security (IPsec) plays an important role in the realm of VPNs by serving as the foundation of secure and encrypted communication over the internet.
- Its importance lies in its ability to ensure the confidentiality, integrity, and authenticity of data in transit, making it an indispensable technology for safeguarding sensitive information, preserving privacy, and fortifying the overall cybersecurity posture of both individuals and organizations.
- In an era characterized by escalating digital threats, IPsec emerges as an essential component in establishing trust and security across the internet.

---

<!-- .element class="split-screen " -->
<div>

# Internet Protocol Security

- **Authentication & Encryption:** IPsec ensures trust and confidentiality by authenticating devices and encrypting data to thwart eavesdropping and tampering.

- **Packet Security:**  In Site-to-site VPNs, IPsec adds security layers, encrypting data and placing it in a new IP header for secure routing.

- **IPsec Headers:** AH or ESP headers sit between the IP header and upper-layer protocol, providing authentication, integrity, and optional encryption.

</div>

> Site-to-site VPN tunnels use Internet Protocol Security (IPsec), a secure network protocol suite that authenticates and encrypts data packets to provide secure encrypted communication between two ends of the tunnel
![Image](/ops-301-guide/curriculum/class-05/slides/assets/16_0.png)

NOTE:
Site-to-site VPN tunnels rely on Internet Protocol Security (IPsec), which is a robust network protocol suite specifically designed for establishing secure communication channels.

Here's how IPsec works:

**Authentication and Encryption:** IPsec performs two vital functions in the context of VPNs. First, it authenticates the identities of the devices or routers at both ends of the tunnel, ensuring that they are legitimate and trusted. Second, it encrypts the data packets, thereby safeguarding their confidentiality. This dual-layered security mechanism guarantees that data exchanged between the two ends remains secure from eavesdropping and tampering.

**Packet Wrapping:** When a device sends data over a Site-to-site VPN tunnel, IPsec comes into play. It wraps the original data packet with additional layers of security. This involves taking the original packet, encrypting its contents, and encapsulating it within a new IP header. The new IP header contains the information needed to route the packet to its destination via the VPN tunnel.

**IPsec Header:** The IPsec header can take one of two forms: Authentication Header (AH) or Encapsulating Security Payload (ESP) header. These headers are inserted between the standard IP header and the upper-layer protocol (e.g., TCP, UDP) data. AH provides authentication and integrity verification for the packet, while ESP not only provides these functions but also encrypts the data payload for confidentiality.

IPsec plays a crucial role in Site-to-site VPN tunnels by combining authentication and encryption to ensure the private exchange of data between two endpoints. By encapsulating, encrypting data packets and authenticating, IPsec establishes a trustworthy communication channel, making it an essential component of private network connections over the internet.

Source: Firewall.cx

---

<!-- .element class="title-and-text " -->

# Internet Protocol Security

<div>

- What are the key elements of an IPsec tunnel?
  - Authentication Header (AH)
    - Ensures the integrity and authenticity of a VPN packet
  - Encapsulating Security Protocol (ESP)
    - Encrypts the VPN packets
  - Security Association (SA)
    - Negotiates encryption keys and algorithms
    - Consists of several protocols such as IKE (Internet Key Exchange) version 1 and 2

</div>

NOTE:
## Key Elements of an IPsec Tunnel:

**Authentication Header (AH):**
  - AH ensures the integrity and authenticity of a VPN packet.
  - It provides data packet authentication, making sure that the data hasn't been tampered with during transmission.

**Encapsulating Security Protocol (ESP):**
  - ESP encrypts the VPN packets.
  - It ensures the confidentiality of the data being transmitted by encrypting its contents.

**Security Association (SA):**
  - SA is responsible for negotiating encryption keys and algorithms between the communicating devices.
  - It consists of several protocols, including IKE (Internet Key Exchange) versions 1 and 2, which facilitate the secure establishment of keys for IPsec communication. IKE helps in setting up the initial parameters needed for secure communication and key exchange between devices involved in the IPsec tunnel.

OLD  NOTES:

- What are the steps to establish an IPSec connection?
  - Key Exchange - needed for encryption
  - Packet Headers and Trailers - IPSec adds headers and trailers containing authentication and encryption information.
  - Authentication - like a stamp of authenticity on the packets
  - Encryption - IPSec encrypts the payload within each packet
  - Transmission - Packets travel across networks using UDP
  - Decryption - At the other end, packets are decrypted and data can be used by applications

---

<!-- .element class="title-and-text " -->

# Internet Protocol Security

<div>

- What are the steps to establish an IPSec connection?
  - Key Exchange - needed for encryption
  - Packet Headers and Trailers - IPSec adds headers and trailers containing authentication and encryption information.
  - Authentication - like a stamp of authenticity on the packets
  - Encryption - IPSec encrypts the payload within each packet
  - Transmission - Packets travel across networks using UDP
  - Decryption - At the other end, packets are decrypted and data can be used by applications

</div>

NOTE:
## Steps to Establish an IPSec Connection:

**Key Exchange:** The initial step involves the exchange of cryptographic keys between the two devices (or peers) that wish to establish a secure IPSec connection. This exchange is necessary for subsequent encryption and authentication processes.

**Packet Headers and Trailers:** IPSec adds specialized headers and trailers to the data packets being transmitted. These headers and trailers contain information related to authentication, encryption, and other security parameters. They serve to protect the integrity and authenticity of the data.

**Authentication:** Authentication involves verifying the legitimacy of the data packets. IPSec adds a form of "stamp of authenticity" to each packet, ensuring that they have not been altered or tampered with during transmission.

**Encryption:** IPSec encrypts the payload within each data packet, making the data unreadable to unauthorized parties. This encryption ensures the confidentiality of the information being transmitted.

**Transmission:** The securely encapsulated and encrypted packets are transmitted across the network. IPSec typically uses the User Datagram Protocol (UDP) or another appropriate transport protocol to facilitate the transfer of these packets.

**Decryption:** At the receiving end, the IPSec-enabled device decrypts the incoming packets, restoring the original data payload. Once decrypted, the data can be used by the intended applications securely.

---

<!-- .element class="title-and-text" -->
<div>

# Confidentiality

- **DES (Data Encryption Standard)**
  - Developed in 1977 at IBM, DES is insecure due to its short 56-bit key size.
- **3DES (Triple Data Encryption Standard)**
  - This symmetric key block cipher applies the DES algorithm three times to each data block. The 56-bit key of DES is no longer considered secure.
- **SEAL (Software Optimized Encryption Algorithm)**
  - Developed in 1997 by IBM, it's a stream cipher with a 32-bit word size, widely adopted for drive encryption.
- **AES (Advanced Encryption Standard)**
  - Established in 2001 by NIST, it supports key lengths of 128, 192, and 256 bits and is widely used, including by the US government.

</div>

NOTE:
## Confidentiality
Cryptographic algorithms used for data encryption are mathematical techniques that transform plaintext (unencrypted data) into ciphertext (encrypted data) to protect the confidentiality, integrity, and authenticity of information during transmission or storage.

DES, 3DES, SEAL, and AES are all cryptographic algorithms used for symmetric data encryption. In symmetric encryption, the same secret key is used for both encryption and decryption. It's efficient but requires a secure method for key distribution.

- **DES (Data Encryption Standard)**
  - Developed in the early 1977 at IBM.
  - DES is insecure due to the relatively short 56-bit key size, making it vulnerable to brute-force attacks.

- **3DES (Triple Data Encryption Standard)**
  - A symmetric key block cipher.
  - 3DES applies the DES cipher algorithm three times to each data block, significantly improving security compared to DES.
  - Despite improved security, 3DES has become less favored due to its slow speed and the availability of more advanced encryption algorithms.

- **SEAL (Software Optimized Encryption Algorithm)**
  - The current version of SEAL was developed in 1997 by IBM.
  - SEAL is a stream cipher with a 32-bit word size.
  - It found adoption in drive encryption applications where it performed efficiently.

- **AES (Advanced Encryption Standard)**
  - Developed in 2001 by the National Institute of Standards and Technology (NIST).
  - AES offers key lengths of 128, 192, and 256 bits, providing a high level of security.
  - It gained widespread adoption and is considered a modern and secure encryption standard.
  - The U.S. government, in particular, adopted AES for its encryption needs, and it is widely used across various industries and applications for data confidentiality.

---

<!-- .element class="title-and-text" -->
<div>

# Integrity

- **MD5 (Message Digest Algorithm)**
  - Developed in 1991, cryptographically broken and unsuitable for further use. Widely exploited.
- **SHA (Secure Hash Algorithms)**
  - First developed in 1993, Version 0-3 exist. NSA highly involved in development of SHA2, version three developed in 2012

</div>

NOTE:
## Integrity
MD5 and SHA are cryptographic hash functions used to generate fixed-size hash values (digests) from variable-sized input data. A hash function is a mathematical function that takes an input and produces a unique output, typically a hexadecimal number. The output, known as the hash value or hash code, is a unique representation of the input.

Hashes are used to verify the integrity of data during transmission or storage. By comparing the hash value of the received data to the original hash value, one can detect any changes or corruption in the data.

- **MD5 (Message Digest Algorithm)**
  - Developed in 1991, MD5 is a cryptographic hash function.
  - Unfortunately, MD5 is cryptographically broken and considered unsuitable for further use due to vulnerabilities that can be exploited.
  - It is no longer recommended for security-sensitive applications.

- **SHA (Secure Hash Algorithms)**
  - Secure Hash Algorithms (SHA) are a family of cryptographic hash functions.
  - The first version, SHA-0, was developed in 1993 but had significant vulnerabilities.
  - SHA-1 was the next version and was widely used but is now considered weak due to vulnerabilities, and its use is being phased out.
  - SHA-2, developed by the National Security Agency (NSA), includes several variants with different hash lengths (e.g., SHA-256, SHA-512) and is considered secure.
  - SHA-3, developed in 2012, is the latest member of the SHA family and provides an additional option for secure hashing. It was designed through a public competition and is considered secure and resistant to known attacks.


---

<!-- .element class="title-and-text" -->
<div>

# Authentication

- PSK (Pre-Shared Key)
  - In cryptography, a shared secret is a piece of data, known only to the parties involved. The shared secret can be a password, a passphrase, a big number, or an array of randomly chosen bytes.
- RSA (Rivest Shamir Adleman)
  - The acronym RSA comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977. RSA is a public-key cryptosystem that is widely used for secure data transmission. In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret (private).

</div>

NOTE:
## Authentication

PSK and RSA are both cryptographic techniques used for authentication.

**PSK (Pre-Shared Key):**
  - In cryptography, a shared secret, such as a Pre-Shared Key (PSK), is a piece of data known only to the parties involved in communication.
  - PSK is a symmetric key authentication method, which means the same shared secret key is used for both encryption and decryption.
  - A PSK can be a password, a passphrase, a large number, or an array of randomly chosen bytes.
  - PSKs are used for authentication and establishing secure communication, especially in scenarios where a secret key is shared between two parties in advance.
  - PSK relies on the knowledge of a shared secret key to authenticate users or devices. The security depends on the secrecy and complexity of the key.

**RSA (Rivest Shamir Adleman):**
  - RSA is a widely used public-key cryptosystem introduced in 1977 by its inventors Ron Rivest, Adi Shamir, and Leonard Adleman, whose surnames form the acronym "RSA."
  - RSA is an asymmetric key encryption and authentication method, where a pair of keys (public and private) is used for encryption and decryption, and digital signatures.
  - The public key is openly shared, allowing anyone to encrypt data that can only be decrypted by the holder of the private key.
  - RSA is commonly employed for secure data transmission, digital signatures, and various cryptographic applications.
  - It uses the mathematical properties of prime numbers for security, making it computationally challenging to break encryption or forge digital signatures.

---

<!-- .element class="split-screen-with-title" -->

# Diffie-Hellman

> Methodology developed in 1976 used for secret communication in exchanging data over a public network.

<div>

<div>

- **DH1-DH5**
  - 768 bit/1024 bit/1536 bit, deprecated.
- **DH14**
  - 2048 bit, deprecated.
- **DH19**
  - 256 bit, elliptic curve

</div>

<div>

- **DH20**
  - 384 bit, elliptic curve
- **DH21**
  - 521 bit, elliptic curve
- **DH24**
  - 2048 bit with 256 prime order subgroup.
</div>

</div>


NOTE:
## Diffie-Hellman

Diffie-Hellman is a key exchange protocol used in cryptography to securely establish a shared secret between two parties over an untrusted network. The choice of key length or elliptic curve parameters determines the security level of the key exchange. As computing power increases, longer key lengths or stronger elliptic curves are often recommended to maintain security against potential attacks.

- **DH1-DH5:**
  - These represent various key lengths used in the original Diffie-Hellman (DH) key exchange protocol.
  - Key lengths include 768 bits, 1024 bits, and 1536 bits.
  - These key lengths are now considered deprecated due to their vulnerability to modern computational attacks.

- **DH14:**
  - DH14 represents a key length of 2048 bits in the Diffie-Hellman key exchange protocol.
  - This key length offers improved security compared to the deprecated shorter key lengths.

- **DH19:**
  - DH19 signifies a key length of 256 bits in elliptic curve Diffie-Hellman (ECDH) key exchange.
  - ECDH is based on elliptic curve cryptography, which offers strong security with shorter key lengths.

- **DH20:**
  - DH20 corresponds to a key length of 384 bits in elliptic curve Diffie-Hellman (ECDH) key exchange.
  - ECDH is known for its security and efficiency, even with shorter key lengths.

- **DH21:**
  - DH21 represents a key length of 521 bits in elliptic curve Diffie-Hellman (ECDH) key exchange.
  - ECDH with a 521-bit key provides a high level of security.

- **DH24:**
  - DH24 indicates a key length of 2048 bits with a 256-bit prime order subgroup in the Diffie-Hellman key exchange protocol.
  - This configuration combines the security of a 2048-bit key with the added security benefit of a 256-bit prime order subgroup, making it suitable for secure key exchange.


Share a real-world analogy
  > You are a spy and you need to send some important information to your headquarters. How do you prevent your enemies from getting ahold of the message? The easiest way is to prearrange whichever type of code and key you plan on using beforehand, or to do it over a sage communication channel. What happens if you couldn't arrange a code with your recipient beforehand? How can you securely exchange information with someone if you haven't had the opportunity to share the key ahead of time?

---

<!-- .element class="main-title" -->
# Demo


NOTE:

