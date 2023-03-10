#!/bin/bash


../../terraform.exe init --backend-config=backend.tfvars -reconfigure
../../terraform.exe plan -var-file=var.tfvars -lock=false
../../terraform.exe apply -var-file=var.tfvars -auto-approve
../../terraform.exe output -json > ./infrastructure.json

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 34243243242342.dkr.ecr.us-east-1.amazonaws.com

docker build -t devsecops/jenkins-master .

docker tag devsecops/jenkins-master:latest 31232132321321.dkr.ecr.us-east-1.amazonaws.com/bar:latest

docker push 32322332131232.dkr.ecr.us-east-1.amazonaws.com/bar:latest
 32352353535253.dkr.ecr.us-east-1.amazonaws.com/bar:latest