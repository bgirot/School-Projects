import socket
import doctest

ex_requete_http1="GET /page1.html HTTP/1.1\r\nHost: localhost\r\nAccept-Language: fr-FR,en;q=0.3\r\nUser-Agent: Mozilla/5.0 Firefox/98.0\r\n\r\n"
ex_requete_http2="GET /pages/index.html HTTP/1.1\r\nHost: localhost\r\nAccept-Language: fr\r\n\r\n"
ex_requete_http3="GET /autres_pages/toto.html HTTP/1.1\r\nHost: localhost\r\n\r\n"

def decode_requete_http(requete) :
    """
    >>> a,b = decode_requete_http(ex_requete_http1)
    >>> a == "/page1.html"
    True
    >>> len(b)
    3
    >>> b["Host"] == "localhost"
    True
    >>> b["Accept-Language"] == "fr-FR,en;q=0.3"
    True
    >>> b["User-Agent"] == "Mozilla/5.0 Firefox/98.0"
    True
    """

    page = requete.split(" ")[1]

    options_list = requete.split("\r\n")[1:-2]
    options = {}

    for optn in options_list:
        key = optn.split(": ")[0]
        val = optn.split(": ")[1]
        options[key] = val
    
    return page, options
    


def get_reponse(url_page) :
    """
    >>> a = get_reponse("pages_serveur/fr/pages/index.html")
    >>> a == "HTTP/1.0 200 OK\\r\\nContent-Type:text/html\\r\\nContent-Length:74\\r\\n\\r\\n<!DOCTYPE html>\\n<html>\\n<body>\\n<h1>Voici index.html !</h1>\\n</body>\\n</html>\\r\\n"
    True
    >>> b = get_reponse("page_non_existante")
    >>> b == "HTTP/1.0 404 NotFound\\r\\nContent-Type:text/html\\r\\nContent-Length:173\\r\\n\\r\\n<!DOCTYPE html>\\n<html>\\n<head><title>404 Not Found</title></head><body>\\n<h1>Page non trouvée !!</h1>\\n<p>L'URL demandée n'a pas été trouvée sur ce serveur.</p></body>\\n</html>\\r\\n"
    True
    """

    try:

        with open(url_page, 'r', encoding='utf-8') as f:

            with open(url_page, 'r', encoding='utf-8') as f:

                content = f.read()
                content_length = len(content) + 1

                content = "\n".join(content.split("\n"))

                response = f"HTTP/1.0 200 OK\r\nContent-Type:text/html\r\nContent-Length:{content_length}\r\n\r\n"
                response += content+"\r\n"

                return response

    except FileNotFoundError or PermissionError or IOError:

        with open("pages_serveur/page404.html", 'r', encoding='utf-8') as f:

            content = f.read()
            content_length = len(content) + 1

            content = "\n".join(content.split("\n"))

            response = f"HTTP/1.0 404 NotFound\r\nContent-Type:text/html\r\nContent-Length:{content_length}\r\n\r\n"
            response += content+"\r\n"

            return response


def traite_requete(requete) :
    """
    >>> traite_requete(ex_requete_http2) == get_reponse("pages_serveur/fr/pages/index.html")
    True
    >>> traite_requete(ex_requete_http3) == get_reponse("pages_serveur/en/autres_pages/toto.html")
    True
    """
    
    page,options = decode_requete_http(requete)

    if "Accept-Language" in options and options["Accept-Language"] == 'fr':
        page = "pages_serveur/fr" + page

    else:
        page = "pages_serveur/en" + page

    return get_reponse(page)
        

if __name__ == "__main__" :
    doctest.testmod()
