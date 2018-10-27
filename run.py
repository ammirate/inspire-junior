from backend.db import db
from backend.factory import create_app


app = create_app('development')
db.create_all()

app.run(debug=True, host='0.0.0.0')