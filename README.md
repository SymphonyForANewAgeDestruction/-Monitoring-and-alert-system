# -Monitoring-and-alert-system

I developed a small project when I was getting acquainted with the Linux system that sends alerts when problems are detected (for example, high CPU load, low free disk space, low memory availability).

To run the program every nth amount of time, use the Cron task scheduler in Linux.
To create a task follow the instructions:

Editing or creating a schedule file for the current user: # crontab -e

Next, in the window that opens in your default editor (Vim/nano), enter: “*/5 * * * * python /path/to/your/project/monitoring.py”)
(as an example to run every 5 minutes) Save and close.

To check that everything is done correctly: # crontab -l

To remove from Cron: #cronrab -r
