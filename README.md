# create-array-from-txt
txt情報からいい感じに配列を生成する。

| サービス | version |
| ------------- | ------------- |
| Python  | 3.8.6  |

# zipをダウンロードしてから動作確認する
1. https://github.com/kuroroblog/save-img-from-video へアクセスする。
2. 緑色の「Code」と書かれたボタンを選択
3. 「Download ZIP」を選択
4. ダウンロードされたzipファイルをデスクトップへ移動
5. zipファイルをダブルクリック
6. ターミナルを開く。
7. ターミナルを活用して、zipを展開して生成されたフォルダへ移動する。(`$ cd Desktop/save-img-from-video-master`)
8. `$ pip install -r requirements.txt`を実行する。
9. `$ python main.py`を実行する。
10. `test.mp4`からimgディレクトリ以下へ、静止画像ファイルが生成されているのか、確認する。

# 参考文献
- https://note.nkmk.me/python-opencv-video-to-still-image/
- https://note.nkmk.me/python-pip-install-requirements/
