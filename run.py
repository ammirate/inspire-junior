from backend import app
from backend import db


db.create_all()
app.run(debug=True, host='0.0.0.0')
