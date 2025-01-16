from app import create_app

app = create_app()

if __name__ == '__main__':
    # Run Flask app on all network interfaces (0.0.0.0) and port 5000
    app.run(debug=True, host='0.0.0.0', port=8000)
