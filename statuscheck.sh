#!/usr/bin/env bash
######################################################
# Orignally written by: Dave McPherson, 2017
# https://github.com/DMcP89/StorjShareStatusChecker
#######################################################

now=$(date)
log="statuscheck.log"
echo "$now -- Collecting storj stats" > $log

python bin/statuscheck.py

