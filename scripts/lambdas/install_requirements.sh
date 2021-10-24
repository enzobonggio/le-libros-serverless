#!/usr/bin/env bash

find ./lambdas/* -maxdepth 0 -type d -exec bash -c "cd {} && pip3 install -r requirements.txt" \;
