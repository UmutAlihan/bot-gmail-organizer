### interactions with the Google Gmail server are done via Gmail API.
### The api codebase for these interactions are belong to Google
### Here I developed a wrapper library for the needs of my bot


### Source to learn: 
### https://blog.mailtrap.io/send-emails-with-gmail-api/
#
### Google API client installation: 
### pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib



# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
#import pysnooper
import pickle
import os.path
import base64
import email
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors
import datetime
from time import time
import dateutil.relativedelta



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 
          'https://www.googleapis.com/auth/gmail.labels',
          'https://www.googleapis.com/auth/gmail.modify']


def auth_service():
  try:
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
    print("# Authenticated")
  except Exception as e:
    print("# Authentication failed")
    print(e)

  service = build('gmail', 'v1', credentials=creds)
  return service


def get_messages(service, user_id):
  try:
    return service.users().messages().list(userId=user_id).execute()
  except Exception as error:
    print('An error occurred: %s' % error)


def get_message(service, user_id, msg_id):
  try:
    return service.users().messages().get(userId=user_id, id=msg_id, format='metadata').execute()
  except Exception as error:
    print('An error occurred: %s' % error)  


def get_message_info(mail):    
    headers = mail["payload"]["headers"]
    for item in headers:
        if(item["name"] == "Date"):
            date = item["value"]
        if(item["name"] == "From"):
            address = item["value"]
        if(item["name"] == "Subject"):
            subject = item["value"]
    return (date, address, subject)


def get_attachments(service, user_id, msg_id, store_dir):
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    for part in message['payload']['parts']:
      if(part['filename'] and part['body'] and part['body']['attachmentId']):
        attachment = service.users().messages().attachments().get(id=part['body']['attachmentId'], userId=user_id, messageId=msg_id).execute()

        file_data = base64.urlsafe_b64decode(attachment['data'].encode('utf-8'))
        path = ''.join([store_dir, part['filename']])

        f = open(path, 'wb')
        f.write(file_data)
        f.close()
  except Exception as error:
    print('An error occurred: %s' % error)


def list_all_messages(service, user_id):
    try:
        response = service.users().messages().list(userId=user_id).execute()
        messages = []
        if('messages' in response):
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id, pageToken=page_token).execute()
            #print(response.keys)
            messages.extend(response['messages'])

        return messages
    except Exception as error:
        print ('An error occurred: %s' % error)


def list_messages_with_matching_query(service, user_id, query=''):
  # Source: https://developers.google.com/gmail/api/v1/reference/users/messages/list
  """List all Messages of the user's mailbox matching the query.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    query: String used to filter messages returned.
    Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

  Returns:
    List of Messages that match the criteria of the query. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate ID to get the details of a Message.
  """
  try:
    response = service.users().messages().list(userId=user_id,
                                               q=query).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id, q=query,
                                         pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except errors.HttpError as error:
    print ('An error occurred: %s' % error)


def list_messages_with_label(service, user_id, label_ids=[]):
  ### Source: https://developers.google.com/gmail/api/v1/reference/users/messages/list
  """List all Messages of the user's mailbox with label_ids applied.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    label_ids: Only return Messages with these labelIds applied.

  Returns:
    List of Messages that have all required Labels applied. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate id to get the details of a Message.
  """
  try:
    response = service.users().messages().list(userId=user_id,
                                               labelIds=label_ids).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id,
                                                 labelIds=label_ids,
                                                 pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except errors.HttpError as error:
    print ('An error occurred: %s') % error


def to_datetime(u): 
  return datetime.datetime.utcfromtimestamp(u) #to convert to normal time

def to_unixtime(d):
    return (d - datetime.datetime(1970, 1, 1)).total_seconds()

def check_direction(mail):
	for data in mail["payload"]["headers"]:
		# Get "From:"
		if(data["name"] == "From"):
			print("From: " + data["value"])
			return "From"
		# Get "To:" 
		if(data["name"] == "To"):
			print(data["value"])


def find_matching_received_mails(query_string, mailbox):
    found_mails = []
    for msg in mailbox:
        for data in msg["payload"]["headers"]:
            if(data["name"] == "From"):
                if(query_string in data["value"]):
                    #print(data["value"])
                    found_mails.append(msg)
    return found_mails


def list_labels(service, user_id):
    """Get a list all labels in the user's mailbox.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.

  Returns:
    A list all Labels in the user's mailbox.
  """
    try:
        response = service.users().labels().list(userId=user_id).execute()
        labels = response['labels']
        return labels
    except errors.HttpError as error:
        print ('An error occurred: %s' % error)
    

def get_id_for_labelname(service, labelname):
    labels = list_labels(service, "me")
    for label in labels:
        if(label["name"] == labelname):
            return label["id"]


def modify_message_label(service, user_id, msg_id, msg_labels):
  """Modify the Labels on the given Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The id of the message required.
    msg_labels: The change in labels.

  Returns:
    Modified message, containing updated labelIds, id and threadId.
  """
  try:
    message = service.users().messages().modify(userId=user_id, 
                                                id=msg_id, 
                                                body=msg_labels).execute()

    label_ids = message['labelIds']

    #print('Message ID: %s - With Label IDs %s' % (msg_id, label_ids))
    return message
  except Exception as error:
    print ('An error occurred: %s' % error)
        
        
def find_mailids_below_threshold(mailBox, month, verbose=False):
    found_mailids = []
    for i, mail in enumerate(mailBox):
        tunix = (int(mail["internalDate"]) / 1000.0)
        tnormal = to_datetime(tunix)
        tthreshold = datetime.datetime.today() - dateutil.relativedelta.relativedelta(months=month)
        comparison = tnormal.date() < tthreshold.date()
        if(not comparison):
            if(verbose):
                print("Position: {} -- State: {} -- {} -- mailID: {} -- Tnormal: {} > Tthresh {}"
                  .format("not added", comparison, i, mail["id"], tnormal, tthreshold))
        elif(comparison):
            if(verbose):
                print("Position: {} -- State: {} -- {} -- mailID: {} -- Tnormal: {} > Tthresh {}"
                  .format("added", comparison, i, mail["id"], tnormal, tthreshold))
            found_mailids.append(mail)
    return found_mailids


def mailBox_retriever(service, mailIds, stop=None, verbose=False):
    mailBox = []
    for i, mailId in enumerate(mailIds):
        if(verbose and (i % 10) == 0):
            print("Retrieved msg: " + str(i) + " --- " + mailId["id"])
        msg = get_message(service, "me", mailId["id"])
        mailBox.append(msg)
        if( stop is not None and i == stop):
            print("Got limited " + str(stop) + " mails!")
            break
    return mailBox


def trash_message(service, mailid ,userId="me"):
    return service.users().messages().trash(userId=userId, id=mailid).execute()



"""def create_object_for_labelupdate():
    #Create object to update labels.
    # Returns:
    # A label update object.
    return {'removeLabelIds': [], 'addLabelIds': ['UNREAD', 'INBOX', 'Label_2']}""" 

"""def check_string_in_From(query_string, mail):
    found_mails = []

    for data in mail["payload"]["headers"]:
        if(data["name"] == "From"):
            if(query_string in data["value"]):
                found_mails.append(data)"""

"""    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])"""

"""def get_mime_message(service, user_id, msg_id):
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()
    print('Message snippet: %s' % message['snippet'])
    msg_str = base64.urlsafe_b64decode(message['raw'].encode("utf-8")).decode("utf-8")
    mime_msg = email.message_from_string(msg_str)

    return mime_msg
  except Exception as error:
    print('An error occurred: %s' % error)"""
