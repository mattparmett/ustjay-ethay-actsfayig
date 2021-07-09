import os
import random
import json

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://randomfactgenerator.net")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="z")

    return facts[0].getText().split("\n")[0]


@app.route('/')
def home():
    # return "test"
    data = {'input_text': get_fact()}
    pig_latin_url = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/",
                                  data=data, 
                                  allow_redirects=False
                                  ).headers['location']
    
    return ("<html><body>Here is the link to a pig-latinized fact: "
            f"<a href={pig_latin_url}>{pig_latin_url}</a></body></html>")


if __name__ == "__main__":
    print(get_fact())
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

