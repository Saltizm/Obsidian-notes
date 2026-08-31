### Outline
- Tools used
	- nmap
	- hydra
The assignment has given us the format of the voucher code to be cracked. Therefore, a dictionary attack will be performed to reduce enum time.

### Method
- nmap scan the server for open ports 
- ![[Pasted image 20260813053102.png]]
- get the hash using the following command
	- echo '8576658' | nc -u 192.168.56.4 12499
- ![[Pasted image 20260813051114.png]]
- I saved the hash in a file name hash.txt
- using hashcat cpu optimsation i used it to find and match the voucher using the following command
- LC_ALL=C LANG=C crunch 11 11 -t '@@8576658^^' 2>/dev/null | hashcat -m 0 e5d6024fe1ec9b6f9733654ece8f5f3b![[Pasted image 20260813053009.png]]
- dumped the cracked hash using the following command
	- hashcat -m 0 e5d6024fe1ec9b6f9733654ece8f5f3b --show
- ![[Pasted image 20260813053202.png]]
- appears the output is in hex. lets fix that
- ![[Pasted image 20260813053432.png]]
- Final answer
	- nv8576658&:

### Summary
The cpu and gpu optimisation was vastly superior to a simple bash script i tried first. Although both got the answer, using netcat was cleaner. No further comments besides issues with setlocale() when using crunch with special characters. Otherwise, a very fun exercise.