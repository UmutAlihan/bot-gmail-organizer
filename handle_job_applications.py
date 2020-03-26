import gmail_bot_functions as gb

#Authenticate to your gmail address
service = gb.auth_service()

# Get all mail ids
    # glassdoor, nueove, etcd
mailIds_glassdoor = gb.list_messages_with_matching_query(service, "me", query='glassdoor')
mailIds_dailycode = gb.list_messages_with_matching_query(service, "me", query='Daily Coding')
mailIds = gb.list_all_messages(service, "me")


# Get mail info from Ids
mailBox = []
for i, mailId in enumerate(mailIds):
    print(i)
    msg = gb.get_message(service, "me", mailId["id"])
    mailBox.append(msg)

mailBox = []
for i, mailId in enumerate(mailIds_glassdoor):
    print(i)
    msg = gb.get_message(service, "me", mailId["id"])
    mailBox.append(msg)

mailBox = []
for i, mailId in enumerate(mailIds_dailycode):
    print(i)
    msg = gb.get_message(service, "me", mailId["id"])
    mailBox.append(msg)

# Get label id for JobApp
labelid_jobapp = gb.get_id_for_labelname(service, "JobApp")
labelid_inbox = gb.get_id_for_labelname(service, "INBOX")
labelid_dailycode = gb.get_id_for_labelname(service, "Daily Code")

label_actions_jobapp = {'removeLabelIds': [labelid_inbox], 'addLabelIds': [labelid_jobapp]}
label_actions_dailycode = {'removeLabelIds': [labelid_inbox], 'addLabelIds': [labelid_dailycode]}


# find un-labeled mails ("JobApp") and label those
for mail in mailBox:
    if(labelid_jobapp in mail["labelIds"]):
        print("It has JobApp label: " + mail["id"] )
        pass
    else:
        print("Modifing to JobApp:" + mail["id"])
        gb.modify_message_label(service, "me", mail["id"], label_actions)  
        #modify_message_label(service, user_id, msg_id, msg_labels)      

# find un-labeled mails ("Daily Code") and label those
for mail in mailBox:
    if(labelid_dailycode in mail["labelIds"]):
        print("It has Daily Code label: " + mail["id"] )
        pass
    else:
        print("Modifing to Daily Code:" + mail["id"])
        gb.modify_message_label(service, "me", mail["id"], label_actions_dailycode)  
        #modify_message_label(service, user_id, msg_id, msg_labels)      


#glassdoor_mails = gb.find_matching_received_mails("glassdoor", mailBox)

