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
    >>> a == "HTTP/1.0 200 OK\\r\\nContent-Type:text/html\\r\\nContent-Length:73\\r\\n\\r\\n<!DOCTYPE html>\\n<html>\\n<body>\\n<h1>Voici index.html !</h1>\\n</body>\\n</html>\\r\\n"
    True
    >>> b = get_reponse("page_non_existante")
    >>> b == "HTTP/1.0 404 NotFound\\r\\nContent-Type:text/html\\r\\nContent-Length:177\\r\\n\\r\\n<!DOCTYPE html>\\n<html>\\n<head><title>404 Not Found</title></head><body>\\n<h1>Page non trouvée !!</h1>\\n<p>L'URL demandée n'a pas été trouvée sur ce serveur.</p></body>\\n</html>\\r\\n"
    True
    """

    try:
        # On ouvre le fichier en mode format binaire pour avoir la véritable length (erreur dans les doctests fournies)
        with open(url_page, 'rb') as f:
            content = f.read()
            content_length = len(content)

            # On repasse en utf-8 pour les modifs
            content = content.decode()

            response = f"HTTP/1.0 200 OK\r\nContent-Type:text/html\r\nContent-Length:{content_length}\r\n\r\n"
            response += content+"\r\n"      # Retour à la ligne obligatoire

    # Si le fichier n'existe pas (FileNotFoundError) ou n'est pas lisible (PermissionError ou IOError (anciennes versions))
    except FileNotFoundError or PermissionError or IOError:
        # On ouvre le fichier en mode format binaire pour avoir la véritable length (erreur dans les doctests fournies)
        with open("pages_serveur/page404.html", 'rb') as f:
            content = f.read()
            content_length = len(content)

            # On repasse en utf-8 pour les modifs
            content = content.decode()

            response = f"HTTP/1.0 404 NotFound\r\nContent-Type:text/html\r\nContent-Length:{content_length}\r\n\r\n"
            response += content+"\r\n"      # Retour à la ligne obligatoire

    return response


def traite_requete(requete) :
    """
    >>> traite_requete(ex_requete_http2) == get_reponse("pages_serveur/fr/pages/index.html")
    True
    >>> traite_requete(ex_requete_http3) == get_reponse("pages_serveur/en/autres_pages/toto.html")
    True
    """
    
    page,options = decode_requete_http(requete)
    
    if "Accept-Language" in options and options["Accept-Language"].startswith('fr'):
        page = "pages_serveur/fr" + page

    else:
        page = "pages_serveur/en" + page

    return get_reponse(page)
        

if __name__ == "__main__" :

    # Ouverture en local sur le port 8080
    IP, PORT = ('127.0.0.1', 8080)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()

        while True:
            requete = conn.recv(1024)

            # S'il n'y a pas de requete on sort de la boucle
            if not requete:
                break

            # Nos fcts attendent une requete en utf-8
            requete = requete.decode()

            conn.sendall(traite_requete(requete).encode())

    conn.close()
    s.close()
