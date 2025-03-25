from flask import Flask

def main():
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return "Hello from flat structure!"
    
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    main()