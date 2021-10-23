#!/usr/bin/env bash

aws lambda update-function-code --function-name le_libros_$1 --zip-file fileb://lambdas/$1/dist/lambda.zip