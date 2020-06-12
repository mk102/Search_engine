from flask import Flask, render_template, url_for, jsonify, request
import os
import random
from elasticsearch import Elasticsearch
import json
import copy

class CustomFlask(Flask):
    '''
    テンプレートのデリミタがVue.jsと競合するので、Flask側でデリミタを別の文字に変更する
	参照：https://muunyblue.github.io/0b7acbba52fb92b2e9c818f7f56bac99.html
    '''
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
		block_start_string='(%',
		block_end_string='%)',
		variable_start_string='((',
		variable_end_string='))',
		comment_start_string='(#',
		comment_end_string='#)',
    ))


app = CustomFlask(__name__)


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route("/")
@app.route("/<name>")
def index(name=None):
	return render_template("index.html")


@app.route("/csvdl")
def csvdl():
	return "csvtest"


@app.route("/search")
def search():
	'''
	検索
	'''
	# パラメータからワードを取得
	g_word = request.args.get('s_g_word', default = None)
	n_word = request.args.get('s_n_word', default = None)
	es = Elasticsearch(['http://localhost:9200/'])

	results = []
	params = {
		'size': 10000
	}
	'''
	body = {
		"query": {"match": {"gyousyu":g_word}}
	}
	'''
	match_list = [{
		"match":{
			n:i
		}
	} for i, n in zip([g_word, n_word], ["gyousyu", "name"]) if i != '']

	print(g_word == '')
	print(n_word == '')

	body = {
		"query": {
			"bool": {
				"must": match_list
			}
		}
	}
	#print(body)
	old_id = []
	for i in es.search(index = "companies", body = body, params=params)["hits"]["hits"]:
		if i["_id"] in old_id:
			continue
		#print(old_id)

		old_id.append(i["_id"])
		body = copy.deepcopy(i["_source"])
		score = i['_score']
		result = {'body': body, 'score': score}
		results.append(result)
	#print(results)
	return jsonify(results)


if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', port=8080)