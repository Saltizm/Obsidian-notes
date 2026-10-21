---
index: true
course: "CSIT 127"
chapter: "Signals and transmission media"
concept: "Time division multiplexing( TDM )"
---

# Time division multiplexing( TDM )

Time division multiplexing send several [[Signal|signals]] in [[round robin order]].
For one period of time there will be several time slot for each device to send their [[Signal]].

Then each device will keep transferring data until they have exhausted all the [[data]] they wanted to transfer.

## Synchronous
Each time slot is reserved from **on device only**. 

![[Synchronous TDM.png]]

However, the drawback of this approach is that there is redundancy.
When on device has finish transferring [[Signal]]. The freed up time slot **will not be occupied**.

used in:
- T1 telephone
- SONET telephone

## Statistical
Each time slot is **Dynamically Allocated** 

empty time slots are taken up by:
- devices that are still transferring [[Signal|signals]].
- devices transferring at a faster speed

![[statTDM.PNG]]
