import gmail_bot_functions as gb

#Authenticate to your gmail address
service = gb.auth_service()

# Get all mail ids
    # glassdoor, nueove, etcd
mailIds = gb.list_messages_with_matching_query(service, "me", query='glassdoor')

# Get mail info from Ids
mailBox = []
for i, mailId in enumerate(mailIds):
    print(i)
    msg = gb.get_message(service, "me", mailId["id"])
    mailBox.append(msg)


# Get label id for JobApp
labelid = gb.get_id_for_labelname(service, "JobApp")
label_actions = {'removeLabelIds': [], 'addLabelIds': [labelid]}

# find un-labeled mails ("JobApp") and label those
for mail in mailBox:
    if(labelid in mail["labelIds"]):
        print("It has JobApp label: " + mail["id"] )
        pass
    else:
        print("Modifing to JobApp:" + mail["id"])
        gb.modify_message_label(service, "me", mail["id"], label_actions)  
        #modify_message_label(service, user_id, msg_id, msg_labels)      


#glassdoor_mails = gb.find_matching_received_mails("glassdoor", mailBox)

