import gmail_bot_functions as gb
import sys

### INIT
#Authenticate to your gmail address
service = gb.auth_service()


### GET DATA
# Get all mail ids
    # glassdoor, nueove, etcd
mailIds_glassdoor = gb.list_messages_with_matching_query(service, "me", query='glassdoor')
mailIds_dailycode = gb.list_messages_with_matching_query(service, "me", query='Daily Coding')
mailIds = gb.list_all_messages(service, "me")

# Get mail info from Ids
mailBox = gb.mailBox_retriever(service, mailIds_glassdoor, verbose=True)

# Get label ids
labelid_jobapp = gb.get_id_for_labelname(service, "JobApp")
labelid_inbox = gb.get_id_for_labelname(service, "INBOX")
labelid_dailycode = gb.get_id_for_labelname(service, "Daily Code")


label_actions_jobapp = {'removeLabelIds': [labelid_inbox], 'addLabelIds': [labelid_jobapp]}
label_actions_dailycode = {'removeLabelIds': [labelid_inbox], 'addLabelIds': [labelid_dailycode]}


### PROCESS DATA

# find un-labeled mails ("JobApp") and label those
"""for mail in mailBox:
    if(labelid_jobapp in mail["labelIds"]):
        print("It has JobApp label: " + mail["id"] )
        pass
    else:
        print("Modifing to JobApp:" + mail["id"])
        gb.modify_message_label(service, "me", mail["id"], label_actions)  
        #modify_message_label(service, user_id, msg_id, msg_labels)"""      

# find un-labeled mails ("Daily Code") and label those
"""for mail in mailBox:
    if(labelid_dailycode in mail["labelIds"]):
        print("It has Daily Code label: " + mail["id"] )
        pass
    else:
        print("Modifing to Daily Code:" + mail["id"])
        gb.modify_message_label(service, "me", mail["id"], label_actions_dailycode)  
        #modify_message_label(service, user_id, msg_id, msg_labels)"""

fms = gb.find_mailids_below_threshold(mailBox, verbose=True)

