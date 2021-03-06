from flask import Flask
from flask import render_template, request
from form import *

from predict.views import *
from convert.views import *
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
jpype.addClassPath('cdk-2.3.jar')
startJVM(getDefaultJVMPath(), "-ea")



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# @app.route('/')
# def base():
#     return render_template('base.html')

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/base')
def base():
    return  render_template('base.html')



@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    form = PredictForm()

    if request.method == 'POST':

        result = request.form
        smiles = result.get('smiles')
        alt = int(result.get('al_fingerprint'))
        print(alt)
        PCE = RegressionPredit(smiles, alt)
        print(PCE)
        # message = []
        # message.append(PCE)
        # print(smiles)
        # print(type(result))
        # print(result)
        return render_template("predict.html", form=form, result= PCE)

    return render_template('predict.html', form=form)


# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form
#         return render_template("result.html",result = result)




@app.route('/convert', methods = ['POST', 'GET'])
def convert():
    form = ConvertForm()
    if request.method == 'POST':
        result = request.form
        #print(request.files)
        try:
            if result.get('smiles') != None:
                f_func = FingerprintType(int(result.get('fingerprint')))
                SingleSmilesConvert(f_func, result.get('smiles'), savename='csv/fingerprint.csv')

                return send_file('csv/fingerprint.csv', mimetype='text/csv',
                                 as_attachment=True, attachment_filename="fingerprint.csv")


            elif request.files != None:
                request.files.get('file').save('uploads/fingerprint.csv')
                file = 'uploads/fingerprint.csv'
                print(result.get('fingerprint'))
                f_func = FingerprintType(int(result.get('fingerprint')))
                FileSmilesConvert(f_func, namecol=1, PCEcol=2, smilescol=3, filename='uploads/fingerprint.csv', savename='csv/file_fingerprint.csv')
                return send_file('csv/file_fingerprint.csv', mimetype='text/csv',
                                 as_attachment=True, attachment_filename="file_fingerprint.csv")
        except:
            pass
    return render_template('convert.html',form=form)


@app.route('/about')
def about():
    return render_template('about.html')


#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
import os


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    #startJVM(getDefaultJVMPath(), "-ea")
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

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
    # @app.route('/')
    # def hello():
    #     return 'Hello, World!'

    # from . import db
    # db.init_app(app)
    #
    # from . import auth
    # app.register_blueprint(auth.bp)
    #
    # from . import blog
    # app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')


if __name__ == '__main__':
    app.run()
