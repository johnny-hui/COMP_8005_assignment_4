import os
import constants
from constants import *


class SymbolicLinkHandler:
    def __init__(self):
        pass

    @staticmethod
    def type_checker(sym_link: str):
        fd_type = sym_link.split(" ")[2].split(":")[0]

        match fd_type:
            case constants.ANON_INODE_MATCH:
                fd_type = ANON_INODE
            case constants.SOCKET_MATCH:
                fd_type = NETWORK_SOCKET
            case constants.MEM_FD_MATCH:
                fd_type = MEM_FD
            case constants.PIPE_MATCH:
                fd_type = PIPE
            case _:
                fd_type = FILE

        return fd_type

    @staticmethod
    def get_socket_id(sym_link: str):
        filtered_sym_link = sym_link.split(" ")[2].split(":")

        if filtered_sym_link[0] == SOCKET_MATCH:  # ['socket', '[XXXXX]']
            return filtered_sym_link[1].replace("[", "").replace("]", "")
        else:
            return None

    @staticmethod
    def port_checker(lsof_list: list[str], sock_id: str, path: str):
        pid = path.split("/")[2]
        socket_type = ""
        port = NOT_AVAILABLE

        for line in lsof_list:
            parsed_line = line.strip().split(" ")[len(line.strip().split(" ")) - 2:]

            if line.strip().split(" ").count(pid) and line.strip().split(" ").count(sock_id):
                port = SymbolicLinkHandler._lsof_parser(parsed_line, port)
                return NETWORK_SOCKET, port
            else:
                socket_type = IPC_SOCKET

        return socket_type, port

    @staticmethod
    def _lsof_parser(parsed_line, port):
        if parsed_line.count(ESTABLISHED_LSOF):
            parsed_line.remove(ESTABLISHED_LSOF)

        if parsed_line.count(LISTEN_LSOF):
            parsed_line.remove(LISTEN_LSOF)

        if parsed_line.count(UDP_LSOF):
            parsed_line.remove(UDP_LSOF)

        if parsed_line.count(TCP_LSOF):
            parsed_line.remove(TCP_LSOF)

        port = parsed_line[ZERO].split(":")[len(parsed_line[ZERO].split(":")) - 1]
        return port

    @staticmethod
    def get_lsof_list():
        stream = os.popen(LSOF_GET_ACTIVE_SOCKETS_CMD)
        output = stream.readlines()[1:]

        return output



