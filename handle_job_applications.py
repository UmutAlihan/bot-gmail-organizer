import gmail_bot_functions as gb


#Authenticate to your gmail address
service = gb.auth_service()

# Get all mail ids
mailIds = gb.list_all_messages(service,"me")

# Get all mail info from Ids
mailBox = []
for i, mailId in enumerate(mailIds):
    print(i)
    msg = gb.get_message(service, "me", mailId["id"])
    mailBox.append(msg)

glassdoor_mails = gb.find_matching_received_mails("glassdoor", mailBox)

#for each glassdoor mail set JobApp label