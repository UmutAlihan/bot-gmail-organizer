#! /usr/bin/env python3

import gmail_bot_functions as gb
import sys, time, traceback, logging, coloredlogs

# Sample command:
# python3 remove_older_than.py JobApp 3



def execute(args):
    try:
        logging.info("INIT PROCESS"); time.sleep(2)
        #Check args
        if(len(args) > 1):
            labelname = args[0]
            month = args[1]
        else:
            logging.error("not enough args")
            sys.exit()
        #Authenticate to your gmail address
        service = gb.auth_service_to("averneus")


        logging.info("GET DATA"); time.sleep(2)
        ## get mails with given Label
        label_ids = gb.get_id_for_labelname(service, labelname)
        label_mailids = gb.list_messages_with_label(service, "me", label_ids=[label_ids])

        ## Get mail info from Ids
        mailBox = gb.mailBox_retriever(service, label_mailids, verbose=True)

        logging.info("PROCESS DATA"); time.sleep(2)
        ## get labeled mails before given Date Threshold
        fms = gb.find_mailids_below_threshold(mailBox, month=int(month), verbose=False)
        if(fms == []):
            logging.warning("No mails found to trash")
        elif(fms != [] and type(fms) == list):
        ## trash mails older than Threshold
            logging.info("Trying to delete mail")
            for mail in fms:
                gb.trash_message(service, mail["id"])
                logging.debug('Gone - {}'.format(mail["snippet"]))
        else:
            logging.warning("Something is wrong with fms variable: go check trash_message")
    except Exception as e:
        logging.error(e)
        exc_info = sys.exc_info()
        # Display the *original* exception
        traceback.print_exception(*exc_info)
        del exc_info



if __name__ == "__main__":
    logging.info("remove_older_than.py")
    execute(sys.argv[1:])
