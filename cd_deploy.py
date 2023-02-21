import boto3
import json
import os
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
                "image": "588338176709.dkr.ecr.us-east-1.amazonaws.com/bar:latest",
#                "containerVersion": "1.1.1",
#                "sigla_sistemica": "siglasistemca",
#                "dd-key": "dd-key",
#                "dd_profiling_enabled": "dd_profiling_enabled",
#                "container_memory_app_fargete":  "container_memory_Reservation_app_name",
#                "container_memoryReservation_app_fargete":  "container_memoryReservation_app_name",
#                "container_cpu_app_fargete":  "container_cpu_app_fargete",
#                "container_cpu_dd_fargete": "container_cpu_dd_fargete",
#                "container_memory_dd_fargete": "container_cpu_app_fargete",
#                "container_bolean_essencial": "true",
#                "env_container": "name-var.env",
#                "log_group": "var.logroup",
#                "env": "env",
#               "region": "var.DEPLOY_AWS_REGION",
#               "client_id": "var.client_id",
#               "client_secret": "var.client_secret",

                "cpu": 256,
                "portMappings": [
                    {
                        "containerPort": 8080,
                        "hostPort": 0,
                        "protocol": "tcp"
                    }
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






response = client.run_task(
    taskDefinition=response_register_task_definition["taskDefinition"]["taskDefinitionArn"],
    launchType='FARGATE',
    cluster=cluster_ecs,
    platformVersion='LATEST',
    count=1,
    networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': [
                'subnet-0e9088435dcb0b49b',
            ],
            'assignPublicIp': 'ENABLED',
            'securityGroups': ["sg-07d75681cf3704d62"]
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
                            'subnet-0e9088435dcb0b49b',
                        ],
                        'assignPublicIp': 'ENABLED',
                        'securityGroups': ["sg-07d75681cf3704d62"]
                    }
                },
                launchType='FARGATE',
            )
#print(json.dumps(response, indent=4, default=str))







