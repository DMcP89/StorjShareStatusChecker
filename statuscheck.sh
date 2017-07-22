#!/usr/bin/env bash
######################################################
# Orignally written by: Dave McPherson, 2017
# https://github.com/DMcP89/StorjShareStatusChecker
#######################################################

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
now=$(date)

log="statuscheck.log"

echo "$now -- Collecting storj stats" > $log

stats=$(/usr/local/bin/storjshare status -j)
#echo $stats

python $DIR/bin/statuscheck.py "$stats"

