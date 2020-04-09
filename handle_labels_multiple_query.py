#! /usr/bin/env python3

import gmail_bot_functions as gb
import sys, time, traceback, logging, coloredlogs

# Sample command:
# python3 handle_labels_multiple_query.py averneus quora stackoverflow reddit medium Informative


def execute(args):
    try:
        if(len(args) > 0):
            pass
        else:
            logging.info("not enough args")
            sys.exit()


        logging.info("INIT"); time.sleep(2)        
        #parse arguments        
        account = args[0] # account name to login
        queries = args[1:-1] #exclude label & accountname, only query kwords
        labelname = args[-1] # include only label

        #Authenticate to your gmail address
        #service = gb.auth_service()
        service = gb.auth_service_to(account)


        logging.info("GET DATA"); time.sleep(2)
        # Get all mail ids
        gb.label_messages_with_multiple_queries(service, queries, labelname)

    except:
        exc_info = sys.exc_info()
        # Display the *original* exception
        traceback.print_exception(*exc_info)
        del exc_info



if __name__ == "__main__":
    logging.info("running handle_labels_multiple_query.py")
    execute(sys.argv[1:])


