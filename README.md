# 5m メッシュ集計  

* 5mメッシュデータの集計を行う

* 4次メッシュ単位集計

* 属性値つき集計


# Requirement
 
* QGIS 3.16
* OGeo4W shell
* Python 3.9.5
* PostgreSQL 13
* PostGIS 3.1.4


# modules

* cnv25mto5m

25mメッシュデータを5mメッシュデータに変換する

* createfolders

作業用フォルダの作成
```DOS
python createfolders.py  miyazakiken
```

* dataTypechecker

shapeファイルのデータチェック
```DOS
python dataTypechecker.py   -r <result file name> -o <output file name>    <input file name>
```

* doovl

5mメッシュの集計

```DOS
python doovl.py  -P <True or False>  <input file>
```

 **input file**            
shape file のフルパス名リストが格納されたテキストファイルの名前 


# Author
 
* YK

# License

* GPL2
