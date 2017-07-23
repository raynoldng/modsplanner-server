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
	compMods = compMods.split(',') if compMods != 'null' else []
	optMods = optMods.split(',') if optMods != 'null' else []
	options = json.loads(options)

	if semester == 1:
		semester = 'AY1718S1'
	elif semester == 2:
		semester = 'AY1617S2'		

	print [compMods, optMods, options]

	smtQuery, modMapping = queryParserBV.parseQuery(numToTake, compMods, optMods, options, semester)

	return jsonify([smtQuery, modMapping])


if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug = True)