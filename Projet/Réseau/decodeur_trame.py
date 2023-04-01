import struct
import doctest
import socket

ex_udp = b'\x00-\xd9\x9e\x00\x0eR\x8ccoucou'
ex_tcp = b'\x00-\xd7[\x00\x00\x17\x15\x00\x00\x04e\x86\xc6\ndg!By!\xaf\xff&\xfc\x19R\xcc\x18\xac|(coincoin'
ex_icmp = b'\x05\x04g\x90\x1a@\xc9\x01'
ex_ip = b"H\xf7\x00&[\x0cI\r\xe5\x01v5\xea\xd8\xa0\xe5L\xda\x86\x93\x0e\xa0\xed\xe8\x99\xc1G\xc0{P'\xc4cuicui"
ex_eth = b'R\x0c\xc7\x1d\xca578\x1fUk\x98\x08\x00coicoi'

ex_complet1 = b'Q\xf0\xdeG?\xf4\xa0\x18\x12f\xde\xd5\x08\x00H$\x00(\x85\xc2\x11\xcc\x83\x01\xf1\x94\xff\xfc\xbf\x067\x17\xd9\x86\xd4\x96\xbf\xdfdv$a\xae\x01\xd0\x90\n\x07\x1d\xfd\xdb\t3\xad'
ex_complet2 = b'\xb3\x82\x90ze\xe66?HJ#9\x08\x00Hu\x00G\\S\n{\r\x06\x0f\x93\x1f\xc9\xa5\xd0\xac\xea\xbc\xea\xc4\x13a\xdet>\xe1\x13\x9cJ\x8f\x1b\x03\x15\xf5\x83\x00\x00\x11L\x00\x00\r\xea\x80:\\\x9dJ\x9c)\xaf\xba\xcc){\xc0\x97\x83\xc4\xcd\xec3\xb4bravo !'
ex_complet3 = b"\x8e`\x1cV\xbf\x86\xa6\x0b\x8f\x99\xe8\x1e\x08\x00H>\x001\x1e*\xd4\xc5\x13\x11\xb20W'\xce*\xdb+\xc4\xa7\x08}\x99\xfd\xd9\x90\x9d\x1cA/\x1f\x00\x02\x99\xddG\x00\x11\xda\x9asuper ;-)"

def decode_udp(data) :
    """
    >>> a = decode_udp(ex_udp)
    >>> len(a) == 2
    True
    >>> a[0] == "        +++ Paquet UDP +++\\n            Port source      : 45\\n            Port destination : 55710\\n            Longueur totale  : 14\\n"
    True
    >>> a[1].decode('utf-8') == "coucou"
    True
    """
    unmask_udp = struct.unpack("!HHHH", data[:8])
    return f"        +++ Paquet UDP +++\n            Port source      : {unmask_udp[0]}\n            Port destination : {unmask_udp[1]}\n            Longueur totale  : {unmask_udp[2]}\n", data[8:]


def decode_tcp(data) :
    """
    >>> a = decode_tcp(ex_tcp)
    >>> len(a) == 2
    True
    >>> a[0] == "        +++ Paquet TCP +++\\n            Port source      : 45\\n            Port destination : 55131\\n            Longueur en-tête : 8\\n"
    True
    >>> a[1].decode('utf-8') == "coincoin"
    True
    """
    port_source_tcp = struct.unpack("!H", data[:2])[0]
    port_destination_tcp = struct.unpack("!H", data[2:4])[0]
    let_tcp = struct.unpack("!B", data[12:13])[0] >> 4
    data_tcp = data[let_tcp*4:]

    return f"        +++ Paquet TCP +++\n            Port source      : {port_source_tcp}\n            Port destination : {port_destination_tcp}\n            Longueur en-tête : {let_tcp}\n", data_tcp


def decode_icmp(data) :
    """
    >>> a = decode_icmp(ex_icmp)
    >>> a == "        +++ Paquet ICMP +++\\n            Type             : 5\\n"
    True
    """
    type_data = struct.unpack("!B", data[:1])[0]
    return f"        +++ Paquet ICMP +++\n            Type             : {type_data}\n"


def decode_adresse_IP(addr) :
    """
    >>> decode_adresse_IP(2475088460) == "147.134.218.76"
    True
    """
    binary_addr = bin(addr)[2:]             # On enlève le 0b du début (qui indique que c'est un nombre binaire)
    binary_addr = binary_addr.zfill(32)     # On complète avec des 0 à gauche pour avoir 32 bits à coup sur

    x = binary_addr[0:8]            # 1er octet de l'adresse IP
    y = binary_addr[8:16]           # 2ème octet de l'adresse IP
    z = binary_addr[16:24]          # 3ème octet de l'adresse IP
    t = binary_addr[24:32]          # 4ème octet de l'adresse IP

    return f"{int(x, 2)}.{int(y, 2)}.{int(z, 2)}.{int(t, 2)}"


def decode_ip(data) :
    """
    >>> a = decode_ip(ex_ip)
    >>> len(a) == 3
    True
    >>> a[0] == '    --- Paquet IP ---\\n        Version          : 4\\n        Longueur en-tête : 8\\n        Protocole        : 1\\n        Adresse source   : 234.216.160.229\\n        Adresse dest.    : 76.218.134.147\\n'
    True
    >>> a[1] == 1
    True
    >>> a[2].decode('utf-8') == "cuicui"
    True
    """
    version_ip = struct.unpack("!B", data[:1])[0] >> 4
    let_ip = struct.unpack("!B", data[:1])[0] % 2**4
    protocole_ip = struct.unpack("!B", data[9:10])[0]
    adresse_source_ip = decode_adresse_IP(struct.unpack("!L", data[12:16])[0])
    adresse_dest_ip = decode_adresse_IP(struct.unpack("!L", data[16:20])[0])
    data_ip = data[let_ip*4:]

    infos_ip = f"    --- Paquet IP ---\n        Version          : {version_ip}\n        Longueur en-tête : {let_ip}\n        Protocole        : {protocole_ip}\n        Adresse source   : {adresse_source_ip}\n        Adresse dest.    : {adresse_dest_ip}\n"

    return infos_ip, protocole_ip, data_ip
    

def decode_mac(data) :
    """
    >>> decode_mac(b'R\\x0c\\xc7\\x1d\\xca5') == "52:0c:c7:1d:ca:35"
    True
    """
    addr = struct.unpack("!BBBBBB", data)   # On récupère les 6 octets de l'adresse MAC
    
    # On convertit chaque octet en hexadécimal, on enlève le 0x du début et on complète avec des 0 à gauche pour avoir 2 caractères à coup sur
    a1 = str(hex(addr[0])[2:]).zfill(2)     
    a2 = str(hex(addr[1])[2:]).zfill(2)
    a3 = str(hex(addr[2])[2:]).zfill(2)
    a4 = str(hex(addr[3])[2:]).zfill(2)
    a5 = str(hex(addr[4])[2:]).zfill(2)
    a6 = str(hex(addr[5])[2:]).zfill(2)

    return f"{a1}:{a2}:{a3}:{a4}:{a5}:{a6}"

def decode_Ethernet(data) :
    """
    >>> a = decode_Ethernet(ex_eth)
    >>> len(a) == 3
    True
    >>> a[0] == '>>> Trame Ethernet <<<\\n    Adresse MAC Destination : 52:0c:c7:1d:ca:35\\n    Adresse MAC Source      : 37:38:1f:55:6b:98\\n    Protocol                : 2048\\n'
    True
    >>> a[1] == 2048
    True
    >>> a[2].decode('utf-8') == "coicoi"
    True
    """
    adresse_dest_mac = decode_mac(data[:6])
    adresse_source_mac = decode_mac(data[6:12])
    protocole_eth = struct.unpack("!H", data[12:14])[0]
    data_eth = data[14:]

    infos_eth = f">>> Trame Ethernet <<<\n    Adresse MAC Destination : {adresse_dest_mac}\n    Adresse MAC Source      : {adresse_source_mac}\n    Protocol                : {protocole_eth}\n"

    return infos_eth, protocole_eth, data_eth

def decode_trame(data) :
    # On récupère les données importantes
    infos_eth, protocole_eth, data_eth = decode_Ethernet(data)

    if protocole_eth == 2048:
        print(infos_eth)
        infos_ip, protocole_ip, data_ip = decode_ip(data_eth)

        print(infos_ip)

        # Si le protocole est ICMP
        if protocole_ip == 1:
            print(decode_icmp(data_ip))

        # Si le protocole est TCP
        elif protocole_ip == 6:
            print(decode_tcp(data_ip)[0])
            print(f"Données : {decode_tcp(data_ip)[1].decode('utf-8')}")
        
        # Si le protocole est UDP
        elif protocole_ip == 17:
            print(decode_udp(data_ip)[0])
            print(f"Données : {decode_udp(data_ip)[1].decode('utf-8')}")

        else:
            print(f"Protocole IP inconnu : {protocole_ip}")
    
    else:
        print(f"Protocole Ethernet inconnu : {protocole_eth}")

if __name__ == "__main__" :
    doctest.testmod()
    print("ex_complet1 :")
    decode_trame(ex_complet1)
    print("ex_complet2 :")
    decode_trame(ex_complet2)
    print("ex_complet3 :")
    decode_trame(ex_complet3)