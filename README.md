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

以下のようなサイトが表示されると成功．

![トップページ](https://github.com/mk102/Search_engine/blob/master/images/fig1.png)

検索ボタンをクリックすると全データの一覧が表示．

![一覧](https://github.com/mk102/Search_engine/blob/master/images/fig2.png)

検索ワードを入力し検索ボタンクリックで企業の絞り込みが可能．

![絞り込み](https://github.com/mk102/Search_engine/blob/master/images/fig3.png)

企業名をクリックすると詳細情報が表示

![詳細](https://github.com/mk102/Search_engine/blob/master/images/fig4.png)

## 注意事項

- githubにはスクレイピングした企業データはアップしていないので注意

- 現在(2020/6/12)時点では未完成．

## 今後の拡張予定

- CSVダウンロード機能

- データ可視化機能

- データを売上高や従業員数でも検索可

など


## 参考
以下のサイトを参考にさせていただきました
#### [FlaskとElasticsearchで社内の簡易書籍管理システムを作ってみた](https://qiita.com/MichiHosokawa/items/7f3393247ae028e316dd)
#### [【Python+Flask】WebAPIを使った簡易書籍管理アプリ【Elasticsearch、Vue.js】](https://qiita.com/aocattleya/items/c374e87b42a14a01e77c)
