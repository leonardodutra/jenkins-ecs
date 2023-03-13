#!/bin/bash


../../terraform.exe init --backend-config=./variables/backend.tfvars -reconfigure
../../terraform.exe plan -var-file=variables.tf -lock=false
../../terraform.exe apply -var-file=variables.tf -auto-approve
../../terraform.exe output -json > ./infrastructure.json

aws ecr get-login-password --region sa-east-1 | docker login --username AWS --password-stdin 588338176709.dkr.ecr.sa-east-1.amazonaws.com

docker build -t my-app:latest .

docker tag my-app:latest 588338176709.dkr.ecr.sa-east-1.amazonaws.com/nginx:latest

docker push 588338176709.dkr.ecr.sa-east-1.amazonaws.com/nginx:latest