﻿# aws-lambda-downloader
 
 A lambda function to download an external file (in this case the UK Government data on Covid 19), convert to a CSV, and upload to an S3 bucket for further processing.
 
 ## Intallation
 Using lambda functions with external dependencies is a bit of a pain.
 
 Use the command to package up the lambda function (on a linux based system):
 ```
 pip install requirements.txt -t ./package
 cd package
 zip -r9 ../function.zip .
 cd ..
 zip function.zip lambda_function.py
 ```
 
 Create the lambda function with the AWS CLI:
 ```
 aws lambda create-funciton --function-name [function_name] --zip-file fileb://function.zip
```
 Update the function with the AWS CLI:
 ```
 aws lambda update-function-code --function-name [function_name] --zip-file fileb://function.zip
 ```
