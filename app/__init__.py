from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

lm = LoginManager()
lm.login_view = 'login'
lm.session_protection = "strong"
lm.init_app(app)

from app.models.seeds import Seed
sd = Seed(app, db)

from app.utils.filters import Filters
ft = Filters()

from app.models import tables, forms
from app.controllers import default
