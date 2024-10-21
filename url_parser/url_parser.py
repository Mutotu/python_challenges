def parse_qs(query):
    """
    Parse a query string into a dictionary of key-value pairs.
    """
    result = {}
    pairs = query.split("&")
    for pair in pairs:
        key, value = pair.split("=")
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    return result


def url_parse(url):
    """
    Parse the URL into components: scheme, host, port, path, and query.
    """
    scheme = url.split(":")[0]
    rest = url.split("//")[1]
    host_port = rest.split("/")[0]  # This will contain host and possibly port
    path_and_query = rest[len(host_port):].split("?")

    # Handle host and port
    if ":" in host_port:
        host, port = host_port.split(":")
    else:
        host = host_port
        port = 80

    # Handle path
    path = "/" + "/".join(path_and_query[0].strip("/").split("/"))

    # Handle query
    query = path_and_query[1] if len(path_and_query) > 1 else ""

    return {
        "scheme": scheme,
        "host": host,
        "port": int(port),
        "path": path,
        "query": query
    }


def parse(url):
    parsed = url_parse(url)
    query = parse_qs(parsed["query"]) if parsed["query"] else {}
    return {
        'scheme': parsed['scheme'],
        'host': parsed['host'],
        'port': parsed['port'],
        'path': parsed['path'],
        'query': "&".join([f"{k}={','.join(v)}" for k, v in query.items()]) if query else ""
    }

