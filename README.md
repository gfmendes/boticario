# Proposed solution to Boticario's backend challenge.

## Modules description:
<pre>
cashback/  
|--controller  
   |--business_resources.py > Endpoints related to business logic such as add reseller, list purchases, etc.
   |--login_resources.py > Endpoints related to login and auth token data.
   |--schema_validation.py > Json schema validations for app endpoints.
|--data/  
   |--data_access.py > Abstraction layer between services and data access objects. Data objects changes are transparent to services modules.
   |--mongo_collections.py > Contains logic to access MongoDb collections.
   |--rest_api.py > Contains logic to access external APIs endpoints.
|--services/  
   |--purchase.py > Address purchase business logic. Service layer is independent of framework implementations (such flask, django, pymongo, etc).
   |--reseller.py > Address reseller business logic. service layer is independent of framework implementations (such flask, django, pymongo, etc).
|--app.py > Contains app configs and flask run function.
|--routes.py > Define cachback app routes.  
tests/  
|--integration/  
   |--test_routes.py > Automated end-to-end tests.
|--unit/  
   |--services/  
     |--test_purchase.py > Purchase service unit tests.
     |--test_reseller.py  > Reseller service unit tests.
</pre>

## Running the application:
#Unix
> export FLASK_APP=cashback/app.py  
> flask run

#Windows cmd
> set FLASK_APP=cashback/app.py  
> flask run

#Windows PowerShell
> $env:FLASK_APP="cashback/app.py"  
> flask run

## Running all UT and IT tests:
> python -m unittest discover
  
## Run UT tests from services layer:
> python -m unittest tests/unit/services/test_purchase.py  
> python -m unittest tests/unit/services/test_reseller.py  

## Run IT tests:
> python -m unittest tests/integration/test_routes.py   