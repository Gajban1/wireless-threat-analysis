"""Regression: multiple APs are an observation, not a confirmed attack."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skrypty"))
from scapy.all import RadioTap, Dot11, Dot11Beacon, Dot11Elt
import analyze_pcap as analyzer

def test_multiple_legitimate_aps_do_not_claim_confirmed_attack(tmp_path):
    frames = []
    for mac in ["02:00:00:00:00:01", "02:00:00:00:00:02"]:
        frames.append(RadioTap() / Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=mac, addr3=mac) / Dot11Beacon() / Dot11Elt(ID=0, info=b"OfficeWiFi"))
    aps = analyzer._analyze_packets(frames, "OfficeWiFi")
    out = tmp_path / "analysis.json"
    analyzer._export_json(aps, str(out), "OfficeWiFi")
    metadata = json.loads(out.read_text())["metadata"]
    assert metadata["multiple_bssids_for_ssid"] is True
    assert "evil_twin_detected" not in metadata
    assert "inwentarz legalnych AP" in analyzer._format_report(aps, "OfficeWiFi")


def test_plot_does_not_assign_attacker_identity(monkeypatch, tmp_path):
    import matplotlib.figure
    frames = []
    for mac in ["02:00:00:00:00:01", "02:00:00:00:00:02"]:
        frames.append(RadioTap() / Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=mac, addr3=mac) / Dot11Beacon() / Dot11Elt(ID=0, info=b"OfficeWiFi"))
    aps = analyzer._analyze_packets(frames, "OfficeWiFi")
    labels = []
    def inspect_figure(fig, *args, **kwargs):
        for ax in fig.axes:
            labels.extend(t.get_text() for t in ax.texts)
            if ax.get_legend():
                labels.extend(t.get_text() for t in ax.get_legend().get_texts())
    monkeypatch.setattr(matplotlib.figure.Figure, "savefig", inspect_figure)
    analyzer._generate_plot(aps, str(tmp_path / "preview.png"), "OfficeWiFi", "synthetic")
    joined = " ".join(labels)
    assert "EVIL TWIN CONFIRMED" not in joined
    assert "Evil Twin AP" not in joined
    assert "Multiple APs can be legitimate" in joined
    assert "02:00:00:00:00:01" in joined
