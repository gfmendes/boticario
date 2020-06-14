# Proposed solution to Boticario's backend challenge.

## Modules description:
cashback/  
|--controller  
   |--business_resources.py   
   |--login_resources.py  
   |--schema_validation.py  
|--data/  
   |--data_access.py  
   |--mongo_collections.py  
   |--rest_api.py  
|--services/  
   |--purchase.py  
   |--reseller.py  
|--app.py  
|--routes.py  
tests/  
|--integration/  
   |--test_routes.py  
|--unit/  
   |--services/  
     |--test_purchase.py  
     |--test_reseller.py  


## Running the application:
1) Set FLASK_APP env property:
  (unix) export FLASK_APP=cashback/app.py 
  (windows) set FLASK_APP=cashback/app.py #windows
  (windows) $env:FLASK_APP="cashback/app.py" #windows
2) Run flask:  
  flask run

## Running all UT and IT tests:
  python -m unittest discover
  
## Run UT tests from services layer:
  python -m unittest tests/unit/services/test_purchase.py  
  python -m unittest tests/unit/services/test_reseller.py  

## Run IT tests:
  python -m unittest tests/integration/test_routes.py   