
# bot-gmailbox-organizer

![alt text](https://raw.githubusercontent.com/umutalihan/bot-gmail-organizer\assets\readme_picture.png)

This bot organizes mailboxes of given gmail address based on given rules using labels to manage mails one-by-one.


## Contents
  * [bot-gmailbox-organizer](#bot-gmailbox-organizer)
  * [Contents](#contents)                                                                             
  * [Description](#description)
  * [Getting Started](#getting-started)                                                                  
  * [Dependencies](#dependencies)                                                                     
  * [Installing](#installing)                                                                      
  * [Contribution &amp; Collaboration](#contribution--collaboration)                                  
  * [Authors](#authors)      


## Description

This repository is a collection of scripts to utilize wrapper functions in python. This module/library is developed as a wrapper for [Gmail API](https://developers.google.com/gmail/api). Gmail API uses get/post requests using Http protocol and transfer data with json objects as usual. Personally I developed this simple wrapper and wrote scripts around it in order to clutter my personal mailbox. I needed this to arrange my Glassdoor, LinkedIn open position notifications into their own folder from Inbox by inserting/removing Labels. 

## Getting Started

All related functions are in gmail_bot_functions.py file. With simple import you can start using wrapper functions. Currently I develop regular automations for my mailbox by writing new .py files. Those are named as what their function in my mailbox is. Since this is a project is in scope of "code to learn" concept, I would be super happy, if you could provide issues, development suggestions, pull requests, beautifying the README, etc.

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.

### Installing

* Install Juypter Notebook for exploring the codebase with explore.pynb
* Enable [Gmail API](https://developers.google.com/gmail/api/quickstart/python) for your gmail account.
* Create your own app and generate credential.json (you might have to design an authorization page). All detailed steps are in [Gmail API Quickstart Guide](https://developers.google.com/gmail/api/quickstart/python)
* Install [Google Client Library](https://developers.google.com/gmail/api/quickstart/python)
* (You can find cmd below in explore.ipynb notebook.)
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```


## Contribution & Collaboration

As I mentioned above, please collaborate. Community always helped me to learn and improve. Even though this is not a very organized project, I am very open to any feedback, suggestions or mentoring. 

## Authors

Contributors names and contact info:

Umut Alihan Dikel
[@umutalihan](https://www.linkedin.com/in/umut-alihan-dikel-13822762?originalSubdomain=tr)

