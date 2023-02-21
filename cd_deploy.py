import boto3
import json
import os
import json
#Variaveis do projeto
cluster_ecs="MeuClusterECS"

DEPLOY_AWS_REGION = os.getenv('DEPLOY_AWS_REGION')

client = boto3.client("ecs", region_name=DEPLOY_AWS_REGION)
response = client.create_cluster(clusterName=cluster_ecs)
#print(json.dumps(response, indent=4))

response_register_task_definition = client.register_task_definition(
        containerDefinitions=[
            {
                "name": "AmazonSampleImage",
                "image": "543443381312376709.dkr.ecr.us-east-1.amazonaws.com/bar:latest",
                "cpu": 256,
                "portMappings": [
                ],
                "essential": True,
                "environment": [],
                "mountPoints": [],
                "volumesFrom": [],
                "logConfiguration": {
                    "logDriver": "awslogs",
                    "options": {
                        "awslogs-group": "/ecs/AWSSampleApp",
                        "awslogs-region": "us-east-1",
                        "awslogs-stream-prefix": "ecs"
                    }
                }
            }
        ],
        executionRoleArn="arn:aws:iam::588338176709:role/test_role",
        family= "AWSSampleApp2",
        networkMode="awsvpc",
        requiresCompatibilities= [
            "FARGATE"
        ],
        cpu= "256",
        memory= "512")
#print(response_register_task_definition["taskDefinition"]["taskDefinitionArn"])

f = open('infrastructure.json')
data = json.load(f)
security_group_id = data['security_group']['value']['id']
vpc_id = data['vpc']['value']['id']
subnet_id = data['subnet']['value']['id']
f.close()




response = client.run_task(
    taskDefinition=response_register_task_definition["taskDefinition"]["taskDefinitionArn"],
    launchType='FARGATE',
    cluster=cluster_ecs,
    platformVersion='LATEST',
    count=1,
    networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': [
                subnet_id,
            ],
            'assignPublicIp': 'ENABLED',
            'securityGroups': [security_group_id]
        }
    }
)
#print(json.dumps(response, indent=4, default=str))

response = client.create_service(cluster=cluster_ecs, 
                serviceName="SimpleWebServer",
                taskDefinition=response_register_task_definition["taskDefinition"]["taskDefinitionArn"],
                desiredCount=2,
                networkConfiguration={
                    'awsvpcConfiguration': {
                        'subnets': [
                            subnet_id,
                        ],
                        'assignPublicIp': 'ENABLED',
                        'securityGroups': [security_group_id]
                    }
                },
                launchType='FARGATE',
            )
#print(json.dumps(response, indent=4, default=str))






