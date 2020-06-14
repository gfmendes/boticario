Running the application:
1) Set FLASK_APP env property:
  export FLASK_APP=app/run.py #unix
  set FLASK_APP=app/run.py #windows
  $env:FLASK_APP = "app/run.py" #windows
2) Run flask:  
  flask run

Running all tests:
  python -m unittest discover