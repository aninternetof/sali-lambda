#!/bin/bash
rm lambda.zip
cwd=$(pwd)
pushd venv/lib/python3.6/site-packages
zip -r9 $cwd/lambda.zip *
popd
zip -g lambda.zip lambda.py