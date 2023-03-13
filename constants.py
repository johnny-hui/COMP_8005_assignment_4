# GENERAL CONSTANTS
ZERO = 0
NONE = "None"
NOT_AVAILABLE = "N/A"


# I/O CONSTANTS
PROC_DIRECTORY = "/proc"
CMD_LINE = "cmdline"
COMM = "comm"
STATUS = "status"
FD = "fd"
PID = "Pid:"
PPID = "PPid"


# ERROR CONSTANTS
USER_NOT_ROOT_ERROR = "[+] ERROR: Only the 'root' user can run this script!\n" \
                      "[+] Please run this script again using sudo command."


# PRINT CONSTANTS
PPID_HEADER = "PPID"
PID_HEADER = "PID"
COMM_HEADER = "COMM"
CMDLINE_HEADER = "CMDLINE"
FD_HEADER = "File Descriptors (Files Opened by"


# TABULATE CONSTANTS
GRID = "simple_grid"
TYPE_HEADER = "Type"
PORT_HEADER = "Listening on Port\n(Only Applicable to Sockets)"


# FD CONSTANTS
ANON_INODE = "Anonymous inode"
IPC_SOCKET = "IPC (Inter-process Communication) Socket"
NETWORK_SOCKET = "Network Socket"
MEM_FD = "Memory File Descriptor"
PIPE = "Pipe"
FILE = "File"
ANON_INODE_MATCH = "anon_inode"
SOCKET_MATCH = "socket"
MEM_FD_MATCH = "/memfd"
PIPE_MATCH = "pipe"


# LSOF CONSTANTS
IPv4 = "IPv4"
IPv6 = "IPv6"
UNIX = "unix"
SOCK = "sock"
ESTABLISHED_LSOF = "(ESTABLISHED)"
LISTEN_LSOF = "(LISTEN)"
UDP_LSOF = "UDP"
TCP_LSOF = "TCP"
LSOF_GET_ACTIVE_SOCKETS_CMD = "sudo lsof -i -n"
