# dh-event-extractor

dh-event-extractor is a lambda function that is used in [Dihome project](https://github.com/grami1/dihome). 
The lambda extracts events from SQS and stores them to DynamoDB.
The deployment is done via terraform in [dh-infra](https://github.com/grami1/dh-infra/tree/main/terraform/lambda) project.

## Create zip for deployment
``zip -r extractor.zip handler.py``
