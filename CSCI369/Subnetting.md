### . 
- Separating a network into smaller networks called [[VLAN]] 
- A portion of bits in the [[IP]] is used to define subnet size (Network bit)
- Subnet prefix = IP ^(AND) ToSubnetMask(Network bit) 

### CIDR
![[CIDR]]
### Reserved IP addresses

| IP addr    | Purpose                  |
| ---------- | ------------------------ |
| 10.0.0.0   | network addr             |
| 10.0.0.1   | internal comm ( router ) |
| 10.0.0.2   | DNS                      |
| 10.0.0.3   |                          |
| 10.0.0.225 | Broadcast                |
