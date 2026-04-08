from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer
from pox.lib.util import dpid_to_str

log = core.getLogger()

connections = {}

def _handle_ConnectionUp(event):
    log.info("Switch %s connected", dpid_to_str(event.dpid))
    connections[event.dpid] = event.connection

def _handle_ConnectionDown(event):
    if event.dpid in connections:
        log.info("Switch %s disconnected", dpid_to_str(event.dpid))
        del connections[event.dpid]

def request_stats():
    for dp in connections.values():
        dp.send(of.ofp_stats_request(body=of.ofp_flow_stats_request()))
        dp.send(of.ofp_stats_request(body=of.ofp_port_stats_request()))

def _handle_FlowStatsReceived(event):
    log.info("\n=== FLOW STATS from %s ===", dpid_to_str(event.connection.dpid))
    log.info("%-30s %-10s %-10s", "Match", "Packets", "Bytes")

    for stat in event.stats:
        log.info("%-30s %-10d %-10d",
                 str(stat.match),
                 stat.packet_count,
                 stat.byte_count)

        # Simple alert
        if stat.packet_count > 50:
            log.info("⚠ HIGH TRAFFIC FLOW DETECTED!")

def _handle_PortStatsReceived(event):
    log.info("\n=== PORT STATS from %s ===", dpid_to_str(event.connection.dpid))

    for stat in event.stats:
        log.info("Port %d | RX: %d | TX: %d",
                 stat.port_no,
                 stat.rx_packets,
                 stat.tx_packets)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("ConnectionDown", _handle_ConnectionDown)
    core.openflow.addListenerByName("FlowStatsReceived", _handle_FlowStatsReceived)
    core.openflow.addListenerByName("PortStatsReceived", _handle_PortStatsReceived)

    # Poll every 5 seconds
    Timer(5, request_stats, recurring=True)
