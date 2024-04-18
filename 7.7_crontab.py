'''
How do we schedule a script?
Preferable way is to schedule jobs in intervals rather than all the time as per nohup
To do this we use the crontab

crontab -e
Select editor - nano is easiest - select relevant number e.g. 1
Use it to schedule tasks to run
5 options
M H DOM MON DOW
Minutes (m) Hours (h) Day of Month (dom) Month (mon) Day of Week (dow)
* means every time

1 * * * * [file name] [file path] - This would run at 1 minute past the hour every hour of every day
*/1 * * * * [file name] [file path] - This would run every minute of every hour of every day with 1 minute intervals
* 12 * * * [file name] [file path] - This would run at every minute of the 12th hour, not every 12 hours
0 12,0 * * * [file name] [file path] - Value needs to be entered to fix the minute value - 12,0 for h means that every 12 hours

crontab acts as though in the root directory need to ensure full path etc is used e.g.
0 12,0 * * * python3 /home/insertion3.py
ctrl x to exit and y to save

need to restart cron tab to initiate:
service cron restart

Use nohup for script which would take a long time to run and then end
Not recommended to have never ending scripts 
Crontab is recommended for regular scripts e.g. daily file transfer

'''