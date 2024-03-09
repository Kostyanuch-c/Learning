from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


def make(url):
    return urlparse(url)


def get_scheme(data):
    return data.scheme


def set_scheme(data, scheme):
    return data._replace(scheme=scheme)


def get_host(data):
    return data.netloc


def set_host(data, host):
    return data._replace(netloc=host)


def get_path(data):
    return data.path


def set_path(data, path):
    return data._replace(path=path)


def get_query_param(data, param_name, default=None):
    d = urlencode(parse_qs(data.query), doseq=True)
    dct_params = {}
    for elem in d.split('&'):
        elem_lst = elem.split('=')
        dct_params[elem_lst[0]] = elem_lst[1]

    return dct_params.get(param_name, default)


def set_query_param(data, key, value):
    query = parse_qs(data.query)
    if value is None and key in query:
        query.pop(f'{key}')
    elif value is None:
        pass
    else:
        query.update({key: [value]})
    d = urlencode(query, doseq=True)
    return data._replace(query=d)


def to_string(data):
    scheme = get_scheme(data)
    path = get_path(data)
    host = get_host(data)
    query = data.query
    fragment = data.fragment
    lst_url = [scheme, host, path, query, fragment, '']
    result = ''
    for elem in urlunparse(lst_url):
        if elem == ';':
            elem = '?'
            result += elem
        else:
            result += elem
    return result


u = make('http://hexlet.io/404?page=5')
u = set_query_param(u, 'missed', None)
