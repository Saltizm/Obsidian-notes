---
index: true
course: "CSIT302"
chapter: "Security foundations"
concept: "DDOS"
---

# DDOS

A **Distributed Denial-of-Service (DDoS)** attack floods a target (website/server) with massive fake traffic, making it **crash or slow down** for real users. ^9eade7

### How It Works

#### Botnet army
- Hackers control thousands of infected devices (bots).
- often [[IoT]] devices

#### Attack command
- The hacker (**"botmaster"**) orders all bots to **send requests** to the target at once
-  **Result**
    - The server **overloads and crashes** (denying service to real users).
    - Sometimes used as a **distraction** while hackers steal data.
        


---

> [!example]- Example
>
> - **Mirai Botnet (2016)** – Hijacked IoT devices to take down major sites (Twitter, Netflix).
> - **GitHub (2018)** – Hit with **1.35 Tbps** traffic (one of the biggest DDoS attacks ever).
>
> ---
>
### How to Prevent DDoS Attacks
**Use DDoS Protection Services** – Cloudflare, AWS Shield.  
**Monitor Traffic** – Detect abnormal spikes early.  
**Update Devices** – Prevent them from becoming bots.  
**Limit Connections** – Restrict how many requests a server accepts.

### How to keep a DDoS attack going
- [[Domain Generation Algorithm]] - Resilient command and control servers 