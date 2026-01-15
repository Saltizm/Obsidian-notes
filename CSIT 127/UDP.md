User Datagram Protocol is a [[network|connectionless]] transfer protocol.

<h2>Function</h2>
- Streaming
- [[VoIP]]

### Features
- Has no Handshaking (packets are sent without establishing connection)
- Packets is unordered
- Packets are not replaced when lost

| pros               | con   |
| ------------------ | ----- |
| No overhead (Fast) | Lossy |


However, [[UDP]] is more ***lossy and insecure*** in terms of data transfer

Can also perform multiplexing of different applications over a single [[IP]]line using [[Time division multiplexing( TDM )]]