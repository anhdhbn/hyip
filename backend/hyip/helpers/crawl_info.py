from urllib.parse import urlparse

def get_domain(url):
    parsed_uri = urlparse(url)
    return parsed_uri.netloc