# 梯次 H｜巢狀迴圈：新夢幻農場

- 課程時間：09:00－12:00
- 遊戲版本：Minecraft Education
- 程式平台：Microsoft MakeCode
- 核心概念：Agent 控制、循序結構、迴圈、巢狀迴圈、耕種、播種、收割、物品欄切換

> 下圖為既有課程資訊圖，圖中的日期與活動資訊僅供辨識；實際上課資訊以當次通知為準。

![梯次 H 課程資訊圖](images/course-info.png)

## 課程目標

學生將從一條 5 格農田開始，逐步完成 5×5 自動收割農田，以及具有外圍柵欄的完整農場。課程結束前，每位學生都要能說明「內層迴圈處理一排，外層迴圈切換下一排」的運作方式。

## 課前準備

- 正式地圖：[神木村 v6](../shared/maps/神木村v6.mcworld)
- 備用地圖：[神木村 8 人版](maps/神木村8人版.mcworld)
- 每位學生配置互不重疊的平坦農地，至少預留 9×9 格空間。
- 農田旁放置水源，確保 5×5 耕地在水源有效範圍內。
- 低階：Agent 第 1 格放至少 5 個種子。
- 中階：老師先準備 5×5 成熟作物；Agent 第 1 格放至少 25 個種子。
- 高階：Agent 第 1 格放至少 25 個種子，第 2 格放至少 24 個柵欄。
- 確認學生有操作者權限、能召喚 Agent，且 Agent 面向與農田長邊一致。

## 半日營流程

| 時間 | 教學內容 |
|---|---|
| 09:00－09:10 | 開場、農場任務說明 |
| 09:10－09:35 | Minecraft 操作、耕地與播種暖身 |
| 09:35－10:15 | 低階：5 格農田與單層迴圈 |
| 10:15－10:35 | 低階測試、錯誤排查與成果驗收 |
| 10:35－10:45 | 休息 |
| 10:45－11:25 | 中階或高階：5×5 路線與巢狀迴圈 |
| 11:25－11:50 | 夢幻農場產量驗收賽 |
| 11:50－12:00 | 成果分享、知識點回顧 |

## 遊戲任務：夢幻農場產量驗收賽

### 共通規則

1. 每人選擇一個程度，Agent 就定位後不可手動修改農田。
2. 老師倒數後，學生只能執行一次對應聊天指令。
3. 程式停止後再計分；若路線錯誤，可在時間內修改後重新挑戰。
4. 各程度分開排行，避免完成內容不同卻直接比較速度。

### 計分方式

| 程度 | 驗收內容 | 計分 |
|---|---|---|
| 低階 | 一條 5 格農田 | 每格完成耕地 1 分、成功播種 1 分，共 10 分 |
| 中階 | 5×5 成熟農田收割並重新播種 | 每格成功重新播種 1 分；25 格全數完成再加 5 分，共 30 分 |
| 高階 | 5×5 播種農田與外圍柵欄 | 農田每格 1 分、柵欄無缺口 5 分，共 30 分 |

同分時依序比較：漏種格數較少、完成時間較短、能清楚解釋巢狀迴圈者。

## 低階｜耕地一條

### 任務

輸入聊天指令 `4`，讓 Agent 重複五次「耕種下方、播種、前進」，完成一條 5 格農田。

### MakeCode Python

```python
def on_on_chat():
    agent.move(UP, 1)
    agent.set_slot(1)
    for index in range(5):
        agent.till(DOWN)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
player.on_chat("4", on_on_chat)
```

- [下載低階 Python](code/low.py)
- MakeCode 分享連結：**待補**

`agent.set_slot(1)` 是為了固定使用第 1 格種子；既有積木圖未呈現這一步，實際上課建議補上，避免學生選錯物品欄。

![低階積木程式](images/farm-row-blocks.png)

### 場地起點與成果

- 既有成果圖記錄：玩家約在 `(154, 65, -127)`，Agent 約在 `(151, 66, -134)`。
- Agent 放在第一格農地上方並朝直線農地前進方向；不同地圖可使用任意座標，但起點、方向與淨空範圍必須相同。

![低階 5 格農田成果](images/farm-row-result.png)

## 中階｜5×5 自動收割與重新播種

### 任務

老師先準備 5×5 成熟農田。學生輸入聊天指令 `3`，讓 Agent 逐格收割、播種、收集掉落物，完成一排後回到排頭並向右換行。

### MakeCode Python

```python
def on_on_chat():
    agent.move(UP, 1)
    agent.set_slot(1)
    for index in range(5):
        for index2 in range(5):
            agent.move(FORWARD, 1)
            agent.destroy(DOWN)
            agent.place(DOWN)
            agent.collect_all()
        agent.move(BACK, 5)
        agent.move(RIGHT, 1)
player.on_chat("3", on_on_chat)
```

- [下載中階 Python](code/medium.py)
- MakeCode 分享連結：**待補**

![中階積木程式](images/auto-harvest-blocks.png)

### 場地起點與成果

- Agent 放在第一排第一格之前一格，面向農田。
- 前方需有 5 格、右側需有 5 排的可通行空間。
- 既有執行附件未清楚呈現農田結果；正式驗收請以 25 格重新播種與掉落物收集結果為準。

![中階既有執行附件](images/auto-harvest-result.png)

## 高階｜5×5 農田與外圍柵欄

### 任務

輸入聊天指令 `5`。Agent 先以兩層迴圈完成 5×5 耕地與播種，再切換到第 2 格物品，沿農田外圍放置柵欄。

### MakeCode Python

```python
def on_on_chat():
    agent.move(UP, 1)
    agent.set_slot(1)
    for index in range(5):
        for index2 in range(5):
            agent.move(FORWARD, 1)
            agent.till(DOWN)
            agent.place(DOWN)
        agent.move(BACK, 5)
        agent.move(RIGHT, 1)
    agent.move(DOWN, 1)
    agent.turn(RIGHT_TURN)
    agent.set_slot(2)
    for index3 in range(4):
        for index4 in range(6):
            agent.move(BACK, 1)
            agent.place(FORWARD)
        agent.turn(RIGHT_TURN)
    agent.move(FORWARD, 1)
player.on_chat("5", on_on_chat)
```

- [下載高階 Python](code/high.py)
- MakeCode 分享連結：**待補**

![高階積木程式](images/farm-fence-blocks.png)

### 場地起點與成果

- Agent 起點與中階相同，前方 5 格、右側 5 排，外圍另保留至少 1 格柵欄空間。
- 第 1 格必須是種子，第 2 格必須是柵欄；若使用不同方位，先以少量方塊測試轉向與柵欄路線。

![高階農田與柵欄成果](images/farm-fence-result.png)

## 場地保存、重置與跨地圖使用

### 座標與參考點

- 神木村內可沿用既有農場區；目前可確認的參考座標為玩家 `(154, 65, -127)`、Agent `(151, 66, -134)`。
- 座標只負責帶老師到附近，程式是否正確仍取決於 Agent 的起點與朝向。
- 換到其他地圖時，找平坦地面、指定一個「第一排第一格」作為共同參考點，再替每組保留至少 9×9 格。

### 保存方式

- 本梯次場地由學生程式直接生成，沒有必要另外製作結構方塊檔。
- 正式課前先保留一份未使用的 `.mcworld`；每場課由備份重新匯入，能同時保留座標、農田與多人區域配置。
- 若只需保存單一學生農田，可在遊戲內使用結構方塊分區保存；大型多人場地仍建議使用世界備份。

### 重置方式

- 低階／高階：清除作物與柵欄，將農地恢復成泥土後重新放置 Agent。
- 中階：補回 5×5 作物並使用骨粉催熟，再讓下一位學生執行。
- 大量重置時，直接退出並重新匯入未使用的世界備份最穩定。

### 教師場地程式

本梯次不另附教師場地 Python：低階與高階的學生程式本身就是場地生成流程；中階則需要成熟作物，使用世界備份或人工補種、骨粉催熟會比額外程式更直觀。

## 上課知識點

- **循序結構：** 耕地、播種、移動的順序改變，結果也會改變。
- **單層迴圈：** 把相同動作重複五次，避免複製大量積木。
- **巢狀迴圈：** 內層處理一排，外層負責換到下一排，形成二維農田。
- **座標與方向：** 相同程式放在不同起點或朝向，會生成在不同位置。
- **狀態與物品欄：** `set_slot` 決定 Agent 放置種子還是柵欄。
- **除錯方法：** 先用 2×2 小範圍確認移動、轉向與放置，再改回 5×5。
- **自動化觀念：** 程式不只節省時間，也讓每次耕作流程保持一致。

## 延伸活動

### 仙人掌骨粉機

時間足夠時，可依影片觀察沙子、仙人掌、水流、漏斗、堆肥桶與箱子的分工，再讓學生比較「手動建造」與「Agent 自動化」的差別。

![仙人掌骨粉機](images/cactus-bonemeal-farm.png)

### 馴狼、命名與染色項圈

準備狼生成蛋、骨頭、命名牌、鐵砧與染料。學生完成馴服後替狼命名並染色項圈，作為農場夥伴。

![不同顏色的狼項圈](images/dyed-dog-collars.png)

### 綿羊與染色羊毛

學生觀察綿羊、染料與羊毛顏色的關係，可延伸設計不同顏色的農場標誌。

## 程式示範影片

- 低階：[A_01 耕種並放種子](https://youtu.be/dDmJ1pzSbxM?list=PL3600H0DVFhTenKqNp7UFrT13vPh8vW-f)
- 中階：[20 機器人收割農作物](https://www.youtube.com/watch?v=4Gz8_x-En_E)
- 中階補充：[5 種出一片田](https://youtu.be/BebGaUguNQo?list=PL3600H0DVFhSzXec8B_GPnGsuRxV6wqmv)
- 高階：[19 綜合練習－種田與柵欄](https://www.youtube.com/watch?v=3GHG1HH6Vzo)
- 延伸：[仙人掌農場](https://youtu.be/OgoEZOrjXUU)
- 延伸：[你可能不知道的狼 10 件事](https://youtu.be/p9NplgkiC3g)
- 延伸：[你可能不知道的綿羊 10 件事](https://youtu.be/ns35nWpNx3E)

## 家長回饋公版

親愛的家長您好：

今天孩子完成了 Minecraft Education「新夢幻農場」課程，學習用程式控制 Agent 進行耕地、播種、收割與放置柵欄。課程從一條直線農田開始，再進階到 5×5 農田，讓孩子理解單層迴圈與巢狀迴圈如何把重複工作自動化。

孩子今天完成的程度為【低階／中階／高階】，課堂表現【請填寫具體表現，例如：能主動檢查 Agent 方向，並修正漏種問題】。在成果挑戰中，孩子完成【請填寫成果】，也練習從起點、方向、物品欄與迴圈次數逐步找出問題。

回家後可以請孩子分享：「為什麼 5×5 農田需要兩層迴圈？」讓孩子用自己的話整理今天的程式概念。
