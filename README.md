# Proposed solution to Boticario's backend challenge.

## Modules description:
<pre>
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
</pre>

## Running the application:
#(unix)
> export FLASK_APP=cashback/app.py  
> flask run

#Windows cmd
> set FLASK_APP=cashback/app.py  
> flask run

#Windows powershell
> $env:FLASK_APP="cashback/app.py"  
> flask run

## Running all UT and IT tests:
  python -m unittest discover
  
## Run UT tests from services layer:
  python -m unittest tests/unit/services/test_purchase.py  
  python -m unittest tests/unit/services/test_reseller.py  

## Run IT tests:
  python -m unittest tests/integration/test_routes.py   