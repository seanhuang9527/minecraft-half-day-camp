# 梯次 D｜巢狀迴圈：礦坑達人

- 課程時間：09:00－12:00
- 遊戲版本：Minecraft Education
- 程式平台：Microsoft MakeCode（Python／積木）
- 核心概念：Agent 控制、方向、迴圈、巢狀迴圈、自動挖掘、礦坑安全

![Minecraft 礦物高度參考圖](images/course-reference.png)

## 課程目標

學生將使用 Agent 建造不同形狀的礦道，理解「重複動作」與「巢狀迴圈」如何把簡單指令組合成樓梯、十字與魚骨結構。完成程式後，學生會進入自己開挖的礦道採集資源，並練習照明、辨認方向及安全返回地面。

## 課前準備

- 正式上課地圖：[神木村 v6](../shared/maps/神木村v6.mcworld)
- 備用舊版地圖：[神木村 8 人版](maps/神木村8人版.mcworld)
- 確認每台電腦可以開啟 Minecraft Education、加入老師世界並連接 MakeCode。
- 學生執行程式時，需有可使用指令與 Agent 的權限。
- 每位學生安排不同礦道起點，起點間至少保留 12 格，並讓 Agent 朝相同方向。
- 每位學生準備十字鎬、食物及火把；低階程式須把火把放進 Agent 第 1 格。
- 老師先備份世界。礦道需要重置時，直接重新開啟備份世界最可靠。

> 三份 Python 是依既有積木截圖轉寫的公開版，尚需老師在當期 Minecraft Education 版本做一次課前實機測試。低階版另外加入 `agent.set_slot(1)`，避免 Agent 放錯材料。

## 半日營流程

| 時間 | 教學內容 |
|---|---|
| 09:00－09:10 | 開場、分組與礦坑安全說明 |
| 09:10－09:35 | Minecraft 操作、Agent 方向與礦物高度介紹 |
| 09:35－10:15 | 低階樓梯挖礦程式與功能測試 |
| 10:15－10:35 | 進入樓梯礦道、採集與除錯 |
| 10:35－10:45 | 休息 |
| 10:45－11:25 | 依進度完成十字挖礦或魚骨挖礦 |
| 11:25－11:50 | 同層級採礦挑戰與成果展示 |
| 11:50－12:00 | 程式概念複習與收尾 |

## 遊戲規則

1. 每位學生只能進入自己的礦道，不得挖進別人的路線。
2. 程式開始前先確認 Agent 面向、物品欄及礦道前方沒有其他玩家。
3. 練習回合不計分；正式回合限時 8 分鐘。
4. 煤炭 1 分、銅或鐵 2 分、其他礦物 3 分。
5. 只計算從自己程式礦道取得並在時間內帶回起點的資源。
6. 不同程式會產生不同挖掘量，因此只和使用相同層級程式的學生比較；也可改為全班累積總分。
7. 同分時以安全回到起點且能說明程式邏輯者優先；仍同分則並列。

## 分級程式

### 低階｜樓梯挖礦與照明

**任務：** 使用兩層迴圈，讓 Agent 分四段向前、向下挖出樓梯，並在每段右側放置火把。

**操作：**

1. 把火把放入 Agent 第 1 格。
2. 將 Agent 放在起點並朝向山體或老師指定方向。
3. 在聊天欄輸入 `3`。
4. 確認通道可以步行、火把在右側，且能沿原路返回。

**知識點：** 指令順序、方向、迴圈、巢狀迴圈、收集掉落物。

**Python 程式碼：** [下載／查看 low.py](code/low.py)

```python
def on_on_chat():
    agent.set_slot(1)
    for index in range(4):
        for index2 in range(4):
            agent.destroy(FORWARD)
            agent.move(FORWARD, 1)
            agent.destroy(UP)
            agent.destroy(DOWN)
            agent.move(DOWN, 1)
            agent.collect_all()
        agent.place(RIGHT)
player.on_chat("3", on_on_chat)
```

![低階樓梯挖礦積木程式](images/staircase-mining.png)

**MakeCode 分享連結：** 待補

### 中階｜十字挖礦

**任務：** 先向下挖 10 格，再從中心向前、後、左、右各挖一條 10 格通道，形成十字礦道。

**操作：**

1. 將 Agent 放在起點並確認下方可挖掘。
2. 在聊天欄輸入 `4`。
3. 程式結束後確認 Agent 回到十字中心附近，再進入礦道採集。

**知識點：** 多段迴圈、相反方向、位移後返回、十字座標關係。

**Python 程式碼：** [下載／查看 medium.py](code/medium.py)

```python
def on_on_chat():
    for index in range(10):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
    for index2 in range(10):
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.destroy(UP)
    agent.move(BACK, 10)
    for index3 in range(10):
        agent.destroy(BACK)
        agent.move(BACK, 1)
        agent.destroy(UP)
    agent.move(FORWARD, 10)
    for index4 in range(10):
        agent.destroy(LEFT)
        agent.move(LEFT, 1)
        agent.destroy(UP)
    agent.move(RIGHT, 10)
    for index5 in range(10):
        agent.destroy(RIGHT)
        agent.move(RIGHT, 1)
        agent.destroy(UP)
    agent.move(LEFT, 10)
player.on_chat("4", on_on_chat)
```

![中階十字挖礦積木程式](images/cross-mining.png)

**MakeCode 分享連結：** 待補

### 高階｜魚骨挖礦

**任務：** 使用外層迴圈重複建立主通道、左右支線及下一個分岔點，形成可延伸的魚骨礦道。

**操作：**

1. 將 Agent 放在礦道起點並確認前後空間足夠。
2. 在聊天欄輸入 `4`。中階與高階是不同 MakeCode 專案，指令相同不會互相影響。
3. 從上方或入口檢查主通道與支線是否規律重複。

**知識點：** 巢狀迴圈、模組化圖案、返回基準點、轉向與路徑規劃。

**Python 程式碼：** [下載／查看 high.py](code/high.py)

```python
def on_on_chat():
    for index in range(4):
        for index2 in range(5):
            agent.destroy(FORWARD)
            agent.move(FORWARD, 1)
            agent.destroy(UP)
        agent.move(BACK, 5)
        for index3 in range(5):
            agent.destroy(BACK)
            agent.move(BACK, 1)
            agent.destroy(UP)
        agent.move(FORWARD, 5)
        agent.turn(RIGHT_TURN)
        for index4 in range(3):
            agent.destroy(FORWARD)
            agent.move(FORWARD, 1)
            agent.destroy(UP)
        agent.turn(LEFT_TURN)
player.on_chat("4", on_on_chat)
```

![魚骨挖礦初階積木程式](images/fishbone-basic.png)

![魚骨挖礦進階積木程式](images/fishbone-advanced-01.png)

![魚骨挖礦成果參考](images/fishbone-advanced-02.png)

**MakeCode 分享連結：** 待補

## 場地與座標

### 地圖內的位置

- 本梯次沒有固定的世界座標；老師以當天世界的礦山或地下空地選擇起點。
- `course-reference.png` 中的 `Y` 值是礦物分布高度參考，不是神木村的集合座標。
- 建議樓梯挖礦由地表或山腰開始；十字與魚骨挖礦可先下降至老師指定高度，再水平展開。
- 若使用不同地圖，請先確認世界深度、基岩及熔岩位置，避免直接照搬舊版高度資料。

### 場地生成與保存方式

- 本課的礦道就是學生程式產生的成果，因此不另提供教師場地生成 Python。
- 本課沒有結構方塊檔；大型地下礦道也不適合用單一結構一次載入。
- 要保存乾淨場地，老師應在上課前匯出一份世界備份；每梯次從備份重新開啟。
- 若必須保存局部示範，可在遊戲內用結構方塊分段保存，但每段都要記錄同一個基準點與載入偏移。

## 上課知識點與講解方式

- **順序：** Agent 必須先破壞再移動，否則會撞到方塊。
- **迴圈：** 把「挖掘、移動、清出頭頂」包成重複動作，修改次數即可改變通道長度。
- **巢狀迴圈：** 內層負責一小段礦道，外層負責重複整個圖案。
- **方向與座標：** `FORWARD/BACK`、`LEFT/RIGHT` 是成對方向；走幾格再走相反方向相同格數，就能回到基準位置。
- **除錯：** 先檢查 Agent 面向，再檢查迴圈次數，最後檢查是否有返回中心的移動指令。
- **演算法比較：** 樓梯法適合安全下降；十字法由中心向四方探索；魚骨法用規律支線增加接觸礦脈的機會。
- **礦坑安全：** 不垂直下挖、保持照明、記錄入口方向，並確保有返回路線。

## 程式示範影片

- [樓梯挖礦：通往地心 2－鋪設道路](https://www.youtube.com/watch?v=FUCTJrbtGcE)
- [魚骨挖礦初階](https://youtu.be/R_x55AyWBao?list=PL3600H0DVFhTenKqNp7UFrT13vPh8vW-f)
- [Minecraft 礦物挖礦指南](https://youtu.be/F42QEtbTsCk)

## 延伸活動｜附魔與裝備維修

若主課程提早完成，可介紹附魔台、青金石及鐵砧，讓學生比較普通工具與附魔工具的差異。此活動不列入採礦挑戰得分。

![附魔活動參考圖一](images/enchant-activity-01.png)

![附魔活動參考圖二](images/enchant-activity-02.png)

- [Minecraft 新手附魔教學](https://youtu.be/aV1TDbfdcAo)

## 家長回饋公版

親愛的家長您好：

今天孩子參加 Minecraft 半日營「礦坑達人」，先認識礦坑照明、返回路線與避免垂直下挖等安全觀念，再運用 MakeCode 控制 Agent 自動開挖礦道。

程式課程的重點是指令順序、方向、迴圈與巢狀迴圈。孩子把「破壞方塊、移動、清出通道」組合成可重複的步驟，完成了＿＿＿＿挖礦程式，並實際進入自己建立的礦道採集資源。

今天孩子在＿＿＿＿方面表現良好；遇到＿＿＿＿時，也能透過檢查 Agent 面向、迴圈次數與移動方向進行除錯。回家後可以請孩子分享不同礦道形狀的用途，以及自己的程式如何讓 Agent 重複工作。
