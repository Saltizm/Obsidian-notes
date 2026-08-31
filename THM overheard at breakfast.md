### Overview
This room is an osint room that is based around a single image attached to the room. The techniques involved are:
- Google dorking
- Decryption 

To begin, the room gives us a single image called "conversation.png" that outlines a conversation between Ponzi and Lambo. This is the image in question.
![[conversation.png]]
As seen, the image led us to an email and a clue about what to do with the email.
I first googled for social media link pages/ business page creators that start with a G.
![[Pasted image 20260812233022.png]]
bingo! I search for ways to search gravatar pages through email and this is the first result
![[Pasted image 20260812233137.png]]
I entered the email "lambobytelotushotel@gmail.com" as shown in the image and clicked check.
![[Pasted image 20260812233255.png]]
![[Pasted image 20260812233319.png]]
Appears to have a profile page linked to this email. Lets see what's inside
![[Pasted image 20260812233412.png]]
Our next lead. A string of upper and lower case letters. Lets run it through hash-identifier to see if this is a hash.
![[Pasted image 20260812233502.png]]
Nothing. This leaves out only two options. It is either a red herring or something that has been converted to another format. Looking at the letters with numbers I guessed it might be base64.
![[Pasted image 20260812233815.png]]
The flag is found!

### Summary
This room is an easy one. Very straightforward and a nice refresher on basic osint tooling. 
