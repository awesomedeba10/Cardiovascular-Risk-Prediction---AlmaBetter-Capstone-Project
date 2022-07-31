from flask import url_for, request
import os
from urllib.parse import urlencode

def route(name, **query):
    url = url_for(name)
    query_pairs = [(k, vlist) for k,vlist in query.items()]
    return request.url_root + url[1:] + '?'+ urlencode(query_pairs)

def get_charts(dir, relative_path):
    # onlyfiles = [{url_for('static', filename='assets/images/charts/'+ f): Image.open(os.path.join(dir, f)).size} for f in os.listdir(dir) 
    #     if f.endswith(".webp")]
    files_list = [url_for('static', filename= relative_path + f) for f in os.listdir(dir) if f.endswith(".webp")]
    return files_list