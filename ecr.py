import boto3

ecr_client = boto3.client('ecr')

repository_Name='monitoring_repo'
response = ecr_client.create_repository(repositoryName=repository_Name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)
