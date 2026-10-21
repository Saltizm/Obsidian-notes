---
index: true
course: "thm"
chapter: "TryHackMe practice"
concept: "Decryption"
---

# Decryption

### IDA 
- prologue - preparin stack for pushes
- epilogue - stack unwinding
- hard drives - deletion only **marks** a section as writable. Data can still be present after deletion
### Operator
- rsp - register stack
- rdx - register data
- rcx - counter register 
- rax - accumulator 
- rbx - base 
### Instructions
- mov - move to 
- sub - subtract from
- lea - load in bracket
- call - call (push + mov to address)
	- calling conventions:
		- window - fastcall
		- linux - system v amd64 abi
### DLL
- Flirt signature - maps names to standard library function during re
- imports/exports - functions called or exported has to have a name. This is found in dll/pe headers, lib file, header file
- modules - anything related to a process that imports/exports. (including script file when process is running)
### OOP
- name mangling - from overloading a function. This can be decoded to receive name
	- C linkage - stops name mangling. Prevents overloading 
		- command : extern C
- 