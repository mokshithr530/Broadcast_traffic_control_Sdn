from config import BROADCAST_THRESHOLD
from utils import is_broadcast

broadcast_count = 0

def handle_broadcast(dst_mac):
    global broadcast_count

    if is_broadcast(dst_mac):
        broadcast_count += 1

        if broadcast_count > BROADCAST_THRESHOLD:
            return "DROP"
        else:
            return "ALLOW"

    return "NORMAL"