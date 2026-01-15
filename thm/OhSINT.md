Task1:
Could not for the life of me find the assignment image. Used https://exif.tools/ to get this result
![[Pasted image 20251216225537.png]]
Went to google maps to enter the GPS coordinates. This end up to be a red herring but it led to this result.
![[Pasted image 20251216225703.png]]
It appears to be a delivery service based in Chile. So i scanned through the images to find any relevant routes 
![[Pasted image 20251216225902.png]]![[Pasted image 20251216230002.png]]
![[Pasted image 20251216230327.png]]
(location for first screenshot)
![[Pasted image 20251216230551.png]]
Seems like a random address so I stopped looking onwards.
Moving on, I checked their websites https://position.cl/. There was nothing as well. Seems like an actual real life business.

Moving back to the meta data, I entered the copyright owner into google. 
![[Pasted image 20251216232655.png]]
Bingo, Woodflint's Twitter, blog github and an article talking about the room.
To avoid spoilers, I proceeded to the twitter.

Which leads to the flag 1: Cat. 
![[Pasted image 20251216233029.png]]
besides that there is also a tweet with a BSSID.

From my research I've gathered that a BSSID is the MAC of a WAP.

| Bssid                  | ssid                |
| ---------------------- | ------------------- |
| MAC address of the WAP | the name of the WAP |
I entered the BSSID into https://wigle.net/ and found a WAP named UnileverWIFI located in London.

Which solves flag 2: London.
and flag 3: UnileverWifi.

I checked the name of the wifi in google but found nothing besides the company so i moved on to the github.

the readme contains the email.

Solving flag 4: [OWoodflint@gmail.com](mailto:OWoodflint@gmail.com)

The final page and final flag took the longest but it was the most frustrating to solve. I scalped through the entire inspect looking for terms like "pass" "password" "//"(for comments) and found nothing. 

Then from an accidental highlight I found the final flag.

flag 5: pennYDr0pper.!

### Conclusion
The room was very fun, felt like a treasure hunt for clues. I have learn how to operate how to use tools like Exif and wiglet which opens up many possibilities. Previously I was limiting myself to using the "properties" tab for images on windows which hid information such as original file name, copyright and encoding processes, I am sure this would be useful for future image analysis.

Wiglet is an entirely new concept for me as I have never done network OSINT before. Being able to search for WAP with it's SSID or BSSID is very powerful. Some possible uses I can think of as of currently would be location triangulation from screenshots or common naming conventions. 

### Area for improvement
For the last part I could have downloaded the entire source code for the website to skim through using a simple script to save time. However, with the wordlist I would use I think it would not have helped much. Learning more about website structure I think would help drastically on spotting the stray hidden element in the website.