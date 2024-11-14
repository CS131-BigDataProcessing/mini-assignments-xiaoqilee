
#!/bin/bash

# Task 1: 
cp -r /c/Users/leexi/log_analysis_project /c/Users/leexi/log_analysis_project/cron_logs/log_analysis_project_backup >> /c/Users/leexi/log_analysis_project/cron_logs/backup.log
#: To run daily at 5 AM: 0 5 * * * /c/Users/leexi/log_analysis_project/setup_cron_tasks.sh  (set this up in cron tab)


# Task 2:
echo "Reminder email" | mail -s "Monday Reminder" xiaoqi.lee@sjsu.edu >> /c/Users/leexi/log_analysis_project/cron_logs/email.log
#: To run every Monday at 6 AM: 0 6 * * 1 /c/Users/leexi/log_analysis_project/setup_cron_tasks.sh  (set this up in cron tab)


# Task 3: 
find /c/Users/leexi/log_analysis_project/cron_logs -type f -size +10M -exec sh -c '> "$1"' _ {} \; >> /c/Users/leexi/log_analysis_project/cron_logs/filter_file_size.log
#: To run daily at midnight: 0 0 * * * /c/Users/leexi/log_analysis_project/setup_cron_tasks.sh  (set this up in cron tab)

