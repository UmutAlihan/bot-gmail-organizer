import gmail_bot_functions as gb
import sys, time, traceback, logging, coloredlogs

# Sample command:
# python3 handle_labels_multiple_queries.py reddit stackoverflow Informative

def execute(args):
    try:
        if(len(args) > 0):
            pass
        else:
            print("not enough args")
            sys.exit()

        logging.info("INIT"); time.sleep(2)
        #print("### INIT"); time.sleep(2)
        #Authenticate to your gmail address
        service = gb.auth_service()

        print("### GET DATA "); time.sleep(2)
        # Get all mail ids
        queries = args[:-1] #exclude label
        labelname = args[-1] # include only label

        gb.label_messages_with_multiple_queries(service, queries, labelname)

    except:
        exc_info = sys.exc_info()
        # Display the *original* exception
        traceback.print_exception(*exc_info)
        del exc_info



if __name__ == "__main__":
    execute(sys.argv[1:])


