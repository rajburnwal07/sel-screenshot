find /home/ec2-user/test -mmin +120 -exec rm {} \;

import os, time, sys
import logging.handlers
import logging
folder_path = "/home/ec2-user/test"
file_ends_with = "*"
how_many_days_old_logs_to_remove = 2

now = time.time()
only_files = []

for file in os.listdir(folder_path):
    file_full_path = os.path.join(folder_path,file)
    if os.path.isfile(file_full_path) and file.endswith(file_ends_with):
        #Delete files older than x days
        if os.stat(file_full_path).st_mtime < now - how_many_days_old_logs_to_remove * 86400:
             os.remove(file_full_path)
             print "\n File Removed : " , file_full_path
handler = logging.handlers.WatchedFileHandler("Del-info.log")

# define format of the log, in this case just a date & time with the log message
formatter = logging.Formatter("%(asctime)s;%(message)s")

# attach new formatter
handler.setFormatter(formatter)

# get logger instance and update its settings
logger = logging.getLogger()
logger.setLevel("INFO")
logger.addHandler(handler)

# now just log away
logging.info("File deleted: {}".format(file))
