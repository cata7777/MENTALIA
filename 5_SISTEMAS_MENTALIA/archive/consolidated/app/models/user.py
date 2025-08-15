from app import db
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    profile_type = db.Column(db.String(50), default='general')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relaciones
    nd_profile = db.relationship('NeurodivergentProfile', backref='user', uselist=False)
    conversations = db.relationship('Conversation', backref='user', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_token(self):
        return create_access_token(identity=self.id)
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'profile_type': self.profile_type,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active
        }
