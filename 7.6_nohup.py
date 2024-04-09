'''
How to get script to always run?
insertion3.py
If using for loop:
for _ in range(5): #Underscore denotes worthlessness of a variable (non-variable)
If while loop - infinite loop
while true:
Using the above the script will only run whilst user e.g. root is logged in
To run script in the background:
Use nohup - no hang up
nohup python insertion2.py &
Run - make sure sleeps are included in file to allow breaks in running script
Outputs to temporary nohup.out file
top - in terminal is similar to task manager
sudo apt-get install htop - more advanced version of top
htop - in terminal to run htop
to end/kill script - highlight line script is running on - F9 to kill
Select default SIGTERM option and hit enter
sudo reboot - reboots server and would also kill any scripts

#Need to add insertion3.py to server and test - rewatch video for additional notes
'''