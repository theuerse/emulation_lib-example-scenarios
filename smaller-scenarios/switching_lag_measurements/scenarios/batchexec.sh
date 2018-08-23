#!/usr/bin/env bash

export PYTHONPATH=${PYTHONPATH}:/home/theuers/ndnSIM_2.3/MobilityEmulation/emulation_python/

python3 baseline_10Mbps.py
python3 symmetric_intervals.py
python3 symmetric_double.py
python3 symmetric.py
python3 symmetric_half.py
python3 symmetric_twoFlows.py
