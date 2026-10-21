"""Generate a reproducible preview from artificial frames, not captured traffic."""
from pathlib import Path
import sys
from scapy.all import RadioTap, Dot11, Dot11Beacon, Dot11Elt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skrypty'))
import analyze_pcap as analysis

frames = []
for device in range(2):
    mac = f'02:00:00:00:00:0{device + 1}'
    for i in range(120):
        packet = (
            RadioTap(present='dBm_AntSignal', dBm_AntSignal=-45-device*8+(i%5)-2)
            / Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=mac,
                    addr3=mac, SC=((i + device * 1000) % 4096) << 4)
            / Dot11Beacon()
            / Dot11Elt(ID=0, info=b'Demo-Office-WiFi')
            / Dot11Elt(ID=1, info=bytes([0x82, 0x84, 0x8b, 0x96]))
            / Dot11Elt(ID=3, info=bytes([6]))
        )
        packet.time = 1700000000 + i * 0.1 + device * 0.01
        frames.append(packet)
aps = analysis._analyze_packets(frames, 'Demo-Office-WiFi')
base = ROOT / 'examples'
analysis._export_json(aps, str(base / 'synthetic-analysis.json'), 'Demo-Office-WiFi')
analysis._export_csv(aps, str(base / 'synthetic-analysis.csv'))
analysis._generate_plot(aps, str(base / 'synthetic-analysis.png'),
                        'Demo-Office-WiFi', 'SYNTHETIC - two legitimate APs')
