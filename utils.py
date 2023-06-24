def identify_url(text: str):
    return True if 'http' in text else False


def make_payload_url(url: str) -> dict:
    payload = {
		"url": url,
		"min_length": 100,
		"max_length": 300,
		"is_detailed": False
    }
    return payload


def make_payload_text(text: str) -> dict:
    payload = {
      "text": text,
      "num_sentences": 5
    }
    return payload