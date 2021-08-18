import urllib.parse

def encode_source_url(n):
    return urllib.parse.quote(n.replace('.', '-').replace('/', 'backslash'))

def decode_source_url(n):
    return urllib.parse.unquote(n.replace('.', '-').replace('/', 'backslash'))