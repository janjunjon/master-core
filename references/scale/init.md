## 初期値/境界値データの作成：init

```
$ cd ${Tutorial_DIR}/real/experiment/init
$ ls
    Makefile
    init.d01.conf
    init.launch.conf
    param.bucket.conf
    scale-rm_init
```


ディレクトリの中には、設定ファイル init.d01.conf が準備されている。他に init.launch.confというファイルも存在するが、ここでは使用しない。init.d01.conf ファイルには表 3.2.1 に示す。

チュートリアル用の設定が既になされているが、pp.d01.conf と同様に実験設定に応じて変更されたい。初期値/境界値データの生成には、前節で作成した地形データが使用される。地形データは、init.d01.conf において相対パスで設定する。


```
&PARAM_TOPOGRAPHY
    TOPOGRAPHY_IN_BASENAME = "../pp/topo_d01",
/
&PARAM_LANDUSE
    LANDUSE_IN_BASENAME = "../pp/landuse_d01",
/
```


その他に、init.d01.conf の設定の中で特に確認して欲しい項目は、[PARAM_MKINIT_REAL_ATMOS]、[PARAM_MKINIT_REAL_OCEAN]、[PARAM_MKINIT_REAL_LAND]の項目である。


```
&PARAM_MKINIT_REAL_ATMOS
    NUMBER_OF_FILES = 2,                                   ← 読み込むファイルの数
    FILETYPE_ORG = "GrADS",                                ← 表 4.1.2 から選択する
    BASENAME_ORG = "namelist.grads_boundary.FNL.grib1",
    BASENAME_BOUNDARY = "boundary_d01",                    ← 境界値データの出力名
    BOUNDARY_UPDATE_DT = 21600.0,                          ← 入力データの時間間隔
    PARENT_MP_TYPE = 3,
    USE_FILE_DENSITY = .false.,                            ← 親モデルの大気密度データを使うか
/

&PARAM_MKINIT_REAL_OCEAN
    ..... 略 .....
    INTRP_OCEAN_SFC_TEMP = "mask",                         ← SST の欠測値処理方法
    INTRP_OCEAN_TEMP = "mask",                             ← SST の欠測値処理方法
/

&PARAM_MKINIT_REAL_LAND
    ..... 略 .....
    USE_FILE_LANDWATER = .true.,                           ← 親モデルの土壌水分データを使うか
    INTRP_LAND_TEMP = "mask",                              ← 土壌温度の欠測値処理方法
    INTRP_LAND_WATER = "fill",                             ← 土壌水分の欠測値処理方法
    INTRP_LAND_SFC_TEMP = "fill",                          ← 地表面温度の欠測値処理方法
/
```


気象場データのファイル形式は (FILETYPE_ORG) で指定する。ここでは、GrADS 形式のデータを読み込むために “grads” を与えている。入力ファイルの詳細は第 4.1.2 節を参照されたい。第 3.2.2 節でバイナリ形式に変換した入力データ (FNL) へのリンクを、作業ディレクトリに張る。リンクを適切に張るために、${Tutorial_DIR}/real/data の中に「gradsinput-link_FNL.sh」と
いうスクリプトを用意している。


```
$ cp ../../data/gradsinput-link_FNL.sh ./
$ sh gradsinput-link_FNL.sh
```

```
ATM_00000.grd -> ../tools/FNL_output/200707/FNL_ATM_2007071418.grd
ATM_00001.grd -> ../tools/FNL_output/200707/FNL_ATM_2007071500.grd
LND_00000.grd -> ../tools/FNL_output/200707/FNL_LND_2007071418.grd
LND_00001.grd -> ../tools/FNL_output/200707/FNL_LND_2007071500.grd
SFC_00000.grd -> ../tools/FNL_output/200707/FNL_SFC_2007071418.grd
SFC_00001.grd -> ../tools/FNL_output/200707/FNL_SFC_2007071500.grd
```


次に、GrADS 形式のバイナリデータを SCALE で読み込むためのネームリストファイルを、ディレクトリ init へリンクする。


```
$ ln -s ../../data/namelist.grads_boundary.FNL.2005053112-2016051106 ./
```