import gmail_bot_functions as gb
import sys, time

print("### INIT"); time.sleep(5)
#Authenticate to your gmail address
service = gb.auth_service()


print("### GET DATA "); time.sleep(5)
# Get all mail ids
    # glassdoor, nueove, etcd
mailIds_neuvoo = gb.list_messages_with_matching_query(service, "me", query='neuvoo')
#mailIds_glassdoor = gb.list_messages_with_matching_query(service, "me", query='glassdoor')
#mailIds_dailycode = gb.list_messages_with_matching_query(service, "me", query='Daily Coding')
#mailIds = gb.list_all_messages(service, "me")

# Get mail info from Ids
mailBox = gb.mailBox_retriever(service, mailIds_neuvoo, verbose=True)

# Get label ids
labelids = {"jobapp" : gb.get_id_for_labelname(service, "JobApp"),
            "inbox" : gb.get_id_for_labelname(service, "INBOX"),
            "dailycode" :  gb.get_id_for_labelname(service, "Daily Code")}


label_actions_jobapp = {'removeLabelIds': [labelids["inbox"]], 
                        'addLabelIds': [labelids["jobapp"]]}
label_actions_dailycode = {'removeLabelIds': [labelids["inbox"]],
                           'addLabelIds': [labelids["dailycode"]]}


print("### PROCESS DATA"); time.sleep(5)
# find un-labeled mails ("JobApp") and label those
for mail in mailBox:
    if(labelids["jobapp"] in mail["labelIds"]):
        print("It has JobApp label: " + mail["id"] )
        pass
    else:
        print("Modifing to JobApp:" + mail["id"])
        gb.modify_message_label(service, "me", mail["id"], label_actions_jobapp)  
        #modify_message_label(service, user_id, msg_id, msg_labels)

# find un-labeled mails ("Daily Code") and label those
"""for mail in mailBox:
    if(labelid_dailycode in mail["labelIds"]):
        print("It has Daily Code label: " + mail["id"] )
        pass
    else:
        print("Modifing to Daily Code:" + mail["id"])
        gb.modify_message_label(service, "me", mail["id"], label_actions_dailycode)  
        #modify_message_label(service, user_id, msg_id, msg_labels)"""

