import gmail_bot_functions as gb
import sys, time

print("### INIT PROCESS"); time.sleep(5)
#Authenticate to your gmail address
service = gb.auth_service()



print("### GET DATA"); time.sleep(5)
## get mails with given Label
label_ids = gb.get_id_for_labelname(service, "JobApp")

label_mailids = gb.list_messages_with_label(service, "me", label_ids=[label_ids])

## Get mail info from Ids
mailBox = gb.mailBox_retriever(service, label_mailids, verbose=True)
#verbose: for i, mail in enumerate(mailBox_jobapp):
#verbose:    print("Snippet for mail: " + str(i) + " is: \n" + mail["snippet"])


print("### PROCESS DATA"); time.sleep(5)
## get labeled mails before given Date Threshold
fms = gb.find_mailids_below_threshold(mailBox, verbose=False, month=2)
if(fms == []):
    print("No mails found to trash")
elif(fms != [] and type(fms) == list):
## trash mails older than Threshold
    print("Trying to delete mail")
    for mail in fms:
        gb.trash_message(service, mail["id"])
        print('Gone - {}'.format(mail["snippet"]))
else:
    print("Something is wrong with fms variable: go check trash_message")