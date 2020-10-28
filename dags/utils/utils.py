import requests

def download_from_github_url(github_url: str = None):
    try:
        response = requests.get(github_url)
        if response.ok:
            return response.text
    except Exception as e:
        raise(e)
