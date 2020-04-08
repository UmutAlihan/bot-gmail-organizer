from __future__ import print_function
import pickle
import os.path
import base64
import email
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors
import logging, coloredlogs
import sys

coloredlogs.install()
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
	level=logging.INFO,
	datefmt='%Y-%m-%d %H:%M:%S')

logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.CRITICAL)
logging.getLogger('googleapiclient.discovery').setLevel(logging.WARNING)

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def auth_service_to(account):
  try:
    #os.chdir("/home/uad/apps/bot-gmail-organizer/")
    pathname = os.path.dirname(sys.argv[0])
    fullpath = os.path.abspath(pathname)
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    file_token = fullpath + '/test_dir/token-' + account + '.pickle'
    file_cred = fullpath + '/test_dir/test-credentials.json'
    if os.path.exists(file_token):
      with open(file_token, 'rb') as token:
        creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            file_cred, SCOPES)
        creds = flow.run_local_server(port=0)
      # Save the credentials for the next run      
      with open(file_token, 'wb') as token:
        pickle.dump(creds, token)
    
    logging.info("# Authenticated")
  except Exception as e:
    logging.info("Authentication failed")
    logging.error(e)

  service = build('gmail', 'v1', credentials=creds)
  return service



auth_service_to(sys.argv[1])