FROM python:3.7

WORKDIR /app

RUN mkdir -p /app/tokens

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./ /app

CMD ["/bin/bash", "/app/gmailbot_handle_labels_in_batch_dockerize.sh"]

#CMD ["/usr/bin/python3", "/app/remove_older_than_dockerize.py", "JobApp", "3"] 
