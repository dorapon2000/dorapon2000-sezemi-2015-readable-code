#使用言語
python

#仕様1
shell上で次のコマンドを実行

```
$ python recipe.py
```

#仕様2
レシピデータを適当な.txtファイルに書き込む

#仕様3
shell上で次のコマンドを実行する

```
$ python recipe.py recipe_data.txt
```

#仕様4
レシピデータは適当な.txtファイルに書き込む
1行に1つのレシピ情報を入れる
最後は改行文字だけ入れる

```
オムライス
親子丼
杏仁豆腐
[Enter]
```

実行は仕様3の時と同じである

#TODO
いまさらながらrecipe_dataではstring型ではなくてobjectにも見えてしまいそう
recipe_infoとかの方がよかったかも
