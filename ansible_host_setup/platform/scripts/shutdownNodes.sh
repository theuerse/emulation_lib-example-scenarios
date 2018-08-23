#!/bin/sh
cd ../ && ansible -b -K -m shell -a 'shutdown -h now' nodes
