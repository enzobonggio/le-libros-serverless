#!/usr/bin/env bash

find ./lambdas/* -maxdepth 0 -type d -exec bash -c "cd {} && make" \;