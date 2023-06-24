from config import (
    TLDR_API_TOKEN,
    TLDR_HOST
)
from utils import (
    make_payload_text,
    make_payload_url,
    identify_url
)

import requests


api_url_article = "https://tldrthis.p.rapidapi.com/v1/model/abstractive/summarize-url/"
api_url_text = "https://tldrthis.p.rapidapi.com/v1/model/extractive/summarize-text/"


headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": TLDR_API_TOKEN,
	"X-RapidAPI-Host": TLDR_HOST
}


def get_summary(text: str) -> str:
    if identify_url(text):
        payload = make_payload_url(text)
        response = requests.post(api_url_article, json=payload, headers=headers)
        return response.json()['summary'][0]
    
    payload = make_payload_text(text)
    response = requests.post(api_url_text, json=payload, headers=headers)
    return ' '.join(response.json()['summary'])

