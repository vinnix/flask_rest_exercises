from flask import Flask
from app import create_app, db
# the models need to be imported before calling db.create_all()
from app.models.People import People

application = create_app()

with application.app_context():
        db.create_all()

        if __name__ == "__main__":
                application.run(debug=True, host="0.0.0.0", port=5100)

