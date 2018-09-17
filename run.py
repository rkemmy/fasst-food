from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')


    return app


if __name__ == "__main__":
    app.run(debug=True)
    