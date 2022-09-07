from flask_sqlalchemy import SQLAlchemy

# note this should only be created once per project
# to define models in multiple files, put this in one file, and import db into each model, as we import it in flaskr.py
db = SQLAlchemy()

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.Text, nullable=False)
    definition = db.Column(db.Text, nullable=False)

    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def __repr__(self):
        return f'{self.term}: {self.definition}'

    def to_dict(self):
        new_dict = {
            "Term": None, 
            "Definition": None
        }
        new_dict["Term"] = self.term
        new_dict["Definition"] = self.definition
        print(f"in models.py: {new_dict}")
        return new_dict