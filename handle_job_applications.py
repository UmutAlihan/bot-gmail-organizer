import gmail_bot_functions as gb


#Authenticate to your gmail address
service = gb.auth_service()

# Get all mail ids
mailIds = gb.list_all_messages(service,"me")

# Get all mail info from Ids
msgs = []
for i, mailId in enumerate(mailIds):
    print(i)
    msg = gb.get_message(service, "me", mailId["id"])
    msgs.append(msg)

