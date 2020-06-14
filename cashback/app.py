from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from cashback.routes import init_routes

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret-string'
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)
jwt = JWTManager(app)

init_routes(api)

if __name__ == "__main__":
    app.run(debug=True)