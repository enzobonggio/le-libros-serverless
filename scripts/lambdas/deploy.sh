#!/usr/bin/env bash

deploy() {
  echo $1
  local lambda_name=$(basename $1)
  echo "Deploying $lambda_name..."
  aws lambda update-function-code --function-name le_libros_$lambda_name --zip-file fileb://$1/dist/lambda.zip
  echo "Deployed $lambda"
}

for lambda_path in lambdas/* ; do
    deploy $lambda_path &
done

