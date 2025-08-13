import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.listener import Listener

with Listener('localhost', 8000) as listener:
    listener.run()