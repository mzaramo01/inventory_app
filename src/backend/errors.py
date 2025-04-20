from flask import jsonify


class APIError(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


def handle_api_error(error):
    response = jsonify({"error": error.message})
    response.status_code = error.status_code
    return response
