import gmail_bot_functions as gb


#Authenticate to your gmail address
service = gb.auth_service()

# Get all mail ids
#old: 
#mailIds = gb.list_all_messages(service,"me")
#more efficient:
mailIds = gb.list_messages_with_matching_query(service, "me", query='glassdoor')

# Get all mail info from Ids
mailBox = []
for i, mailId in enumerate(mailIds):
    print(i)
    msg = gb.get_message(service, "me", mailId["id"])
    mailBox.append(msg)
    

# Get label id for JobApp
labelid = get_id_for_labelname(service, "JobApp")
    
#for each glassdoor mail set JobApp label





#glassdoor_mails = gb.find_matching_received_mails("glassdoor", mailBox)

