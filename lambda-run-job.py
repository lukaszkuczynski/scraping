import os
import requests
from requests.auth import HTTPBasicAuth
import json


API_KEY = os.getenv("SCRAPINGHUB_API_KEY")


def run_job(event, context): 
    url = "https://app.scrapinghub.com/api/run.json"
    topic = event['topic']
    body = {
        "project": "446349",
        "spider": "mediumtopic",
        "topic": topic,
    }
    print(body)
    resp = requests.post(url, data=body, auth=HTTPBasicAuth(username=API_KEY, password=""))
    return {
        'status': resp.status_code,
        'text': resp.text
    }


if __name__ == "__main__":
    event = {
        "topic": "data-science"
    }
    run_job(event, None)