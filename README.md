# Wireless Threat Analysis

Academic Wi-Fi security project: offline analysis of Beacon frames to investigate possible Evil Twin / rogue access points.

**Portfolio owner:** Piotr Straszak · Cybersecurity, AGH University of Krakow
**Stack:** Python, Scapy, Matplotlib, Wireshark, Kali Linux

## What this demonstrates

- Extracting access-point characteristics from 802.11 packet captures.
- Comparing Information Elements, RSSI and sequence numbers across BSSIDs.
- Exporting findings as JSON, CSV and plots for investigation.
- Reporting experimental observations separately from conclusions and limitations.

## My contribution and project provenance

Piotr Straszak conducted the practical laboratory work and used an AI agent (CodeWhale with the DeepSeek API) to assist experiment execution, code and analysis. This is not presented as entirely manually written software or as a benchmark of autonomous AI performance.

The original academic project credits **Piotr Straszak and Hubert Czernicki**. Original repository: [Hose-Zur/BBSK-Evil-Twin](https://github.com/Hose-Zur/BBSK-Evil-Twin). The original MIT license is retained.

This curated portfolio snapshot includes the analysis scripts and existing tests. Raw captures, logs, device identifiers, test passwords, third-party attack tooling and bundled dependencies have been omitted. The original local project is unchanged.

## Run the offline analysis

Python 3.10+ is recommended. From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python skrypty/analyze_pcap.py /path/to/authorised-capture.pcap LabNetwork --json --csv -o wyniki/
python skrypty/beacon_diff.py /path/to/authorised-capture.pcap LabNetwork --json --markdown -o wyniki/
python -m pytest tests/ -q
```

Captures are not included. Use an authorised laboratory capture. Analysis scripts operate on files; capturing traffic or running attack tooling is outside this portfolio package.

## Preview

[View a synthetic example and analysis plot](examples/README.md). The example contains artificial frames, not private lab traffic.

## Laboratory findings

The original lab compared an authorised access point and a lab-controlled Evil Twin. One exported comparison recorded differences in 15 of 18 compared Information Element categories and approximately 20 dBm RSSI difference. These describe that particular capture, not general detection accuracy.

Evil Twin connectivity and a simulated captive portal were exercised. KARMA/MANA trials produced partial observations and configuration limitations. TLS ClientHello SNI exposed some destination domains in the tested traffic; HTTPS payload decryption was **not demonstrated**.

See [findings and limitations](docs/findings-and-limitations.md).

## Limitations

Multiple BSSIDs sharing an SSID are normal in many legitimate networks. RSSI and Information Element differences alone do not establish an attack. Sequence numbers wrap and can be manipulated. Findings require an authorised AP inventory and contextual investigation. No production detection accuracy or false-positive rate was measured.

## Files

- `skrypty/analyze_pcap.py`: Beacon extraction, summary, JSON/CSV and plots.
- `skrypty/beacon_diff.py`: per-AP Information Element comparison.
- `tests/`: existing tests using generated packet data.

## License

MIT; see [LICENSE](LICENSE). Original contributors remain credited.
