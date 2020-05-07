clean:
	rm -drf ./lambda-package

package: clean
	pip install -r requirements.txt --target ./lambda-package
	cp scraping2dynamo.py ./lambda-package
	rm -rf ./function_package.zip
	cd lambda-package; zip -r ../function_package.zip *

lambda-create: package
	aws lambda create-function --function-name scraping2dynamo --runtime python3.8 --role ${LAMBDA_BASIC_ROLE} --handler scraping2dynamo.handler --zip-file fileb://function_package.zip

deploy: package	
	aws lambda update-function-code --function-name scraping2dynamo --zip-file fileb://function_package.zip
