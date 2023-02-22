import binascii
import struct # pour unpack
import syntaxe
import socket

def analyse_semantique(trame):
    """
    Analyse une trame Ethernet :  cf https://fr.wikipedia.org/wiki/Ethernet    
    Input : trame est un tableau d'octets
    """
    print("-"*60)
    print ("\nTrame Ethernet en cours d'analyse ({}): \n{} ... ".format( type(trame), trame[0:10]))
  
    # Analyse du header ETHERNET
    eth_header = trame[0:14]
    #print(eth_header)
    eth_mac_dest, eth_mac_src, eth_type = struct.unpack('!6s6sH' , eth_header) #  https://docs.python.org/fr/3/library/struct.html
    
    print ('Destination MAC : {}'.format(eth_mac_dest.hex(":"))) # .hex() ssi Python > 3.8
    print ('Source MAC \t: {}'.format(binascii.hexlify(eth_mac_src)))

    #https://stackoverflow.com/questions/4959741/python-print-mac-address-out-of-6-byte-string

    ##########################################################
    
    if hex(eth_type) == '0x800':
        print("Type de trame \t: IPv4")
    else:
        print("Type de trame \t: {}".format(hex(eth_type)))
    
    eth_IPvX = trame[22:34]
    ttl, protocole, caca, ip_source, ip_dest = struct.unpack('!BBH4s4s', eth_IPvX)
    
    print("TTL \t\t: {}".format(ttl))
    print("Protocole \t: {}".format(protocole))
    print("IP source \t: {}".format(socket.inet_ntoa(ip_source)))
    print("IP destination \t: {}".format(socket.inet_ntoa(ip_dest)))

#=================================================================
if __name__ == '__main__':
    filename = "tramz.txt"
    # Analyse syntaxique
    lestrames = syntaxe.analyse_syntaxique(filename)
    # Analyse sémantique 
    for trame in lestrames:
        analyse_semantique(trame)        
