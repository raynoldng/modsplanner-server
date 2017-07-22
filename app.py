from flask import Flask, jsonify
import json

import config
import queryParserBV

app = Flask(__name__)

# router.get('/:semester/:numToTake/:compMods/:optMods/:options', (req, res) => {


@app.route('/')
def index():
	return "Home page"

@app.route('/api/<int:semester>/<int:numToTake>/<string:compMods>/<string:optMods>/<string:options>')

def apiQuery(semester, numToTake, compMods, optMods, options):
	compMods = compMods.split(',')
	optMods = optMods.split(',')
	options = json.loads(options)

	if semester == 1:
		semester = 'AY1718S1'
	elif semester == 2:
		semester = 'AY1617S2'		

	print [compMods, optMods, options]

	smtQuery, modMapping = queryParserBV.parseQuery(numToTake, compMods, optMods, options, semester)

	return jsonify([smtQuery, modMapping])


if __name__ == '__main__':
	app.run(debug = True)