#!/usr/bin/env bash

export PYTHONPATH=${PYTHONPATH}:/home/pi-gateway/mobilityEmulationTestbed/

#python3 testbed_scenario.py
python3 onlyNdnDemoApps.py
python3 onlyNdnDemoAppsWLDR.py

