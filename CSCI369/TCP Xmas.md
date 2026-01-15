### .
- Sends non handshake flags (PSH, FIN, URG)
- Rarely used for mapping
- More for [[IDS and IPS]] diagnostics 
- Process
	- Sends FIN flag 
	- IF RST:
		- Port = CLOSED
	- IF no response:
		- FILTERED or Port = OPEN