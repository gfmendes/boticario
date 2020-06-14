Running the application:
1) Set FLASK_APP env property:
  export FLASK_APP=cashback/app.py #unix
  set FLASK_APP=cashback/app.py #windows
  $env:FLASK_APP="cashback/app.py" #windows
2) Run flask:  
  flask run

Running all UT and IT tests:
  python -m unittest discover
  
Run UT tests from services layer:
  python -m unittest tests/unit/services/test_purchase.py  
  python -m unittest tests/unit/services/test_reseller.py  

Run IT tests:
  python -m unittest tests/integration/test_routes.py   