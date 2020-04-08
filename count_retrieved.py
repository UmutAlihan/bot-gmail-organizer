#! /usr/bin/env python3

import gmail_bot_functions as gb
import dateutil.relativedelta
import datetime
from time import time
import csv

service = gb.auth_service()
mailIds = gb.list_all_messages(service, "me")
mailBox = gb.mailBox_retriever(service, mailIds, verbose=True)

counted_messages, sorted_counted_messages = gb.count_retrieved_messages(mailBox)

w = csv.writer(open("counted_messages.csv", "w"))
for key, val in counted_messages.items():
    w.writerow([key, val])
