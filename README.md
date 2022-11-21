# PortScanner
As I continue to try to level up my Python skills from beginner to intermediate, I continue to try to find projects that would be useful to my future cybersecurity career. This script was created with the help of a tutorial by H. Poston and I modfied the script to scan a list of addresses.<br>
<br>
<h3>The Process:</h3>
<br>
We start off by importing the modules Scapy and Ipaddress. Scapy is a fantastic packet manipulation tool for python. We establish a list of ports that we would like to scan and also an empty list that we will add IP addresses to. <br>
<a href="https://imgur.com/rP3vt31"><img src="https://i.imgur.com/rP3vt31.jpg" title="source: imgur.com" /></a><br>
<br>
Now I added a "with open" statement to import a list of IP addresses that we appened to our empty host_address list. Next we define our SynScan function, here you have to ensure you follow Scapy's syntax or you will get errors. In the function we create a variable that sr(send.receives) to a specific IP and settting a TCP syn scan via the flag "S". We then write a for loop that states that if we receive a syn/ack repsonce we will print the destination port. Finally we create a try function with the exception of halting and exiting if the ip address is invalid. Lastly we call the SynScan funciton.<br>
<a href="https://imgur.com/nnAbaj0"><img src="https://i.imgur.com/nnAbaj0.jpg" title="source: imgur.com" /></a><br>
<br>
<h3>Lessons Learned:</h3>
1. You should never scan IP addresses without permission.<br>
2. If you're having trouble, pull up the manual and follow the syntax of the module.<br>
3. This script has to be run with admin/root privileges.<br>


