import datetime

from modernrpc.core import rpc_method


@rpc_method()
def get_true():
    return True


@rpc_method()
def get_false():
    return False


@rpc_method()
def get_null():
    return None


@rpc_method()
def get_int():
    return 42


@rpc_method()
def get_negative_int():
    return -42


@rpc_method()
def get_float():
    return 3.14


@rpc_method()
def get_string():
    return "abcde"


@rpc_method()
def get_bytes():
    return b"abcde"


@rpc_method()
def get_date():
    return datetime.datetime(1987, 6, 2, 8, 45, 00)


@rpc_method()
def get_data_type(data):
    """Returns a string representation of input argument type"""
    return str(type(data))


@rpc_method()
def get_list():
    return [1, 2, 3]


@rpc_method()
def get_struct():
    return {
        'x': 1,
        'y': 2,
        'z': 3
    }
