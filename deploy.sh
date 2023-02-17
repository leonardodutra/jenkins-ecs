#!/bin/bash
./terraform init --backend-config=backend.tfvars -reconfigure
./terraform plan -var-file=var.tfvars -lock=false
./terraform apply -var-file=var.tfvars -auto-approve



aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 588338176709.dkr.ecr.us-east-1.amazonaws.com

docker build -t devsecops/jenkins-master .

docker tag devsecops/jenkins-master:latest 588338176709.dkr.ecr.us-east-1.amazonaws.com/bar:latest

docker push 588338176709.dkr.ecr.us-east-1.amazonaws.com/bar:latest
 588338176709.dkr.ecr.us-east-1.amazonaws.com/bar:latest
