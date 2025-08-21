from typing import Tuple, Callable, List, Dict

from framework.models.request import Request
from framework.models.body import Body


def create_request_from_bytes(read_data: Callable, body_size_threshold: int) -> Request:

    startline_header_bytes, leftover_body_bytes = read_until_body(read_data)
    startline_header_bytes = startline_header_bytes.decode().split("\n")

    method, route, version = startline_header_bytes[0].split()
    path, query_params_dict = extract_query_params(route)
    headers_dict = extract_headers_dict(startline_header_bytes[1:])
    body = Body.create(
        read_data,
        int(headers_dict.get("content-length", 0)),
        body_size_threshold,
        leftover_body_bytes,
    )
    return Request(
        method=method,
        path=path,
        http_version=version,
        query_params=query_params_dict,
        headers=headers_dict,
        body=body,
    )


def extract_headers_dict(header_list: List[str]) -> Dict[str, str]:
    return {
        split_header[0].lower(): split_header[1]
        for split_header in [header_pair.split(": ") for header_pair in header_list]
    }


def extract_query_params(route: str) -> Tuple[str]:
    if "?" not in route:
        return route, dict()
    path, query_params_str = route.split("?")
    # TODO: add support for multiple values for same param
    query_params = {
        param[0]: [param[1]]
        for param in [elem.split("=") for elem in query_params_str.split("&")]
    }
    return path, query_params


def read_until_body(read_data: Callable) -> Tuple[bytes, bytes]:
    buffer = b""
    while b"\r\n\r\n" not in buffer:
        buffer += read_data()

    return buffer.split(b"\r\n\r\n")
