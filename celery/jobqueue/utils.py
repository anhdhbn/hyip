from urllib.parse import urlparse

def get_domain(url):
    parsed_uri = urlparse(url)
    return parsed_uri.netloc.replace("www.", "")

def get_domain_pri(url):
    parsed_uri = urlparse(url)
    return parsed_uri.netloc

def get_link( url):
    parsed_uri = urlparse(url)
    return '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)