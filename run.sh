#!/usr/bin/env bash

set -e
echo "Year $1 Day $2"
echo "Example Input:"
python $1/day_$2/input{.py,_example}
echo "Input:"
python $1/day_$2/input{.py,}
