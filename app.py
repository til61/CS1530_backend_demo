import os

from flask import Flask, request, render_template, redirect, jsonify

from models import db, Card

app = Flask(__name__)


# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'flashcard.db')
))

db.init_app(app)

@app.cli.command('initdb')
def initdb_command():
	"""Creates the database tables."""
	db.create_all()
	print('Initialized the database.')


@app.route('/')
def hello_world():
    return render_template('demo.html')


@app.route('/cards', methods=['GET', 'POST'])
def cards_view():
	if request.method == 'GET':
		cards_list_raw = list(Card.query.order_by(Card.id.desc()))
		print(cards_list_raw)
		cards_list_json = []
		for card in cards_list_raw:
			new_card = card.to_dict()
			cards_list_json.append(new_card)
		print(cards_list_json)
		return jsonify(cards_list_json)
	if request.method == 'POST':
		term = request.json.get('term', None)
		definition = request.json.get('definition', None)
		print(f"term = {term}, def = {definition}")
		new_card = Card(term=term, definition=definition)
		db.session.add(new_card)
		db.session.commit()
		return {'status': 'ok'}


if __name__ == '__main__':
    app.run(debug=True)
