from flask import url_for, request
from urllib.parse import urlencode

def route(name, **query):
    url = url_for(name)
    query_pairs = [(k, vlist) for k,vlist in query.items()]
    return request.url_root + url[1:] + '?'+ urlencode(query_pairs)