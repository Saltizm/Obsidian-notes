### Outline
Tools used:
- Python sockets
This is a mock demo of a reverse shell in action. The goal is to create two scripts. One listens on port 4445 to incoming requests and executes it, and one client script that sends the request.

### Method
- run server.py with the following command
	- python3 server.py
- then run revshell.py with the following command on another terminal
	- python3 revshell.py
- Following this. Enter the command 'ls'. After a few seconds the terminal should show the files in the current directory.
- ![[Pasted image 20260813012040.png]]
- ![[Pasted image 20260813012315.png]]

### Summary
The scripts work by continuously listening (server) and requesting (revshell client) with the server running the commands using subprocess.run(). The output is then sent back to the client.