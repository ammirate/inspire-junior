from backend.factory import create_app


app = create_app('development')
app.run(debug=True, host='0.0.0.0')
