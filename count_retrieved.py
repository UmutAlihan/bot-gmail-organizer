#! /usr/bin/env python3

import gmail_bot_functions as gb
import dateutil.relativedelta
import datetime
from time import time
import csv
import logging

service = gb.auth_service()
mailIds = gb.list_all_messages(service, "me")
logging.info("retrieving mails")
mailBox = gb.mailBox_retriever(service, mailIds, verbose=True)

logging.info("counting mails")
counted_messages, sorted_counted_messages = gb.count_retrieved_messages(mailBox)


<<<<<<< HEAD
filename = "counted_messages.csv"
logging.info("writing into: " + filename)
w = csv.writer(open(filename, "w"))
=======
#CSV writer source: https://pythonspot.com/save-a-dictionary-to-a-file/
w = csv.writer(open("counted_messages.csv", "w"))
>>>>>>> f0ab7ea93ad5f25ae563313ead78563b439549a4
for key, val in counted_messages.items():
    w.writerow([key, val])
