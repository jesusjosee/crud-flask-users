from flask import Flask, make_response, request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
# flask config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Swagger config
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Lexmax API',
    description='CRUD User API',
)
ns = api.namespace('api', description='Users operations Api')


#db conection
db = SQLAlchemy(app)
from models import User

model_user = api.model('User', {
    'id': fields.Integer(readonly=True, description='The user identifier'),
    'name': fields.String(required=True, description='The name'),
    'lastname': fields.String(required=True, description='The lastname'),
    'email': fields.String(required=True, description='The email') ,
    'address': fields.String( description='The address'), 
    'reference_address': fields.String(description='The reference address'),
    'phone_number': fields.String( description='The phone number')
})

@ns.route('/users/')
class UserList(Resource):
    '''Shows a list of all Users, and lets you POST to add new User'''

    @ns.doc('list_users')
    # @ns.marshal_list_with(model_user)
    def get(self):
        '''List all Users'''
        query = User.query.all()
        users = []
        for user in query:
            u = {
                'id': user.id,
                'name': user.name,
                'lastname': user.lastname,
                'email': user.email,
                'address': user.address,
                'reference_address': user.reference_address,
                'phone_number': user.phone_number
            }
            users.append(u)

        return  jsonify(users)


    @ns.doc('create_user')
    @ns.expect(model_user)
    def post(self):
        '''Create a new User'''
        
        data = request.get_json()
        user = [ user for user in User.query.all() if user.email == data['email']]
        if user:
            return {"message": "User already exists"}, 404

        user = User( 
                        name=data['name'], 
                        lastname=data['lastname'], 
                        email=data['email'], 
                        address=data['address'], 
                        reference_address=data['reference_address'], 
                        phone_number=data['phone_number'])
        user.save()

        return {"message": "user created"}


@ns.route('/users/<int:id>/')
@ns.param('id', 'The user identifier')
class Users(Resource):
    '''Show a single user item , lets you delete and update them'''
    @ns.doc('get_user')
    def get(self, id):
        '''Fetch a user'''
        user = User.query.get(id)
        if user:
            u = {
                'id': user.id,
                'name': user.name,
                'lastname': user.lastname,
                'email': user.email,
                'address': user.address,
                'reference_address': user.reference_address,
                'phone_number': user.phone_number
            }
            return jsonify(u)
        else:
            return {"message": "user not found"}, 404

    @ns.doc('delete_user')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a user '''
        user = User.query.get(id)
        if user:
            user.delete()
            return {"message": "user deleted"}
        else:
            return {"message": "user not found"}, 404

    @ns.expect(model_user)
    def put(self, id):
        '''Update a user'''
        user = User.query.get(id)
        if request.method == 'PUT':
            if user:
                data = request.get_json()
                user.name = data['name']
                user.lastname = data['lastname']
                user.email = data['email']
                user.address = data['address']
                user.reference_address = data['reference_address']
                user.phone_number = data['phone_number']
                user.save()
                return {"message": "user updated"}
            else:
                return {"message": "user not found"}, 404

        elif request.method == 'GET':
            if user:
                return jsonify(user)




####### CRUD SIN DOCUMENTACION#########
# @app.route('/api/users/')
# def users():
#     query = User.query.all()
#     users = []
#     for user in query:
#         u = {
#             'id': user.id,
#             'name': user.name,
#             'lastname': user.lastname,
#             'email': user.email,
#             'address': user.address,
#             'reference_address': user.reference_address,
#             'phone_number': user.phone_number
#         }
#         users.append(u)

#     return  jsonify(users)

# @app.route('/api/users/<int:id>/')
# def user(id):
#     user = User.query.get(id)
#     if user:
#         u = {
#             'id': user.id,
#             'name': user.name,
#             'lastname': user.lastname,
#             'email': user.email,
#             'address': user.address,
#             'reference_address': user.reference_address,
#             'phone_number': user.phone_number
#         }
#         return jsonify(u)
#     else:
#         return {"message": "user not found"}, 404

# @app.route('/api/users/', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     user = [ user for user in User.query.all() if user.email == data['email']]
#     if user:
#         return {"message": "User already exists"}, 404

#     user = User( 
#                     name=data['name'], 
#                     lastname=data['lastname'], 
#                     email=data['email'], 
#                     address=data['address'], 
#                     reference_address=data['reference_address'], 
#                     phone_number=data['phone_number'])
#     user.save()

#     return {"message": "user created"}

# @app.route('/api/users/<int:id>', methods=['DELETE'])
# def delete_user(id):
#     user = User.query.get(id)
#     if user:
#         user.delete()
#         return {"message": "user deleted"}
#     else:
#         return {"message": "user not found"}, 404


# @app.route('/api/users/<int:id>', methods=['PUT', 'GET'])
# def update_user(id):
#     user = User.query.get(id)
#     if request.method == 'PUT':
#         if user:
#             data = request.get_json()
#             user.name = data['name']
#             user.lastname = data['lastname']
#             user.email = data['email']
#             user.address = data['address']
#             user.reference_address = data['reference_address']
#             user.phone_number = data['phone_number']
#             user.save()
#             return {"message": "user updated"}
#         else:
#             return {"message": "user not found"}, 404

#     elif request.method == 'GET':
#         if user:
#             return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)