# 梯次R_變數：挖礦挑戰賽

## 課程定位

- 時間：09:00－12:00，共三小時
- 平台：Minecraft Education＋Microsoft MakeCode
- 核心概念：變數、事件觸發、分數累積、迴圈與倒數計時
- 使用地圖：[神木村 v6](../shared/maps/神木村v6.mcworld)，由老師課前在指定區域生成共用大型礦坑
- 遊戲目標：在 60 秒內挖掘不同礦物，依礦物價值累積分數

## 教師備課快速總覽

| 教學階段 | 老師帶學生完成的程式 | 程式完成標準 | 完成後的遊戲或比賽 |
|---|---|---|---|
| 低階：礦物計分 | 用分數變數與四個挖掘事件記錄礦物價值 | 煤、鐵、金、鑽石分別增加 1、2、3、5 分，輸入 `2` 可查分 | 由老師統一計時的挖礦計分賽 |
| 中階：倒數計時 | 用時間變數、重複迴圈及暫停製作 60 秒倒數 | 輸入 `1` 後顯示開始標題，快捷欄上方每秒更新剩餘時間 | 個人限時挖礦體驗 |
| 高階：倒數＋計分 | 將時間與分數顯示在快捷欄上方，時間到後停止計分 | 輸入 `1` 開始 60 秒比賽，輸入 `2` 可重看最後分數 | 60 秒正式挖礦挑戰賽 |

## 遊戲準備

- 使用神木村 v6，由老師或世界主持人選定不影響既有建築的礦坑區域。
- 老師課前站在場地中心執行本教案的教師專用礦坑生成程式，輸入 `9` 生成 41×41×2 格礦坑。
- 礦坑生成程式只由老師操作，避免學生重複覆蓋共用世界。
- 同一場比賽所有學生統一使用同一種類的鎬子；鎬子種類由授課老師依課堂情況分配，並確認能挖掘四種礦物。
- 在礦坑外圍標示起始位置，避免所有學生集中在同一點。
- 學生程式不調整難度、遊戲模式、天氣、時間或遊戲規則。
- 個人分數、倒數與結果只顯示給本機玩家，避免洗滿全班聊天室。
- 已用兩台裝置確認一位學生挖礦不會增加另一位學生的分數。

## 遊戲規則

1. 學生到老師指定的起始位置準備。
2. 低、高階輸入 `1` 將分數歸零；中階輸入 `1` 啟動倒數。
3. 正式賽每回合 60 秒。
4. 煤礦 1 分、鐵礦 2 分、金礦 3 分、鑽石礦 5 分。
5. 不搶奪其他學生已挖出的掉落物。
6. 時間到立即停止挖礦；低、高階輸入 `2` 查看最後總分，中階由老師協助計分。
7. 總分最高者獲勝；同分時比較鑽石數量。
8. 下一回合由老師重新生成礦坑，學生再將分數歸零。

## 分級程式

三份學生程式彼此獨立，每次只使用一份。學生從空白專案逐塊完成，不以貼上 Python 作為主要教學方式。

### 教師專用礦坑生成程式

只由老師或世界主持人執行。老師站在選定區域中心輸入 `9`，生成共用礦坑。

```python
index = 0


def on_chat_9():
    global index
    blocks.fill(
        STONE,
        pos(-20, -2, -20),
        pos(20, -1, 20),
        FillOperation.REPLACE
    )

    index = 0
    while index < 1500:
        blocks.place(COAL_ORE, randpos(pos(-20, -2, -20), pos(20, -1, 20)))
        index += 1

    index = 0
    while index < 1000:
        blocks.place(IRON_ORE, randpos(pos(-20, -2, -20), pos(20, -1, 20)))
        index += 1

    index = 0
    while index < 500:
        blocks.place(GOLD_ORE, randpos(pos(-20, -2, -20), pos(20, -1, 20)))
        index += 1

    index = 0
    while index < 200:
        blocks.place(DIAMOND_ORE, randpos(pos(-20, -2, -20), pos(20, -1, 20)))
        index += 1

    player.tell(mobs.target(LOCAL_PLAYER), "礦坑完成")
player.on_chat("9", on_chat_9)
```

### 低階完整程式：礦物計分

所有學生至少完成礦物自動計分，直接用於挖礦比賽。

```python
score = 0


def on_block_broken_iron_ore():
    global score
    score += 2
    player.tell(mobs.target(LOCAL_PLAYER), score)
blocks.on_block_broken(IRON_ORE, on_block_broken_iron_ore)


def on_chat_2():
    player.tell(mobs.target(LOCAL_PLAYER), score)
player.on_chat("2", on_chat_2)


def on_block_broken_coal_ore():
    global score
    score += 1
    player.tell(mobs.target(LOCAL_PLAYER), score)
blocks.on_block_broken(COAL_ORE, on_block_broken_coal_ore)


def on_block_broken_gold_ore():
    global score
    score += 3
    player.tell(mobs.target(LOCAL_PLAYER), score)
blocks.on_block_broken(GOLD_ORE, on_block_broken_gold_ore)


def on_chat_1():
    global score
    score = 0
    gameplay.title(mobs.target(LOCAL_PLAYER), "挖礦挑戰賽", "開始!")
player.on_chat("1", on_chat_1)


def on_block_broken_diamond_ore():
    global score
    score += 5
    player.tell(mobs.target(LOCAL_PLAYER), score)
blocks.on_block_broken(DIAMOND_ORE, on_block_broken_diamond_ore)
```

### 中階完整程式：倒數計時器

使用時間變數、迴圈與暫停完成 60 秒倒數。

```python
time = 0


def on_chat_1():
    global time
    time = 60
    gameplay.title(mobs.target(LOCAL_PLAYER), "挖礦挑戰賽", "開始!")

    while time > 0:
        player.execute("title @s actionbar 時間:" + str(time))
        loops.pause(1000)
        time += 0 - 1

    player.execute("title @s actionbar 時間到")
player.on_chat("1", on_chat_1)
```

### 高階完整程式：倒數＋計分

整合倒數與計分，時間到後停止加分並保留最後結果。

```python
time = 0
score = 0


def on_block_broken_iron_ore():
    global score
    if time > 0:
        score += 2
blocks.on_block_broken(IRON_ORE, on_block_broken_iron_ore)


def on_chat_2():
    player.execute("title @s actionbar 最後總分:" + str(score))
player.on_chat("2", on_chat_2)


def on_block_broken_coal_ore():
    global score
    if time > 0:
        score += 1
blocks.on_block_broken(COAL_ORE, on_block_broken_coal_ore)


def on_block_broken_gold_ore():
    global score
    if time > 0:
        score += 3
blocks.on_block_broken(GOLD_ORE, on_block_broken_gold_ore)


def on_chat_1():
    global time, score
    time = 60
    score = 0
    gameplay.title(mobs.target(LOCAL_PLAYER), "挖礦挑戰賽", "開始!")

    while time > 0:
        player.execute("title @s actionbar 時間:" + str(time) + " 分數:" + str(score))
        loops.pause(1000)
        time += 0 - 1

    player.execute("title @s actionbar 時間到 分數:" + str(score))
player.on_chat("1", on_chat_1)


def on_block_broken_diamond_ore():
    global score
    if time > 0:
        score += 5
blocks.on_block_broken(DIAMOND_ORE, on_block_broken_diamond_ore)
```

## 半日營標準流程

| 時間 | 流程大綱 |
|---|---|
| 09:00－09:10 | 開場、自我介紹與破冰 |
| 09:10－09:35 | 遊戲操作與自由探索 |
| 09:35－10:15 | 基礎程式教學 |
| 10:15－10:35 | 基礎功能測試與遊戲活動 |
| 10:35－10:45 | 休息時間 |
| 10:45－11:25 | 進階程式教學 |
| 11:25－11:50 | 進階功能測試與成果挑戰 |
| 11:50－12:00 | 課程複習與收尾 |

## 程式示範影片

- [挖礦挑戰賽程式示範 1](https://youtu.be/TB4g48VBF6M?si=GCWYsIjLe4jb_Xjn)
- [挖礦挑戰賽程式示範 2](https://youtu.be/0JJ9qUJ2ZBM?si=5cEJBSfjcoxv27sN)

## 家長回饋

親愛的家長您好：

今天的主題是「變數：挖礦挑戰賽」。

今天孩子們進入大型礦坑，挑戰在有限時間內挖掘煤礦、鐵礦、金礦與鑽石礦。

孩子們把「變數」想像成會記住數字的小盒子，利用它保存剩餘時間與目前分數。

不同進度的孩子分別完成自動計分、倒數計時，以及結合時間與分數的完整挖礦挑戰程式。

學習重點

重點一：孩子們使用「分數變數」記錄挖礦成果，讓煤礦、鐵礦、金礦與鑽石礦分別獲得 1、2、3、5 分。

重點二：孩子們學會將「時間變數」設定為 60，搭配「重複迴圈」與暫停一秒，製作會自動減少的倒數計時器。

重點三：進階孩子將倒數與計分顯示在自己的快捷欄上方，並讓程式在時間結束後停止加分，完成一套完整的挖礦競賽系統。

今天每位孩子都表現得非常棒，也順利完成了挖礦挑戰賽的程式建構任務！

## 教師課後確認

- [x] 低、中、高核心程式已在 Minecraft Education 內測試。
- [x] 核心程式可正常執行並切換成積木。
- [x] 聊天指令 `1`、`2` 可正常執行。
- [x] 快捷欄上方可顯示倒數、目前分數與最後總分。
- [x] 高階時間到後不再增加分數。
- [x] 已使用兩台裝置確認計分互不影響。
- [ ] 教師已在正式上課地圖測試礦坑生成。
- [ ] 已補齊低、中、高程式截圖及礦坑畫面。
- [x] 已補上兩支遊戲內示範影片。
