#!/bin/sh
cd ../ && ansible -m shell -a 'sh emulation/cpugov.sh' nodes