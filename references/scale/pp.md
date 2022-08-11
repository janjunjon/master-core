## 地形データの作成：pp

pp ディレクトリの中には、pp.d01.conf という名前の設定ファイルが準備されている。計算領域の位置や格子点数等の実験設定に応じて、pp.d01.conf を適宜編集する必要がある。本チュートリアルでは pp.d01.conf は編集済みであるので、そのまま利用すれば良い。表 3.2.1 に実験設定を示す。

pp.d01.conf のネームリストの中で、計算領域に関係する設定は **[PARAM_PRC_CARTESC]**、**[PARAM_GRID_CARTESC_INDEX]**、**[PARAM_GRID_CARTESC]** で行っている。

領域全体の総格子点数は、X 方向 、Y 方向それぞれ **(IMAXG)** = 90、**(JMAXG)** = 90 である。
X 方向 、Y 方向ともに領域は 2 分割されているので、各 MPI プロセスが担当する格子数は、X 方向 、Y 方向それぞれ 45 (= 90/2) である。

各方向の格子幅は **[PARAM_GRID_CARTESC]** の (**DX, DY**) において 20,000 m（20 km）と指定されている。したがって、計算領域の一辺の長さは 90 × 20 km であるので、計算領域は 1800 km × 1800 km の正方領域である。


```
# 各 MPI プロセスが担当する格子数
&PARAM_PRC_CARTESC
    PRC_NUM_X = 2,
    PRC_NUM_Y = 2,
    PRC_PERIODIC_X = .false.,
    PRC_PERIODIC_Y = .false.,
/

# 領域全体の総格子点数
&PARAM_INDEX_GRID_CARTESC_INDEX
    KMAX = 36,
    IMAXG = 90,
    JMAXG = 90,
/

# 各方向の格子幅
&PARAM_GRID_CARTESC
    DX = 20000.0,
    DY = 20000.0,
    FZ(:) = 80.841, 248.821, 429.882, 625.045, 835.409, 1062.158,
               1306.565, 1570.008, 1853.969, 2160.047, 2489.963, 2845.575,
               3228.883, 3642.044, 4087.384, 4567.409, 5084.820, 5642.530,
               6243.676, 6891.642, 7590.074, 8342.904, 9154.367, 10029.028,
               10971.815, 11988.030, 13083.390, 14264.060, 15536.685, 16908.430,
               18387.010, 19980.750, 21698.615, 23550.275, 25546.155, 28113.205,
    BUFFER_DZ = 5000.0,
    BUFFER_DX = 400000.0,
    BUFFER_DY = 400000.0,
/
```


scale-rm_pp 専用のネームリストとして [PARAM_CONVERT] がある。(CONVERT_TOPO) を.true.にすると標高データが処理され、(CONVERT_LANDUSE) を.true. にすると土地利用区分データが処理がされる。


```
&PARAM_CONVERT
    CONVERT_TOPO = .true.,
    CONVERT_LANDUSE = .true.,
/
```


また、[PARAM_CNVTOPO_GTOPO30] の中の (GTOPO30_IN_DIR) と [PARAM_CNVLANDUSE_GLCCv2]
の中の (GLCCv2_IN_DIR) はそれぞれ、標高データと土地利用区分データの場所を指定している。


```
&PARAM_CNVTOPO_GTOPO30
    GTOPO30_IN_DIR = "./topo/GTOPO30/Products",
    GTOPO30_IN_CATALOGUE = "GTOPO30_catalogue.txt",
/
&PARAM_CNVLANDUSE_GLCCv2
    GLCCv2_IN_DIR = "./landuse/GLCCv2/Products",
    GLCCv2_IN_CATALOGUE = "GLCCv2_catalogue.txt",
    limit_urban_fraction = 0.3D0,
/
```