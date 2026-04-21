from ryu.lib.packet import packet, ethernet
from broadcast_control import handle_broadcast
from flow_manager import add_flow

def handle_packet_in(app, msg):
    datapath = msg.datapath
    parser = datapath.ofproto_parser
    ofproto = datapath.ofproto

    pkt = packet.Packet(msg.data)
    eth = pkt.get_protocol(ethernet.ethernet)

    dst = eth.dst
    src = eth.src
    in_port = msg.match['in_port']

    decision = handle_broadcast(dst)

    if decision == "DROP":
        print("Dropping broadcast packet")
        return

    actions = [parser.OFPActionOutput(ofproto.OFPP_FLOOD)]

    match = parser.OFPMatch(in_port=in_port, eth_dst=dst)

    add_flow(datapath, 1, match, actions)

    out = parser.OFPPacketOut(
        datapath=datapath,
        buffer_id=msg.buffer_id,
        in_port=in_port,
        actions=actions,
        data=msg.data
    )
    datapath.send_msg(out)