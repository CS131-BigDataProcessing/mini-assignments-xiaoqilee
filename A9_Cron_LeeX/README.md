A09 Cron-Tasks

Objectives:
Understand how to use `cron` for scheduling recurring tasks
Learn how to use `at` for scheduling one-time tasks
Practice setting up, running, and troubleshooting automated jobs

Files Included:
1. crontab.txt
   - Includes a copy of the crontab file in a txt form showing the commands for 3 separate cron jobs
2. about_crontask.txt
   - Answers the questions: What other types of tasks could benefit from automation using cron or at? What are the potential risks with poorly  managed automated tasks, and how can these risks be avoided?
3. README.md
   - Explains purpose and content of assignment submission


                                                                                  crontab.txt - Task 1: Delete all files from a temporary directory every day at 2:00 AM                                                                              Command: 0 2 * * * /bin/rm -rf /mnt/scratch/FA24_CS131_Jessica/xleefa24/temp/*

crontab.txt - Task 2: Back up your home directory every Sunday at 3:00 AM
Command: 0 3 * * 0 tar -czf /mnt/scratch/FA24_CS131_Jessica/xleefa24/backups/backup.tar.gz /mnt/scratch/FA24_CS131_Jessica/xleefa24

crontab.txt - Task 3: Email a disk usage report every day at 8:30 AM
Command: 30 8 * * * df -h | mail -s "disk usage report" xiaoqi.lee@sjsu.edu

To implement the cron jobs:
1. Type crontab -e to edit your crontab
2. Paste the commands located in crontab.txt into your crontab and click Esc and :wq to save and quit
3. Ensure the crontab was updated by using crontab -l
4. Prior to the cron jobs running, have a directory /mnt/scratch/FA24_CS131_Jessica/xleefa24/temp and  /mnt/scratch/FA24_CS131_Jessica/xleefa24/backups
5. Wait for the scheduled time to arrive (should have files in temp and xleefa24 to see changes and a mail system set up)
