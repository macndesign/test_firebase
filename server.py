import sys
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer


def main(handler_class=SimpleHTTPRequestHandler, server_class=BaseHTTPServer.HTTPServer):
    """
    Usage:
    >>> python server.py 127.0.0.1
    Serving HTTP on 127.0.0.1 port 8000 ...
    >>> python server.py 127.0.0.1:9000
    Serving HTTP on 127.0.0.1 port 9000 ...
    >>> python server.py 8080
    Serving HTTP on 0.0.0.0 port 8080 ...
    """

    protocol = "HTTP/1.0"
    host = ''
    port = 8000
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if ':' in arg:
            host, port = arg.split(':')
            port = int(port)
        else:
            try:
                port = int(sys.argv[1])
            except:
                host = sys.argv[1]

    server_address = (host, port)

    handler_class.protocol_version = protocol
    httpd = server_class(server_address, handler_class)

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


if __name__ == "__main__":
    main()
