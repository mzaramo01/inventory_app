import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_PATH = os.path.join(
    os.environ["USERPROFILE"], "inventory_app_data", "inventory.db"
)
API_URL = "http://localhost:5000"
DASH_PORT = 8050
