## walicaaa

### Git

##### コミット名
基本

```
DayXX {変更内容}
```

細かい修正

```
Fix {修正を加えた内容}
```

例:
```
Day1 必要なライブラリのインストール
Day2 main.py（API）の内容を修正
Day3 トップページのレイアウトを変更
Fix 不要なコメントアウトの削除
```
* できるだけ実装した機能、担当したタスクごとにコミットする
* 1日に複数コミットしてかまわない。例えばトップページのレイアウトとバックエンドのAPIを修正した場合、
Day2, Day3のように分けてコミットしていい
* 後から参加した開発者がコミット履歴を辿って理解できるように、DayXXという表記にしてみた
* 今回の開発は既存のリポジトリを参考に開発を進めていて、対象リポジトリのコミット履歴をたどりながら開発を進めている
https://github.com/uchijo/walica-clone-backend/commits/main/?before=bdb10179ad6cd8d6c837076d0abc9ea657945e50+35
* 基本はこのリポジトリに沿って開発を進めていくため、{変更内容}の部分は対象リポジトリのコミット番号でも良い。
* Go言語で書かれたものをPythonに置き換える形で進めている。
* なお、コミットメッセージミスったときは git commit --amend で修正できる
https://docs.github.com/ja/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/changing-a-commit-message

...

# ブランチ
```
main
|-develop
    |- takutosan
    |- hayato

```
### 初期セットアップ
1. 仮想環境（venv, anaconda）に入る
2. walicaaaディレクトリに移動
```console
cd ~/path/to/project/walicaaa

```
3. ↓仮想環境に入ってwalicaaaのディレクトリにいる状態
(project1) User@pc-name walicaaa
4. requirement.txtに記載のあるライブラリを全てインストール（初回）

```console
$ cd backend
$ pip install -r requirements.txt

```
これで開発に必要なセットアップは完了
なお、requirement.txtに変更を加えたら、再度このコマンドを実行してライブラリの再インストールが必要です

以下、walicaディレクトリにいる状態でコマンドを実行します
### サーバー起動（フロントエンド）
``` console
$ cd frontend
$ npm run dev

```
http://localhost:3000 でブラウザ上画面が表示される

### サーバー起動（バックエンド）
```console
$ cd backend
$ uvicorn app.main:app --reload

```
http://127.0.0.1:8000 でアクセス可能
何も表示されないように見えるが、frontendからのAPIリクエストを受け取れるようになっている
http://127.0.0.1:8000/docs にアクセスすると、現在のAPI仕様が全て確認できる
APIリクエスト/レスポンスのテストもここでできる