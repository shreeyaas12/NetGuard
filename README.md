NetGuard — Enterprise Network Security Lab & Automated SOAR Pipeline
A professional-grade, segmented cybersecurity lab featuring real-time intrusion detection, custom Python-based automated incident response (SOAR), and enterprise security monitoring.

Architecture & Tech Stack
OS Environment: Ubuntu Server running inside VirtualBox with Host-Only network configuration .

Perimeter Security: iptables strict default-deny firewall ACLs and network segmentation.

Intrusion Detection System (IDS): Suricata deployed on primary packet-inspection interfaces for real-time threat logging.

Automated Incident Response (SOAR): Custom Python daemon (soar_responder.py) tailing logs and dynamically dropping malicious IPs into iptables.

Key Features & Implementation
1. Network Segmentation & Firewall ACLs
Configured strict default-deny policies on Linux iptables to isolate management and internal traffic zones. Established persistent firewall rules using netfilter-persistent to survive system reboots.

2. Real-Time Intrusion Detection (IDS)
Deployed and tuned Suricata IDS to inspect incoming network frames and log anomalous signatures to /var/log/suricata/fast.log.

3. Automated SOAR Defense Daemon
Developed a continuous Python background worker that parses Suricata logs using Regular Expressions. Automatically isolates threat actors by checking existing firewall rules and executing immediate iptables block injections, drastically reducing Mean Time to Respond (MTTR).

Project Structure
/etc/netguard/scripts/soar_responder.py -> Automated Python SOAR threat-blocking daemon
/var/log/suricata/fast.log -> Live IDS telemetry log source
