import requests

GITHUB_BASE_URL_DOWNLOAD="https://raw.githubusercontent.com/francamacdowell/orchestrator-airflow/master/data/"

FILE_NAMES = ["369120472020-04-02.json", "369120472020-04-03.json", "369120472020-04-04.json"]

def download_from_github_url(github_url: str = None):
    try:
        response = requests.get(github_url)
        if response.ok:
            return response.text
    except Exception as e:
        raise(e)
