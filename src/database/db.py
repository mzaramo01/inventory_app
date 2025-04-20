from flask_sqlalchemy import SQLAlchemy
from src.utils.logger import set_logger

db = SQLAlchemy()
logger = set_logger("database")

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=True)  # Added category column

    def __repr__(self):
        return f"<Item {self.id}: {self.name}, Quantity: {self.quantity}, Price: {self.price}>"

def init_db():
    try:
        logger.info("Attempting to create database tables")
        db.create_all()
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Failed to create database tables: {e}")
        raise