# Zadanie 1 - SIP proxy
# Autor: Samuel Bernat 
# Datum: 25.2.2022
# Predmet: MTAA
# Zdroj libky: https://github.com/tirfil/PySipFullProxy/blob/master/sipfullproxy.py


from sipfullproxy import *
import socketserver



HOSTNAME = socket.gethostname()
LOCAL_IP = socket.gethostbyname(HOSTNAME)
PORT = 5060

print("Local IP: ", LOCAL_IP)
print ("Port: ", PORT)



def main ():
    ip = input("Enter IP adress of your PC in local network: ")

    main_init(ip, PORT)
    server = socketserver.UDPServer(("0.0.0.0", PORT), UDPHandler)
    server.serve_forever()
main()
