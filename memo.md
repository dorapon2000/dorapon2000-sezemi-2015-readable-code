dorapon2000-sezemi-2015-readable-code/recipe.py

```python
recipe_file = sys.argv[1]
file_object = open(recipe_file,"r")
```

最初は
```
args = sys.args
```
のようにして引数に対して操作しようとしましたが、今回は引数が1つだけなので
sys.argv[1]をそのままrecipe_fileとして操作した方が読み手はわかりやすいと思いました。
単純にsys.argv[1]をopen()の引数にしませんでした

###この書き方の一言説明
理解しやすい仲間変数の宣言
