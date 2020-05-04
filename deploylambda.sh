zip -g lambda.zip lambda-run-job.py
aws lambda update-function-code --function-name run_scrapinghub_job_medium --zip-file fileb://lambda.zip
