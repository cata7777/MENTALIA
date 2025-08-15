from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
limiter = Limiter(key_func=get_remote_address)

def create_app(config_name='production'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    
    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    limiter.init_app(app)
    
    # Registro de blueprints
    from app.core import bp as core_bp
    app.register_blueprint(core_bp, url_prefix='/api')
    
    from app.apps.hiperfoco import bp as hiperfoco_bp
    app.register_blueprint(hiperfoco_bp, url_prefix='/hiperfoco')
    
    from app.apps.universe import bp as universe_bp
    app.register_blueprint(universe_bp, url_prefix='/universe')
    
    from app.apps.chat import bp as chat_bp
    app.register_blueprint(chat_bp, url_prefix='/chat')
    
    return app
