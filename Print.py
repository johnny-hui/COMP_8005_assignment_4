from tabulate import tabulate
from constants import *
from constants import ZERO, NONE, GRID


def _print_header():
    print("==========================================================================================="
          "==============================")
    print(f"{PPID_HEADER:<10}{PID_HEADER:<10}{COMM_HEADER:<30}{CMDLINE_HEADER:<5}")
    print("==========================================================================================="
          "==============================")


def print_processes(ppid: str, pid: str,
                    comm: str, cmdline: str,
                    fd_list: list):
    table_header = [f"{FD_HEADER} PID: {pid})", TYPE_HEADER, PORT_HEADER]

    if len(fd_list) is ZERO:
        fd_list.append([NONE])

    _print_header()
    print(f"{ppid:<10}{pid:<10}{comm:<30}{cmdline:<5}")
    print(tabulate(fd_list, table_header, GRID))
