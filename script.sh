#!/bin/bash

# A script file for Google Colaboratory

# logs
rm -rf *.log && rm -rf *.pdf && rm -rf *.zip

# dask
pip install dask[complete] &> dask.log

# https://linux.die.net/man/1/wget
wget -q https://github.com/briefings/phe/raw/develop/phe.zip

# https://linux.die.net/man/1/unzip
# -u: update
# -q: quiet
rm -rf phe
unzip -u -q phe.zip
rm -rf phe.zip