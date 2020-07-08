#!/usr/bin/env python3

import gmail_bot_functions as gb
import sys, time, traceback, logging, coloredlogs
import click

# Sample command:
# python3 handle_labels_multiple_query.py averneus quora stackoverflow reddit medium Informative



@click.command()
@click.option('--account', help='Acocunt name to login')
@click.option('--query', multiple=True, help='Query words to search inbox')
@click.option('--label', help='Label name to move queried mails')


def execute(account, query, label):
    try:
        logging.info("INIT"); time.sleep(2)
        #parse arguments
        account = account # account name to login
        queries = list(query) #exclude label & accountname, only query kwords
        labelname = label # include only label

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
        sys.exit(1)



if __name__ == "__main__":
    logging.info("Running script: handle_labels_multiple_query.py")
    execute(sys.argv[1:])


