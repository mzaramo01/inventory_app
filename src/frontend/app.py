import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from dash import Dash
from dash import html

from src.frontend.layout import get_layout
from src.utils.logger import set_logger
from src.utils.config import DASH_PORT
from src.database.db import db, init_db
from src.backend.api import register_routes

logger = set_logger("frontend")

app = Dash(__name__)
# Navigate up two directories: src/frontend -> src -> root
app.server.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "inventory.db"))}'
app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print(f"Database URI: {app.server.config['SQLALCHEMY_DATABASE_URI']}")
db.init_app(app.server)

with app.server.app_context():
    init_db()

register_routes(app.server)
app.layout = get_layout()

if __name__ == "__main__":
    app.run_server(debug=True, port=DASH_PORT)