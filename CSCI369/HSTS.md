### .
- HTTP Strict Transport Security
- A rule that instructs the browser to always request in [[HTTPS]] 
### Process
- First request sent as http (http://web.com)
- The web server returns a **302 redirection directive** (request a https redirect)
- A second request is sent as https (https://web.com)
- the website is saved to be https in a table
#### Issue
- On first load, [[SSL strip]] can still happen as the browser does not know yet that the website is in https
#### Fix
- HSTS preloading
	- A list of KNOWN websites that must be accessed in https.
	- Trustworthy websites can register to be on this list
>[!note]-
>This is why dubious sites should always be visited in https as they might not be in the preload list

