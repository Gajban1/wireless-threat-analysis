# Findings and limitations

## Evidence reviewed

This summary was prepared from the local academic project's scripts, experiment logs, report and exported comparison results. It does not independently reproduce the radio experiments.

- An exported comparison contains 18 IE categories, with 15 marked different, and about 20 dBm difference in average RSSI.
- Experiment notes report lab-client connectivity through an Evil Twin and a simulated captive-portal interaction.
- KARMA/MANA results were partial; observing probe exchanges is not evidence that a device joined or that its application traffic was decrypted.
- TLS SNI observations exposed some destination names in the tested captures. This does not demonstrate HTTPS payload decryption or a universal ability to observe domains.

## Interpretation

These are investigation heuristics, not proof of maliciousness. Enterprise networks routinely advertise one SSID from multiple APs. RSSI depends on position, transmit power and interference; IE differences can be legitimate. Sequence numbers are not an immutable hardware identity.

The original documentation included stronger claims of certainty. This portfolio does not repeat those claims. No representative benign dataset, sensitivity, specificity or false-positive benchmark is supplied.

## Scope and attribution

Original academic project: Piotr Straszak and Hubert Czernicki. Practical experiments were conducted by Piotr Straszak with AI assistance, as described by the portfolio owner. The repository separates reusable offline analysis from raw operational material.

## Changes in the portfolio edition

- Added English introduction, contribution statement and reproducible usage instructions.
- Excluded raw logs/captures, memory files, installed dependencies and third-party attack tooling.
- Relabelled conclusive Evil Twin verdicts as investigation indicators.
