"""LICENSE file in the root directory of this source tree. An additional grant
of patent rights can be found in the PATENTS file in the same directory.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

try:
    from thrift.transport import TSocket
    from thrift.transport import TTransport
    from thrift.protocol import TBinaryProtocol
except ImportError:
    print("Cannot import thrift: pip install thrift")
    exit(1)

from osquery.extensions.ExtensionManager import Client

DEFAULT_SOCKET_PATH = "/var/osquery/osquery.em"
"""The default path for osqueryd sockets"""

class ExtensionClient(object):
    """A client for connecting to an existing extension manager socket"""

    _transport = None

    def __init__(self, path=DEFAULT_SOCKET_PATH, uuid=None):
        """
        Keyword arguments:
        path -- the path of the extension socket to connect to
        uuid -- the additional UUID to use when constructing the socket path
        """
        self.path = path
        if uuid:
            self.path += ".%s" % str(uuid)
        transport = TSocket.TSocket(unix_socket=self.path)
        transport = TTransport.TBufferedTransport(transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self._transport = transport

    def close(self):
        """Close the extension client connection"""
        if self._transport:
            self._transport.close()

    def open(self):
        """Attempt to open the UNIX domain socket"""
        self._transport.open()

    def extension_manager_client(self):
        """Return an extension manager (osquery core) client."""
        return Client(self.protocol)

    def extension_client(self):
        """Return an extension (osquery extension) client."""
        return Client(self.protocol)
