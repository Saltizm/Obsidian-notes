---
index: true
course: "CSIT 127"
chapter: "Signals and transmission media"
concept: "Pulse code modulation"
---

# Pulse code modulation

Pulse code modulation is a method to turn [[Analog]] [[signal]] into [[Digital]] [[signal]]s with high fidelity.

**deconstruction**
This method takes **snapshots** at regular time intervals in a [[Analog]] signal.
Then these **snapshots** are converted into [[Bits|binary values]].

**reconstruction**
using the **snapshots** that has been taken. The computer generates a [[Digital|step signal]] using a [[DAC]] and use a [[Low pass filter]]. to convert it into a [[Analog]] signal.

![[pulsecode.PNG|500]]

![[reconstructionLow.PNG|250]]![[reconstructionHigh.PNG|250]]

Low [[Sampling rate]] --> High [[Sampling rate]]
The [[Sampling rate]] should follow [[Nyquist theorem]].

[[Sampling rate]] determines the quality/detail of the [[signal]]
[[quantization level]] determines the [[bandwidth]] of the [[signal]]

Pulse code modulation is complex and therefore very computationally intensive. 
It is used for:
- Blu-ray 
- Compact Disk
- digital audio
- digital telephones