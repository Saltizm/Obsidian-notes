Code division multiplexing is continuous transmission of all devices on one channel simultaneously.

Three different mobile devices use the following codes:
•Mobile A: 11110000
•Mobile B: 10101010
•Mobile C: 00110011

when converted to values it would be:
- Mobile A: ==+1== ==+1== ==+1== ==+1== -1 -1 -1 -1
- Mobile B: ==+1== -1 ==+1== -1 ==+1== -1 ==+1== -1
- Mobile C: -1 -1 ==+1== ==+1== -1 -1 ==+1== ==+1==

When transferring:
- 1 bit: send the code unchanged
- 0 bit: send the inverse of the code
- rest: no data sent

so if mobile A wanted to transfer a 0bit:
==+1== ==+1== ==+1== ==+1== -1 -1 -1 -1   >>>   -1 -1 -1 -1 ==+1== ==+1== ==+1== ==+1==

if mobile A wanted to transfer a 1bit:
==+1== ==+1== ==+1== ==+1== -1 -1 -1 -1   >>>   ==+1== ==+1== ==+1== ==+1== -1 -1 -1 -1

lets assume:
mobile A sends a **1bit**
mobile B sends a **0bit**
mobile C sends a **1bit**

With all the codes added up the result will be:
-1, +1,  +1, +3, -3, -1, -1, +1



by decoding with mobile A's code:
-1, +1,  +1, +3, -3, -1, -1, +1
becomes
-1, +1, +1, +3, +3, +1, +1, -1

And the sum of the values above is +8.
Since the product is positive, the bit set is 1.


