#!/data/data/com.termux/files/usr/bin/python
import socket
import ssl

def check_ssl_simple(host, port):
    # Обычный сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.00000000000001) # Маленький таймаут для экономии батареи

    # Настройка SSL
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    try:
        # Сначала простое TCP соединение
        sock.connect((host, port))
        # Пробуем "натянуть" SSL поверх сокета
        ssl_sock = ctx.wrap_socket(sock, server_hostname=host)
        print(f"[+] SSL открыт на порту: {port}")
        ssl_sock.close()
    except:
        # Если порт закрыт или не SSL
        pass
    finally:
        sock.close()

# Проверяем порты по очереди
target = "127.0.0.1"
targetone = "192.168.0.1"
targettwo = "192.168.1.1"
targettree = "192.168.31.1"
targetfour = "fe80::1"
targetfive = "fd21::1"
targetsix = "ff02::1"
targetseven = "169.254.187.0"
targeteight = "169.254.189.0"
targetnine = "255.255.255.0"
targetten = "169.254.186.0"
targeteleven = "255.255.0.0"
targettwelve = "255.255.255.255"
targettherteen = "255.0.0.0"
for p in range(1, 65535):
    check_ssl_simple(target, p)
    check_ssl_simple(targetone, p)
    check_ssl_simple(targettwo, p)
    check_ssl_simple(targettree, p)
    check_ssl_simple(targetfour, p)
    check_ssl_simple(targetfive, p)
    check_ssl_simple(targetsix, p)
    check_ssl_simple(targetseven, p)
    check_ssl_simple(targeteight, p)
    check_ssl_simple(targetnine, p)
    check_ssl_simple(targetten, p)
    check_ssl_simple(targeteleven, p)
    check_ssl_simple(targettwelve, p)
    check_ssl_simple(targettherteen, p)
