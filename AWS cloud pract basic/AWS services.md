---
index: true
course: "AWS cloud pract basic"
chapter: "AWS cloud services"
concept: "AWS services"
---

# AWS services

- base services
	- Containers 
		- ECS - Elastic Container Service
		- EKS - Elastic Kubernetes Service
	- Compute:
		- EC2 - Elastic Compute Cloud (server based)
		- Lambda - Serverless compute 
		- Fargate - Serverless Container compute
		- Outpost - Private Cloud
	- Database (data storage systems)
		- OLTP
			- Amazon RDS - rdd based distrubuted storage system 
			- Aurora -SQL like
			- DynamoDB - noSQL like
		- OLAP
			- Redshift - data warehouse (OLAP)
	- Storage (physical persistent memory)
		- S3 - Simple Storage Service
		- S3 Glacier - Long term persistent storage
		- EFS/EBS - 
			- F(file) shared file system. 
			- B(beanstalk) local based.
	- Network
		- VPC (iaas)
		- Lightsail (saas)
		- Route 53
		- CloudFront
		- Elastic Load balancing
	- Virtualisation
		- VMware Cloud on AWS
- IDE
	- Cloud9
- Metrics and eval
	- Cloudwatch
	- ...
- Cost management
	- ...

### Web service
Uses standardise format XML, JSON to handle request
to and fro for an API

platforms
- cli
- gui (managment console)
- sdk
### Cloud Adaptation Framework
![[Pasted image 20260326215858.png]]
Left - Business perspective
Right - Technical perspective

Business
- Cloud service actually instrumental to goal
- Aligns with business needs
People
- People are onboard with cloud implementation
- can adapt and utilise new infrastructure (continuous learning)
Governance
- Manage changes
- Minimise transformation risk
- Maximise organisation benefits (profits)

---
Platform
- implementation has to be understandable at a human level and be thoroughly described.
Security
- implementation follow the CIA triad
- confidentiality
- Integrity
- Authority
Operations
- Define how business is operated across different time periods

---
### Module 1 : Cloud Concepts

- Computing **on demand** via the internet with **pay as you go pricing**
#### Hardware
- Require:
	- Space
	- Staff
	- Physical security 
	- planning
		- Guessing theoretical maximum compute peak to provision capacity
	- capital
- Long hardware procurement cycle (take time to buy parts)
#### Software
- flexible
- Cost effective due to economy of scale
- Ease of use (some products handles infrastructure)
- on demand
#### Cloud types
Hybrid - Cloud + On premise
On premise - Private cloud, self hosted and distributed through vpn and tunnels
Cloud - resources accessed through the internet
![[Pasted image 20260329223034.png]]
DAS - direct attach storage
NAS - network attach storage
SAN - storage area network

#### Cloud advantages
- Massive economies of scale
- Stop guessing capacity
- Speed and agility
- Stop spending money on running and maintaining data centers
- Go global in minutes
---
### Module 2 : Cloud Economics and Billing
cost drivers
- Compute
- Storage
- Data transfer
#### RI (reserved instances)
- AURI - All upfront
	- Largest discount
- PURI - partial upfront
	- Lower discount
- NURI - no upfront
	- Lowest discount
- On demand
	- NO discount 