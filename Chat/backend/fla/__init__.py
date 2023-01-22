import os

from flask import Flask,request,jsonify


from flask_cors import CORS
import fla.chatAPI.chatAPI

#app = Flask(__name__)
#CORS(app)
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'fla.sqlite'),
    )
    CORS(app)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')

    def hello():
        return 'Hello, World!'

    @app.route('/chat/api', methods=["GET", "POST"])

    def chat():
        if request.method == "GET":
            print(request.args)
            contents = str(request.args.get('value', ''))
            print('入力文',contents)
            res = fla.chatAPI.chatAPI.mainProcess(contents)
            print('GET',res,contents)
            return res
        else:
            contents =  str(request.form["value"])
            print('入力文',contents)
            res = fla.chatAPI.chatAPI.mainProcess(contents)
            print('POST',res)
            #return jsonify({'data':res})
            return res
    return app