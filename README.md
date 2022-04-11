# AWS Lambda container functions

# Testing lambda function

```sh
docker-compose build
docker-compose up
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

- Access to the container for developemnt mode

```sh
docker ps
docker exec -it <CONTAINER ID> bash
# Testing
python -m unittest
```

## Upload container to ECR registry


```sh
export ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
export ECR_REPOSITORY=ffda-poi/test_mercy
export DOCKER_IMAGE=${ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/${ECR_REPOSITORY}:shp2geojson


aws ecr get-login-password --region us-east-1 | docker login \
        --username AWS \
        --password-stdin ${ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com

aws ecr create-repository --repository-name ${ECR_REPOSITORY}
aws ecr describe-repositories | jq .repositories[].repositoryName


docker tag shp2geojson:v1 ${DOCKER_IMAGE}
docker push ${DOCKER_IMAGE}

```


## Execute Lambda function