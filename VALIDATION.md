# Validation

- 17 tests passed using pytest 8.4.2, Scapy 2.8.0 and Matplotlib 3.9.4.
- Fixed the original synthetic-packet fixtures to encode rates correctly and preserve the RadioTap link type.
- Regression tests verify that multiple legitimate APs are not labelled a confirmed attack in the JSON or plot.
- Generated JSON/CSV and a plot from 240 artificial Beacon frames; no private captured traffic is included.
- The original radio experiments were not rerun in this preparation environment.
- Dependency deprecation warnings remain; no test failures occurred.

## Portfolio code changes

The plot uses per-BSSID labels rather than hard-coded original/attacker identities. JSON reports multiple BSSIDs as an observation, and the comparison script labels heuristic matches as indicators requiring investigation. The legacy report generator was excluded because its template contained unsupported conclusions.
