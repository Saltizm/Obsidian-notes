gcc -(tags) (-flag1 -flag2) -operation path/to path/from

### Privilege escalation 
1.
Prerequisite
LD_PRELOAD/LD_LIBRARY_PATH
program allowed to be sudo'd

create shared library for LD_PRELOAD with malicious payload
gcc -fPIC -nostartfiles (ignore other lib) -o path/to path/from

sudo LD_PRELOAD=path/to

run any program