# Search_engine
スクレイピングした企業の検索サイトFlask+Vue.js

スクレイピングした企業情報を検索するWebアプリです．

## Requirement

- Elasticsearch
  - http://localhost:9200でアクセスできることを要確認．
- pip install elasticsearch
- pip install Flask

## Usage

### Flask起動
以下をapp.pyの置かれているディレクトリ直下で実行

- python app.py

### アプリ利用
https:localhost:8080にアクセス


## 注意事項
githubにはスクレイピングした企業データはアップしていないので注意

## 参考
以下のサイトを参考にさせていただきました
#### [FlaskとElasticsearchで社内の簡易書籍管理システムを作ってみた](https://qiita.com/MichiHosokawa/items/7f3393247ae028e316dd)
#### [【Python+Flask】WebAPIを使った簡易書籍管理アプリ【Elasticsearch、Vue.js】](https://qiita.com/aocattleya/items/c374e87b42a14a01e77c)
