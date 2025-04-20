from src.frontend.app import app

def run_dash():
    app.run_server(debug=True, port=8050)  # Adjust port if needed

if __name__ == "__main__":
    run_dash()