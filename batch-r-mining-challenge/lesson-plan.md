# 梯次 R｜變數：挖礦挑戰賽

- 課程時間：09:00－12:00
- 遊戲版本：Minecraft Education
- 程式平台：Microsoft MakeCode
- 核心概念：變數、事件觸發、分數累積、迴圈、倒數計時

## 課程目標

學生在 60 秒內挖掘煤、鐵、金與鑽石礦，使用變數記錄時間與分數。低階完成自動計分，中階完成倒數，高階整合倒數與計分，並在時間結束後停止加分。

## 課前準備

- 地圖：[神木村 v6](../shared/maps/神木村v6.mcworld)
- 老師在不影響既有建築的平坦區域選定礦坑中心，站在中心輸入 `9`，生成 41×41×2 格礦坑。
- 礦坑程式使用玩家相對座標：中心點為 `(0, 0, 0)`，範圍為 X `-20～20`、Y `-2～-1`、Z `-20～20`。
- 礦坑外圍標示多個起點，讓學生平均分散。
- 同一場比賽所有學生使用相同種類的鎬子；鎬子須能挖掘四種指定礦物。
- 為每位學生建立獨立 MakeCode 專案；不要把低、中、高疊在同一專案。
- 學生程式不調整世界難度、遊戲模式、天氣、時間或遊戲規則。
- 開課前以兩台裝置確認一位學生挖礦不會增加另一位學生的分數。
- 保留一份未生成礦坑的乾淨 `.mcworld` 世界備份。

## 半日營流程

| 時間 | 教學內容 |
|---|---|
| 09:00－09:10 | 開場、礦物價值與比賽規則 |
| 09:10－09:35 | Minecraft 挖礦操作與場地熟悉 |
| 09:35－10:15 | 低階：變數與礦物事件計分 |
| 10:15－10:35 | 計分測試與老師統一計時練習賽 |
| 10:35－10:45 | 休息 |
| 10:45－11:25 | 中階／高階：倒數與完整競賽程式 |
| 11:25－11:50 | 60 秒正式挖礦挑戰賽 |
| 11:50－12:00 | 公布結果、程式概念回顧 |

## 遊戲任務：60 秒挖礦挑戰賽

### 遊戲規則

1. 學生到老師指定的不同起點準備。
2. 低、高階輸入 `1` 將分數歸零；中階輸入 `1` 啟動倒數。
3. 老師宣布開始後進行 60 秒正式賽。
4. 煤礦 1 分、鐵礦 2 分、金礦 3 分、鑽石礦 5 分。
5. 不搶奪其他學生已挖出的掉落物，也不可離開礦坑範圍。
6. 時間到立即停止挖礦；低、高階輸入 `2` 查看最後分數，中階由老師協助計分。
7. 總分最高者獲勝；同分時依鑽石、金礦、鐵礦數量排序。
8. 下一回合由老師輸入 `9` 重新生成礦坑，學生再把分數歸零。

### 程式與遊戲的連接

| 程度 | 程式負責 | 遊戲中的使用方式 |
|---|---|---|
| 低階 | 自動辨認四種礦物並累積分數 | 老師統一計時，學生用自己的程式計分 |
| 中階 | 顯示 60 秒倒數 | 學生進行個人限時體驗，由老師協助計分 |
| 高階 | 同時倒數、計分並在時間到後鎖定分數 | 學生獨立完成正式挑戰 |

## 教師程式｜生成與重置礦坑

老師站在選定區域中心輸入 `9`。程式先鋪滿石頭，再隨機放入煤、鐵、金、鑽石礦；隨機位置可能重疊，因此最終數量不一定等於放置次數。

```python
index = 0

def on_chat_9():
    global index
    blocks.fill(STONE, pos(-20, -2, -20), pos(20, -1, 20), FillOperation.REPLACE)
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

- [下載教師礦坑 Python](code/teacher-mine.py)

## 低階｜礦物自動計分

### 任務與完成標準

用 `score` 變數記錄總分，替四種礦物建立挖掘事件。輸入 `1` 歸零並開始，輸入 `2` 查看總分。

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

- [下載低階 Python](code/low.py)
- MakeCode 分享連結：**待補**
- 積木程式圖片：**待補**
- 功能測試：分別挖一個煤、鐵、金、鑽石礦，總分應依序增加 1、2、3、5；輸入 `2` 應顯示相同總分。

## 中階｜60 秒倒數

### 任務與完成標準

用 `time` 變數從 60 開始，每秒減 1，並在快捷欄上方顯示剩餘時間。

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

- [下載中階 Python](code/medium.py)
- MakeCode 分享連結：**待補**
- 積木程式圖片：**待補**
- 功能測試：先把 60 改成 5，確認每秒更新並在 5 秒後顯示時間到，再改回正式數值。

## 高階｜倒數與計分

### 任務與完成標準

整合 `time` 與 `score`，倒數期間挖礦才加分；時間到後鎖定結果。輸入 `2` 可重看最後總分。

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

- [下載高階 Python](code/high.py)
- MakeCode 分享連結：**待補**
- 積木程式圖片：**待補**
- 功能測試：先改成 5 秒，倒數中挖礦應加分，時間到後再挖礦應維持原分數。

> 低、中、高核心程式已有 Minecraft Education 測試紀錄，能執行並轉換成積木；正式授課前仍需依當期版本再次測試。教師礦坑程式尚未留下正式地圖的實測紀錄。

## 場地保存、重置與跨地圖使用

- 礦坑位置由老師站立點決定，不綁定絕對座標；選好中心後，建議用告示牌記錄該世界的 X、Y、Z。
- 本梯次已用獨立教師 Python 解決場地生成與座標偏移，換世界時只需更換老師站立的中心點。
- 41×41×2 礦坑若用單一結構方塊容易受版本或範圍限制，且每回合仍要補入隨機礦物，因此以教師程式重建較方便。
- 每回合重置：所有學生離開礦坑後，老師回到同一中心點輸入 `9`。
- 世界保存：課前保留乾淨 `.mcworld`；需要保留學生結果時另存新世界，不覆蓋公版。

## 上課知識點

- **變數：** `score` 記住分數，`time` 記住剩餘秒數。
- **事件：** 玩家挖到指定礦物時，對應事件才會執行。
- **累加：** 不同礦物使用不同分值加入同一個總分。
- **條件判斷：** 高階程式只有在 `time > 0` 時才加分。
- **迴圈與暫停：** 每暫停 1000 毫秒再扣 1，形成一秒一次的倒數。
- **相對座標：** 教師站立點改變，礦坑生成位置也跟著改變。
- **公平性：** 統一工具、分散起點與個人計分可減少非程式因素造成的差異。

## 程式示範影片

- [挖礦挑戰賽程式示範 1](https://youtu.be/TB4g48VBF6M?si=GCWYsIjLe4jb_Xjn)
- [挖礦挑戰賽程式示範 2](https://youtu.be/0JJ9qUJ2ZBM?si=5cEJBSfjcoxv27sN)

## 家長回饋公版

親愛的家長您好：

今天孩子完成了 Minecraft Education「變數：挖礦挑戰賽」課程，在 60 秒內挖掘煤、鐵、金與鑽石礦，並用程式記錄時間與分數。孩子把變數當成會記住數字的小盒子，再透過礦物事件、累加與條件判斷，讓不同礦物得到不同分數。

孩子今天完成的程度為【低階／中階／高階】，課堂表現【請填寫具體表現，例如：能逐一測試四種礦物並修正計分】。正式挑戰得到【請填寫分數或成果】，並能說明【請填寫孩子掌握的概念】。

回家後可以請孩子分享：「程式如何知道挖到哪一種礦物？時間到後又為什麼不再加分？」幫助孩子整理事件、變數與條件判斷的關係。
