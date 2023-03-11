import boto3
import json
import os
import yaml


with open("micro-service.yaml", "r") as stream:
    try:
        yaml_file = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
print(yaml_file["metadata"]['cluster'])

DEPLOY_AWS_REGION = os.getenv('DEPLOY_AWS_REGION')
mixed=[]

client = boto3.client("ecs", region_name=DEPLOY_AWS_REGION)
elb = boto3.client("elbv2", region_name=DEPLOY_AWS_REGION)


cluster_name=yaml_file["metadata"]['cluster']
variables=yaml_file["spec"]['code']['environment']

response = client.create_cluster(clusterName=cluster_name)
#print(json.dumps(response, indent=4))

response_register_task_definition = client.register_task_definition(
        containerDefinitions=[
            {
                "name": yaml_file["metadata"]['container_name'],
                "image": yaml_file["spec"]['code']['container_image'] + ":" + yaml_file["spec"]['code']['tag'],
                "cpu": 512,
                "memory": 2048,
                "memoryReservation": 2048,
                "portMappings": [
                    {
                        "containerPort": 8080,
                        "hostPort": 8080,
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
                        "awslogs-group": "ecs",
                        "awslogs-region": "us-east-1",
                        "awslogs-stream-prefix": "ecs"
                    }
                }
            }
        ],
        executionRoleArn=yaml_file["spec"]['code']['executionRoleArn'],
        family=yaml_file["metadata"]['taskdefinition'],
        networkMode="awsvpc",
        requiresCompatibilities= [
            "FARGATE"
        ],
        cpu= "512",
        memory= "2048")
#print(response_register_task_definition["taskDefinition"]["taskDefinitionArn"])

#f = open('infrastructure.json')
#data = json.load(f)
#security_group_id = data['security_group']['value']['id']
#vpc_id = data['vpc']['value']['id']
#subnet_id = data['subnet']['value']['id']
#f.close()




response = client.run_task(
    taskDefinition=response_register_task_definition["taskDefinition"]["taskDefinitionArn"],
    launchType='FARGATE',
    cluster=cluster_name,
    platformVersion='LATEST',
    count=1,
    networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': [
                yaml_file["spec"]['code']['subnet'],
            ],
            'assignPublicIp': 'ENABLED',
            'securityGroups': yaml_file["spec"]['code']['security_group']
        }
    }
)
#print(json.dumps(response, indent=4, default=str))

response = client.create_service(cluster=cluster_name, 
                serviceName=yaml_file["metadata"]['taskdefinition'],
                taskDefinition=response_register_task_definition["taskDefinition"]["taskDefinitionArn"],
                desiredCount=1,
                networkConfiguration={
                    'awsvpcConfiguration': {
                        'subnets': [
                            yaml_file["spec"]['code']['subnet'],
                        ],
                        'assignPublicIp': 'ENABLED',
                        'securityGroups': yaml_file["spec"]['code']['security_group']
                    }
                },
                launchType='FARGATE',
            )
#print(json.dumps(response, indent=4, default=str))






