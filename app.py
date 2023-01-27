from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route('/')
def health():
    return jsonify({'health': 200})


class sum(Resource):

    def get(self):

        return jsonify({'hello': 'check'})

    def post(self):
        a = request.get_json()
        x = a['a']
        y = a['b']

        z = x+y
        return jsonify({'sum': z})


# class predict(Resource):

#     def get(self):
#         x = int(a)+int(b)
#         return jsonify({'sum': x})


@app.route('/sub', methods=['GET'])
def sub():
    a = request.args['a']
    b = request.args['b']
    x = int(a) + int(b)
    return jsonify({"sub": x})
    # http://0.0.0.0:5000/sub?a=8&b=9


api.add_resource(sum, '/sum')
#api.add_resource(predict, '/predict')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# gunicorn --bind=0.0.0.0 --port=5000 app:app
