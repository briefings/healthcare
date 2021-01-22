#!/bin/bash

# A script file for Google Colaboratory


# cleaning-up
rm -rf *.log && rm -rf *.pdf && rm -rf *.zip
rm -rf phe
rm -rf config.py


# dask
pip install dask[complete] &> dask.log


# https://linux.die.net/man/1/wget
wget -q https://raw.githubusercontent.com/briefings/phe/develop/config.py
wget -q https://github.com/briefings/phe/raw/develop/phe.zip


# https://linux.die.net/man/1/unzip
# -u: update
# -q: quiet
unzip -u -q phe.zip
rm -rf phe.zip