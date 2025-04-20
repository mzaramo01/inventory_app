from flask import jsonify, request
from src.database.db import db, Item

def register_routes(app):
    @app.route('/items', methods=['GET'])
    def get_items():
        try:
            items = Item.query.all()
            return jsonify([{'id': i.id, 'name': i.name, 'quantity': i.quantity, 'price': i.price} for i in items])
        except Exception as e:
            app.logger.error(f"Error in get_items: {str(e)}")
            return jsonify({'error': str(e)}), 500

    @app.route('/items', methods=['POST'])
    def create_item():
        try:
            data = request.get_json()
            new_item = Item(name=data['name'], quantity=data['quantity'], price=data['price'])
            db.session.add(new_item)
            db.session.commit()
            return jsonify({'id': new_item.id, 'name': new_item.name, 'quantity': new_item.quantity, 'price': new_item.price}), 201
        except Exception as e:
            app.logger.error(f"Error in create_item: {str(e)}")
            return jsonify({'error': str(e)}), 500