#!/bin/bash

python3 -m unittest unitTest_math_functions.py

if [ $? -eq 0 ]; then
	echo "Tests passed"
else
	echo "At least one test failed"
fi

