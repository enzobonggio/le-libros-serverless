#!/usr/bin/env bash

find ./lambdas/* -maxdepth 0 -type d -exec bash -c "echo 'Deploying {}...' && cd {} && aws lambda update-function-code --function-name le_libros_{} --zip-file fileb://lambdas/{}/dist/lambda.zip" \;
