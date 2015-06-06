### 実際のコード
https://github.com/dorapon2000/dorapon2000-sezemi-2015-readable-code/commit/654043db4e0f2ace224d8a795aabeba7bf16def1

### どうしてリーダブルだと思ったのかの説明
```python
recipe_file = sys.argv[1]
file_object = open(recipe_file,"r")
```

最初は
```python
args = sys.args
```
のようにして引数に対して操作しようとしましたが、今回は引数が1つだけなので
sys.argv[1]をそのままrecipe_fileとして操作した方が読み手はわかりやすいと思いました。
単純にsys.argv[1]をopen()の引数にしませんでした

###この書き方の一言説明
理解しやすい中間変数の宣言


### 実際のコード
https://github.com/dorapon2000/ch1ca0-sezemi-2015-readable-code/commit/c56b7cc2118e9c02e941f768447cc3b0e853caf0

### どうしてリーダブルだと思ったのかの説明
```python
recipe_list = recipe_json.keys()
for recipe in recipe_list:
    print(recipe)
```
recipe_listから取り出されるrecipeは後ろに情報をつけなくても単体のレシピ情報なんだと文脈からわかるから素直にrecipeとしたのがリーダブル

###この書き方の一言説明
文脈判断によるシンプル変数名



### 実際のコード
https://github.com/dorapon2000/ch1ca0-sezemi-2015-readable-code/commit/b4b02a91065102a62b9458dc511cb16dfd1e4694

### どうしてリーダブルだと思ったのかの説明
```python
recipe_file = open('recipe-data.json', 'r')
+recipe_json = json.load(recipe_file)
```
recipe_fileとrecipe_jsonでレシピを分けることで、どの型のレシピなのかわかりやすくてリーダブル

###この書き方の一言説明
コメント変数
