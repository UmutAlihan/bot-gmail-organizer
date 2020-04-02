import gmail_bot_functions as gb
import sys, time, traceback



def execute(args):
    try:
        print("### INIT PROCESS"); time.sleep(2)
        #Check args
        if(len(args) > 1):
            labelname = args[0]
            month = args[1]
        else:
            print("not enough args")
            sys.exit()
        #Authenticate to your gmail address
        service = gb.auth_service()


        print("### GET DATA"); time.sleep(2)
        ## get mails with given Label
        label_ids = gb.get_id_for_labelname(service, labelname)
        label_mailids = gb.list_messages_with_label(service, "me", label_ids=[label_ids])

        ## Get mail info from Ids
        mailBox = gb.mailBox_retriever(service, label_mailids, verbose=True)

        print("### PROCESS DATA"); time.sleep(2)
        ## get labeled mails before given Date Threshold
        fms = gb.find_mailids_below_threshold(mailBox, month=int(month), verbose=False)
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
    except Exception as e:
        exc_info = sys.exc_info()
        # Display the *original* exception
        traceback.print_exception(*exc_info)
        del exc_info



if __name__ == "__main__":
    execute(sys.argv[1:])