### バイナリ形式データの入力
バイナリデータを入力ファイルとして用いる場合は、GrADSで使われる形式に従ってデータを用意しておく必要がある。GrADSのデータ形式は、ttp://cola.gmu.edu/grads/gadoc/aboutgriddeddata.html#structure を参照いただきたい。GrADS 形式データの [PARAM_MKINIT_REAL_(ATMOS|OCEAN|LAND)] の設定例は以下の通りである。


```
&PARAM_MKINIT_REAL_ATMOS
    NUMBER_OF_FILES = 2,
    FILETYPE_ORG = "GrADS",
    BASENAME_ORG = "namelist.grads_boundary.FNL.2005053112-2016051106",
    BASENAME_ADD_NUM = .true.,
    BASENAME_BOUNDARY = ’boundary_d01’,
    BOUNDARY_UPDATE_DT = 21600.0,
    ...
/

&PARAM_MKINIT_REAL_OCEAN
    FILETYPE_ORG = "GrADS",
    BASENAME_ORG = "namelist.grads_boundary.FNL.2005053112-2016051106",
    INTRP_OCEAN_SFC_TEMP = "mask",
    INTRP_OCEAN_TEMP = "mask",
    ...
/

&PARAM_MKINIT_REAL_LAND
    FILETYPE_ORG = "GrADS",
    BASENAME_ORG = "namelist.grads_boundary.FNL.2005053112-2016051106",
    INTRP_LAND_TEMP = "fill",
    INTRP_LAND_WATER = "fill",
    INTRP_LAND_SFC_TEMP = "fill",
/
```

(FILETYPE_ORG) は"GrADS"に設定する。SCALE-RM では、バイナリデータ (GrADS 形式) のファイル名やデータ構造について、**「ctl」ファイルの代わりに、(BASENAME_ORG) で指定するネームリストファイルで指定する**。ネームリストファイルは、予め用意しておく必要がある。バイナリデータのファイル名やデータ構造の情報を与えるネームリストファイル(namelist.grads_boundary*)の一例を下記に示す。


```
#
# Dimension
#
&GrADS_DIMS
    nx = 360, ; Default value of the number of grids in the x direction
    ny = 181, ; Default value of the number of grids in the y direction
    nz = 26, ; Default value of the number of layers in the z direction
/
#
# Variables
#
&GrADS_ITEM name=’lon’, dtype=’linear’, swpoint=0.0d0, dd=1.0d0 /
&GrADS_ITEM name=’lat’, dtype=’linear’, swpoint=90.0d0, dd=-1.0d0 /
&GrADS_ITEM name=’plev’, dtype=’levels’, lnum=26,
    lvars=100000,97500,.........,2000,1000, /
&GrADS_ITEM name=’HGT’, dtype=’map’, fname=’FNLatm’, startrec=1, totalrec=125 /
&GrADS_ITEM name=’U’, dtype=’map’, fname=’FNLatm’, startrec=27, totalrec=125 /
&GrADS_ITEM name=’V’, dtype=’map’, fname=’FNLatm’, startrec=53, totalrec=125 /
&GrADS_ITEM name=’T’, dtype=’map’, fname=’FNLatm’, startrec=79, totalrec=125 /
&GrADS_ITEM name=’RH’, dtype=’map’, fname=’FNLatm’, startrec=105,totalrec=125, nz=21 /
&GrADS_ITEM name=’MSLP’, dtype=’map’, fname=’FNLsfc’, startrec=1, totalrec=9 /
&GrADS_ITEM name=’PSFC’, dtype=’map’, fname=’FNLsfc’, startrec=2, totalrec=9 /
&GrADS_ITEM name=’SKINT’, dtype=’map’, fname=’FNLsfc’, startrec=3, totalrec=9 /
&GrADS_ITEM name=’topo’, dtype=’map’, fname=’FNLsfc’, startrec=4, totalrec=9 /
&GrADS_ITEM name=’lsmask’, dtype=’map’, fname=’FNLsfc’, startrec=5, totalrec=9 /
&GrADS_ITEM name=’U10’, dtype=’map’, fname=’FNLsfc’, startrec=6, totalrec=9 /
&GrADS_ITEM name=’V10’, dtype=’map’, fname=’FNLsfc’, startrec=7, totalrec=9 /
&GrADS_ITEM name=’T2’, dtype=’map’, fname=’FNLsfc’, startrec=8, totalrec=9 /
&GrADS_ITEM name=’RH2’, dtype=’map’, fname=’FNLsfc’, startrec=9, totalrec=9 /
&GrADS_ITEM name=’llev’, dtype=’levels’, nz=4, lvars=0.05,0.25,0.70,1.50, /
    missval=9.999e+20 /
&GrADS_ITEM name=’STEMP’, dtype=’map’, fname=’FNLland’, nz=4, startrec=1, totalrec=8,
    missval=9.999e+20 /
&GrADS_ITEM name=’SMOISVC’, dtype=’map’, fname=’FNLland’, nz=4, startrec=5, totalrec=8,
    missval=9.999e+20 /
```


格子数のデフォルト値は [GrADS_DIMS] の nx, ny, nz で指定する。また、入力データに関する設定は、各変数ごとに [GrADS_ITEM] を用意し指定する。[GrADS_ITEM] に関する説明は、表 4.1.3 に示す。

入力ファイルのベース名は、ネームリストファイル内の fname で設定する。fname="filename"と指定されている場合、入力ファイルが１つのとき ((NUMBER_OF_FILES)=1) は、入力ファイルは「filename.grd」という名前で準備する。

入力ファイルが複数あるとき、もしくは、(BASENAME_ADD_NUM)= .true. の場合には、「filename_XXXXX.grd」と番号付けされたファイルを準備する。


ある変数の格子数がデフォルト値と異なる場合には、[GrADS_ITEM] の nx, ny, nz でその変数の格子数を設定する。例えば、ある層から上では、比湿 (QV) や相対湿度 (RH) のデータが利用できない場合がある。その場合には、データが存在する層数を nz で指定する。

nz より上層での QV の与え方は、[PARAM_MKINIT_REAL_GrADS] の (upper_qv_type) で指定される。(upper_qv_type)=ZERO の場合、QV=0 と設定される。(upper_qv_type)=COPY の場合、湿度の入力データが存在する最上層の RH をデータの存在しない上層にコピーして、QV の値を決める。デフォルトの設定は’ZERO’ である。


```
&PARAM_MKINIT_REAL_GrADS
    upper_qv_type = "ZERO" ; nz より上層での QV の与え方
    (”ZERO”, ”COPY”)
/
```

| GrADS_ITEM の項目 | 説明 | 備考 |
|:---|:---|:---|
|name <br> dtype |変数名 <br> データタイプ |<br> "linear", "levels", "map"から選択 |
|(dtype) が"linear"の場合のネームリスト ("lon", "lat"専用) <br> fname <br> swpoint <br> dd | <br> ファイル名の頭 <br> スタートポイントの値 <br> 増分 |  |
|(dtype) が"levels"の場合のネームリスト ("plev", "llev"専用) <br> lnum <br> lvars | <br> レベルの数 (層数) <br> 各層の値 |  |
|(dtype) が"map"の場合のネームリスト <br> startrec <br> totalrec <br> missval | <br> 変数 (item) のレコード番号 <br> 一時刻あたりの全変数のレコード長 <br> 欠陥値の値 | <br> t=1 の時刻の値 <br>  <br> (オプション) |
|nx |x 方向の格子数 | (オプション) |
|ny |y 方向の格子数 | (オプション) |
|nz |z 方向の層数 | (オプション) |
|yrev |データが北から南の順に記録されている場合は.true. とする | (オプション) |



[GrADS_ITEM] の (name) の変数リスト。アスタリスクは「オプションであるが、可能な限
り推奨される」ことを意味する。二重のアスタリスクは、「利用できるが、推奨されない」ことを意
味する。


| flag | 変数名(name) | 説明 | 単位 |データタイプ(dtype) |
|:---|:---|:---|:---|:---|
| |lon |緯度 |[deg.] |linear, map |
| |lat |経度 |[deg.] |linear, map |
| |plev |気圧 |[Pa]  |levels, map |
|* |HGT |高度(ジオポテンシャル) |[m] |map |
|* |DENS |密度 |[kg/m3] |map |
| |U |東西風速 |[m/s] |map |
| |V |南北風速 |[m/s] |map |
|** |W |鉛直風速 |[m/s] |map |
| |T |気温 |[K] |map |
| |RH |相対湿度 (QV がある場合は省略可) |[%] |map |
| |QV |比湿 (RH がある場合は省略可) |[kg/kg] |map |
|** |QC |雲水の質量比 |[kg/kg] |map |
|** |QR |雨水の質量比 |[kg/kg] |map |
|** |QI |雲氷の質量比 |[kg/kg] |map |
|** |QS |雪の質量比 |[kg/kg] |map |
|** |QG |霰の質量比 |[kg/kg] |map |
|** |MSLP |海面更正気圧 |[Pa] |map |
|** |PSFC |地上気圧  |[Pa] |map |
|** |U10 |10m 東西風速 |[m/s] |map |
|** |V10 |10m 南北風速 |[m/s] |map |
|** |T2 |2m 気温 |[K] |map |
|** |RH2 |2m 相対湿度 (Q2 がある場合は省略可)  |[%] |map |
|** |Q2 |2m 比湿 (RH2 がある場合は省略可) |[kg/kg] |map |
|* |TOPO |GCM の地形 |[m]  |map |
|* |lsmask |GCM の海陸分布 |0:海 1:陸 |map |
| |SKINT |地表面温度 |[K] |map |
| |llev |土壌の深さ  |[m]  |levels |
| |STEMP |土壌温度  |[K] |map |
| |SMOISVC |土壌水分 (体積含水率)　(SMOISDS がある場合は省略可)  |[-] |map |
| |SMOISDS |土壌水分 (飽和度)　(SMOISVC がある場合は省略可)  |[-] |map |
| |SST |海面温度 (SKINT がある場合は省略可) |[K] |map |