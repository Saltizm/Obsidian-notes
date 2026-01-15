- [[IaaS]] (EC2)
- [[PaaS]] (Lambda)
- [[SaaS]](beanstalk)
- Pay as you go model
 - Lower initial capital investment

### Cloud Adaptation Framework
#### Business
- Aligned with business need
	- reducing cost 
#### People
#### Governance
#### Platform
#### Security
#### Operations

![[AWS ou statistics.png|600]]
### Pricing compute
- Outbound transfer 
- Compute 
- Storage
### Number of servers
38 region
120 availability

Auto scale - Overflow onto other server when load is too high on it

Load balancing - Split load equally amongst servers 

IAM

[[IAM policy]] is granted to 
IAM roles which are given to either
IAM group
or
IAM users - > can be granted to either individuals or their programs

### AWS route 53
- route 53 - most connected highway in US
- AWS DNS server 
EC2 - server for compute (iaas)
Lambda - serverless compute (saas)

### Storage

![[storage hiereachy drawing|500]]

#### EC2
- nest product
#### Onezone 
- single server storage
- no redundancy 
#### S3
- non nest storage
- can be configured to be a static website
### Database
#### Amazon RDS 
- Structured db
#### Amazon redshift
- data warehouse
- structured
- Use case - data analytics 
### DynamoDB
- nosql db
### Pillars 
#### Operational excellence pillar
- aligns with business values
- 
#### Security pillar
- PMCM (prevention/corrective)
- [[CIA]]
#### Reliability pillar
- UAT 
- PAT
#### Performance efficiency/Cost optimisation pillar
- using performance data to determine optimal amount of resources required 
- MTTF - uptime
- MTTR - downtime + repair 
- MTBR - avg time to fail
![[x9s chart.PNG]]