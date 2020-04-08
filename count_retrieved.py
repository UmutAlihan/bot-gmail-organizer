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


filename = "counted_messages.csv"
logging.info("writing into: " + filename)
w = csv.writer(open(filename, "w"))
for key, val in counted_messages.items():
    w.writerow([key, val])
