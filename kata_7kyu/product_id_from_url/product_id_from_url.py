import re


def get_product_id(url):
    match = re.search(r"-p-(\d+)-\d{8}\.html$", url)
    return match.group(1)
