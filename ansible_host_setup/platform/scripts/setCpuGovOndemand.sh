#!/bin/sh
cd ../ && ansible -b -K -m shell -a 'sh emulation/cpugov.sh ondemand' nodes
