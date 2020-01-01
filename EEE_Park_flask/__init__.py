from flask import Flask, render_template
from flask_mongoengine import MongoEngine
import routes
app = Flask(__name__)
app.config['MONGODB_SETTINGS']={"db":"IEEE_Park"}
# app.run(host='0.0.0.0')
# app.config['FLASK_ENV']={"env":"development"}
db = MongoEngine(app)