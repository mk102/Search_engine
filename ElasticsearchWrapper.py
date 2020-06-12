from elasticsearch import Elasticsearch
import copy
import sys
import json


# ElasticSearchへデータ登録
def data_submission():
	es = Elasticsearch(['http://localhost:9200/'])
	create_pages_index(es)

	for line in sys.stdin:
		page = json.loads(line)
		es.index(index = "companies", doc_type = "_doc", body = page)


def create_pages_index(es: Elasticsearch):
	"""
	Elasticsearchにpagesインデックスを作成する
	"""
	# キーワード引数bodyでJSONに相当するdictを指定
	# ignore=400はインデックスが存在する場合でもエラーにしないという意味
	es.indices.create(index='companies', ignore=400, body={
		# settingsという項目で，kuromoji_analyzerというアナライザーを定義
		# アナライザーは転地インデックスの作成方法
		"settings": {
			"analyzer": {
				"kuromoji_analyzer": {
					# 日本語形態素解析を使って文字列を分割するkuromoji_tokenizerを使用
					"tokenizer": "kuromoji_tokenizer"
				}
			}
		},
	# mappingsという項目で，ドキュメントが持つフィールドを定義
	"mappings": {
		"_doc": {
			# name, uriage, eigyo_rieki, keizyo_rieki, zyun_rieki, gyousyuのフィールドを定義
			"properties": {
				"name": {"type": "text", "analyzer": "kuromoji_analyzer"},
				"uriage": {"type": "text"},
				"eigyo_rieki": {"type": "text"},
				"keizyo_rieki": {"type": "text"},
				"zyun_rieki": {"type": "text"},
				"gyousyu": {"type": "text", "analyzer": "kuromoji_analyzer"}
			}
		}
	}
	})


if __name__ == '__main__':
	data_submission()
