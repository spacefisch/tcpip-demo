from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
from definitions import SERVER_ADDRESS, SERVER_PORT, AnsiColors
from config import BUFFER_SIZES
from utility import print_protected


def tcp_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    pass


def udp_server():
    server_socket = socket(AF_INET, SOCK_DGRAM)
    bind_address = SERVER_ADDRESS, SERVER_PORT
    server_socket.bind(bind_address)
    bytes_rcvd, sender_addr = server_socket.recvfrom(BUFFER_SIZES)
    print_protected(
        f"{AnsiColors.GREEN}Server: Received {len(bytes_rcvd)} from {sender_addr[0]} "
        f"and port {sender_addr[1]}"
    )
    print_protected(f"{AnsiColors.GREEN}Server: String received: {bytes_rcvd}")
    bytes_sent = server_socket.sendto(bytes_rcvd, sender_addr)
    print_protected(f"{AnsiColors.GREEN}Server: Sent back {bytes_sent} bytes to client")
    server_socket.close()
