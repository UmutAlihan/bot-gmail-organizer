import gmail_bot_functions as gb

#Authenticate to your gmail address
service = gb.auth()

# Get all mail ids
mailIds = gb.list_all_messages(service,"me")

# Get mail data from id
mail = gb.get_message(service, "me",messages[2]["id"])


# Get Date info
#Source: https://stackoverflow.com/questions/21787496/converting-epoch-time-with-milliseconds-to-datetime
date_unix = int(mail["internalDate"]) #returns Unix Time
date_normal = to_datetime((date_unix/1000.0))




###
for i in range(len(messages)):
	print(i)
	mail = gb.get_message(service, "me",messages[i]["id"])
	date_unix = int(mail["internalDate"]) #returns Unix Time
	date_normal = to_datetime((date_unix/1000.0))
	print(date_normal)
	for data in mail["payload"]["headers"]:
		if(data["name"] == "To"):
			print(data["value"])
	for data in mail["payload"]["headers"]:
		if(data["name"] == "From"):
			print(data["value"])
	print("############## ############# #############")


