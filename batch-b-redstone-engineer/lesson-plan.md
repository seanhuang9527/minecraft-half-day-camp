# 梯次B_迴圈：紅石工程師

- 課程時間：09:00－12:00
- 遊戲版本：Minecraft Education
- 程式平台：Microsoft MakeCode Python
- 核心概念：Agent 控制、方向、迴圈、巢狀迴圈與紅石供電
- 課程任務：讓 Agent 從 A 點鋪設 36 格動力鐵軌到 B 點
- 使用地圖：[下載神木村 v6](../shared/maps/神木村v6.mcworld)

## 課前準備

- 老師開啟神木村 v6，讓全班加入同一個世界。
- 學生執行程式時，將權限設為操作者（皇冠）。
- 確認每台電腦能開啟 Minecraft Education、進入 MakeCode 並召喚 Agent。
- Agent 物品欄第 1 格放動力鐵軌，第 2 格放紅石火把。
- 先帶學生熟悉 Agent 的前、後、左、右、上、下與物品欄切換。
- 先在「紅石工程大道」說明任務，再傳送到正式的 10 線測試場。
- 紅石工程大道傳送指令：`/tp -527 66 236`
- 10 線鐵路測試場傳送指令：`/tp -442 139 231`
- 每位學生站在不同顏色羊毛上；羊毛就是 Agent 鋪設第一格鐵軌的起點。
- 正式測試前，確認每條軌道底下是允許方塊，其他區域底下是拒絕方塊。

## 教師備課快速總覽

| 層級 | 聊天指令 | 程式重點 | 完成標準 |
|---|---:|---|---|
| **低階** | `1` | 單層迴圈，自動鋪設 36 格動力鐵軌 | 鐵軌從 A 點連續到達 B 點 |
| **中階（全班目標）** | `2` | 單層迴圈，每格嘗試供電 | 完成 36 格鐵軌，右側有紅石火把 |
| **高階** | `3` | 巢狀迴圈，每 9 格放 1 支火把 | 完成 36 格鐵軌，只使用 4 支火把 |

## 遊戲內容

### 一、紅石工程大道

老師先帶學生到紅石工程大道，認識紅石電力、動力鐵軌和紅石火把，並說明今天要讓 Agent 從 A 點鋪設鐵路到 B 點。這一階段以觀察、預測與短距離測試為主，不一定要安排比賽。

![紅石工程大道](images/redstone-engineering-road.png)

傳送指令：

```text
/tp -527 66 236
```

### 二、10 線鐵路測試場

正式場地共有 10 條路線。不同顏色羊毛用來標示學生與 Agent 的起點；紅色羊毛標示 B 點。學生站上自己的羊毛，召喚 Agent 並統一面向後，再執行程式。

![10 線鐵路測試場](images/railway-test-field.png)

傳送指令：

```text
/tp -442 139 231
```

場地規則：

1. 每位學生選一種顏色羊毛，Agent 站在羊毛上方。
2. 第 1 格動力鐵軌會放在起點羊毛上方。
3. 從 A 點到 B 點共有 36 格鐵軌。
4. 軌道及右側紅石火把的範圍底下使用允許方塊。
5. 其他區域底下使用拒絕方塊，避免學生破壞場地。
6. 低階先確認鐵軌完整；中階比較「每格放火把」的效果；高階挑戰節能供電。

### 三、成果測試

- 檢查鐵軌是否連續，沒有漏放或超出終點。
- 放置礦車，確認能從 A 點沿著鐵軌前往 B 點。
- 比較中階與高階使用的紅石火把數量。
- 請學生說明巢狀迴圈如何把「8 格一般鋪設＋1 格供電」重複 4 次。
- 活動可採個人測試、兩人互相檢查或全班展示，不必設定競賽。

## 程式示範影片

- [6. 紅石點燈](https://www.youtube.com/watch?v=nbwJHj0DYB4)
- [6-1. 紅石點燈（正方形版）](https://www.youtube.com/watch?v=wuuGF71qjdQ)
- [36. 用紅石裝置練習物品欄切換](https://www.youtube.com/watch?v=2MD8TdhEpB0)
- [59. 巢狀迴圈節能鐵路](https://youtu.be/QbJUFraUPdU?si=FAkuhIfF4iF2hXyK)

## 程式內容

### 低階：36 格動力鐵軌

使用單層迴圈，讓 Agent 重複前進並把動力鐵軌放在身後。

```python
def on_on_chat():
    agent.set_slot(1)

    for index in range(36):
        agent.move(FORWARD, 1)
        agent.place(BACK)

player.on_chat("1", on_on_chat)
```

- [下載低階程式](code/low.py)

![低階積木程式](images/low-program.png)

### 中階：每格放置紅石火把

每次迴圈先在 Agent 右側放紅石火把，再前進並把動力鐵軌放在身後。這個版本適合觀察供電，但火把數量較多。

```python
def on_on_chat():
    for index in range(36):
        agent.set_slot(2)
        agent.place(RIGHT)

        agent.set_slot(1)
        agent.move(FORWARD, 1)
        agent.place(BACK)

player.on_chat("2", on_on_chat)
```

- [下載中階程式](code/medium.py)

![中階積木程式](images/medium-program.png)

### 高階：巢狀迴圈節能鐵路

外層迴圈執行 4 次；每次先用內層迴圈鋪 8 格，再放 1 支紅石火把並鋪第 9 格。最後完成 36 格鐵軌，只使用 4 支火把。

```python
def on_on_chat():
    agent.set_slot(1)

    for index in range(4):
        for index2 in range(8):
            agent.move(FORWARD, 1)
            agent.place(BACK)

        agent.set_slot(2)
        agent.place(RIGHT)

        agent.set_slot(1)
        agent.move(FORWARD, 1)
        agent.place(BACK)

player.on_chat("3", on_on_chat)
```

- [下載高階程式](code/high.py)

![高階積木程式](images/high-program.png)

## 教師用：建立 10 線測試場

老師站在預定場地中央並面向鐵路前進方向，輸入聊天指令 `9`。程式會建立石頭地面、拒絕方塊底層、10 條允許建造區、不同顏色起點羊毛、紅色終點羊毛與玻璃邊界。

```python
def build_lane(lane_x, start_wool):
    blocks.fill(
        blocks.block_by_name("allow"),
        pos(lane_x - 1, -2, 0),
        pos(lane_x + 1, -2, 40),
        FillOperation.REPLACE
    )

    blocks.place(start_wool, pos(lane_x, -1, 2))
    blocks.place(RED_WOOL, pos(lane_x, -1, 37))
    blocks.place(GLASS, pos(lane_x, 0, 1))
    blocks.place(GLASS, pos(lane_x, 0, 39))

    blocks.fill(
        YELLOW_WOOL,
        pos(lane_x + 2, -1, 0),
        pos(lane_x + 2, -1, 40),
        FillOperation.REPLACE
    )


def on_on_chat():
    blocks.fill(
        AIR,
        pos(-20, 0, 0),
        pos(20, 5, 40),
        FillOperation.REPLACE
    )

    blocks.fill(
        blocks.block_by_name("deny"),
        pos(-20, -2, 0),
        pos(20, -2, 40),
        FillOperation.REPLACE
    )

    blocks.fill(
        STONE,
        pos(-20, -1, 0),
        pos(20, -1, 40),
        FillOperation.REPLACE
    )

    build_lane(-18, blocks.block_by_name("white_wool"))
    build_lane(-14, blocks.block_by_name("orange_wool"))
    build_lane(-10, blocks.block_by_name("yellow_wool"))
    build_lane(-6, blocks.block_by_name("lime_wool"))
    build_lane(-2, blocks.block_by_name("green_wool"))
    build_lane(2, blocks.block_by_name("cyan_wool"))
    build_lane(6, blocks.block_by_name("light_blue_wool"))
    build_lane(10, blocks.block_by_name("blue_wool"))
    build_lane(14, blocks.block_by_name("purple_wool"))
    build_lane(18, blocks.block_by_name("magenta_wool"))

    player.tell(
        mobs.target(LOCAL_PLAYER),
        "10線紅石鐵路測試場完成"
    )

player.on_chat("9", on_on_chat)
```

## 半日營標準流程

| 時間 | 流程大綱 |
|---|---|
| **09:00－09:10** | 開場、自我介紹與破冰 |
| **09:10－09:35** | Minecraft 操作、Agent 方向與紅石暖身 |
| **09:35－10:15** | 低階程式：36 格動力鐵軌 |
| **10:15－10:35** | A 點到 B 點功能測試 |
| **10:35－10:45** | 休息時間 |
| **10:45－11:15** | 中階程式：加入紅石火把 |
| **11:15－11:40** | 高階程式：巢狀迴圈節能鐵路 |
| **11:40－11:50** | 礦車測試、成果展示與除錯 |
| **11:50－12:00** | 程式概念複習與收尾 |

## 分級教學設計

| 層級 | 適合學生 | 必學概念 | 過關方式 |
|---|---|---|---|
| **低階** | 第一次玩 Minecraft 或第一次寫程式 | Agent 移動、物品欄、單層迴圈 | 完成 36 格連續動力鐵軌 |
| **中階（全班目標）** | 大部分學生 | 在迴圈中切換物品並向右放置 | 鐵軌與紅石火把都能正確放置 |
| **高階** | 進度較快或已熟悉迴圈 | 巢狀迴圈、分組重複、節省材料 | 以 4 支火把完成 36 格供電鐵路 |

## 家長回饋

親愛的家長您好：

今天的 Minecraft 半日營主題是「紅石工程師」。孩子先認識動力鐵軌、紅石火把與 Agent 的方向，再使用迴圈讓 Agent 從 A 點自動鋪設 36 格鐵軌到 B 點。

完成基礎版本後，孩子進一步練習在程式中切換物品欄並放置紅石火把。進度較快的孩子也挑戰巢狀迴圈，把重複工作分成「每 9 格一組」，用更少的紅石火把完成節能鐵路。最後大家透過礦車測試成果，觀察程式是否有漏放、方向錯誤或材料使用過多的情況。

這堂課不只練習迴圈，也讓孩子從實際成果理解程式設計中的規律、除錯與資源效率。孩子今天都很認真，也順利完成自己的鐵路工程！

<details>
<summary>查看原教案家長回饋</summary>

親愛的家長您好：

今天是 Minecraft 半日營的「紅石工程師」。

我們首先帶孩子們複習了 Minecraft 世界中的基本操作。

進入程式設計的單元後，我們使用了三個基礎指令，分別是「召喚」、「轉動」與「前進」，讓孩子們操控機器人進行簡單的動作。

今天的重點是認識 Minecraft 中的紅石系統。紅石在遊戲中就像真實世界的電力系統，紅石方塊就像電源、紅石粉如同電線、中繼器則像延長線。

接著，我們讓孩子們透過程式指令控制機器人，除了介紹「迴圈」的概念，並且實際運用迴圈來讓機器人挖礦。

今天每位孩子都表現得非常棒，也順利完成了指定的任務～

</details>

## 原教案參考資料

以下舊資料保留在 GitHub，方便老師需要時查閱，但不列入本次正式三階鐵路課程：

- 十字挖礦法：`images/cross-mining.png`
- 魚骨挖礦法初階版：`images/fishbone-basic.png`
- 紅石活塞門：`images/piston-door.png`
- 紅石陷阱門：`images/trapdoor.png`
- 紅石自動化農場：`images/auto-farm-*.png`
- 紅石焚化爐：`images/incinerator-*.png`
- [你可能不知道的紅石的 10 件事](https://youtu.be/eAq2rPhRoow)
- [隱藏 2×2 活塞門](https://youtu.be/VuXbVEHB0xI)
- [半自動小麥收割機製作](https://youtu.be/XzjnPqRDU00)
- [紅石焚化爐](https://youtu.be/dHRh5E5UXjQ?si=VGCUvFC5SOHtwp_N)

## 教師課後確認

- [ ] 學生知道不同顏色羊毛是自己與 Agent 的鐵軌起點。
- [ ] Agent 第 1 格為動力鐵軌，第 2 格為紅石火把。
- [ ] 全班至少完成低階 36 格鐵軌，大部分學生完成中階。
- [ ] 進度快的學生能說明高階巢狀迴圈的 4 × 9 結構。
- [ ] 學生實際以礦車測試 A 點到 B 點。
- [ ] 軌道區底下是允許方塊，其他場地底下是拒絕方塊。
- [ ] 下課前完成迴圈、巢狀迴圈與節省材料的概念複習。
