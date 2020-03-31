import gmail_bot_functions as gb
import sys, time, traceback



def execute(args):
	try:
		if(len(args) > 0):
			pass
		else:
			print("not enough args")
			sys.exit()

		print("### INIT"); time.sleep(5)
		#Authenticate to your gmail address
		service = gb.auth_service()


		print("### GET DATA "); time.sleep(5)
		# Get all mail ids
		query = args[0]
		labelname = args[1]

		mailIds = gb.list_messages_with_matching_query(service, "me", query=query)
		#mailIds_glassdoor = gb.list_messages_with_matching_query(service, "me", query='glassdoor')

		#mailIds_dailycode = gb.list_messages_with_matching_query(service, "me", query='Daily Coding')
		#label_actions_dailycode = {'removeLabelIds': [labelids["inbox"]],
		#                           'addLabelIds': [labelids["dailycode"]]}

		# Get label ids
		"""labelids = {"jobapp" : gb.get_id_for_labelname(service, "JobApp"),
		            "inbox" : gb.get_id_for_labelname(service, "INBOX"),
		            "dailycode" :  gb.get_id_for_labelname(service, "Daily Code")}"""
		labelid = gb.get_id_for_labelname(service, labelname)
		labelid_inbox = gb.get_id_for_labelname(service, "INBOX")

		label_actions_jobapp = {'removeLabelIds': [labelid_inbox], 
								'addLabelIds': [labelid]}

		# Get mail info from Ids
		print("# Retrieving: '" + query + "' related mails" )
		mailBox = gb.mailBox_retriever(service, mailIds, verbose=True)


		print("### PROCESS DATA"); time.sleep(5)
		# find un-labeled mails ("JobApp") and label those
		for mail in mailBox:
		    if(labelid in mail["labelIds"]):
		        print("It has JobApp label: " + mail["id"] )
		        pass
		    else:
		        print("Modifing to JobApp:" + mail["id"])
		        gb.modify_message_label(service, "me", mail["id"], label_actions_jobapp)  
		        #modify_message_label(service, user_id, msg_id, msg_labels)
	except:
		exc_info = sys.exc_info()
		# Display the *original* exception
		traceback.print_exception(*exc_info)
		del exc_info



if __name__ == "__main__":
   execute(sys.argv[1:])



# find un-labeled mails ("Daily Code") and label those
"""for mail in mailBox:
    if(labelid_dailycode in mail["labelIds"]):
        print("It has Daily Code label: " + mail["id"] )
        pass
    else:
        print("Modifing to Daily Code:" + mail["id"])
        gb.modify_message_label(service, "me", mail["id"], label_actions_dailycode)  
        #modify_message_label(service, user_id, msg_id, msg_labels)"""

