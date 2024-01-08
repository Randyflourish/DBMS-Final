# DBMS-Final
組員：陳均凱、羅鵬博、黃哲宇、張智鈞

### 更新日誌 2024/1/5 ：
新增登入功能

待辦：
- [ ] 優化登入頁面
- [ ] 驗證用戶身分功能

### 更新日誌 2024/1/6 ：
改善登入頁面

### 更新日誌 2024/1/7 ：
修正了登入與錯誤帳號密碼的路由，現在會變得較為合理：
#### 目前網頁會有三種狀態：
1. 未登入
2. 登入失敗
3. 登入成功

- 在進入首頁時，會導向 / 路由
- 在試圖登入並且成功時，會導向 index/<user> 路由
- 在試圖登入並且失敗時，會導向 index/Unknown 路由。
    - 這是一個小小的技巧，將 Unknown 視為一個用戶。

在登入成功時，右上角的 sort 圖示會改為 list ，按下後會將使用者導向 / 路由，作為登出的功能。

### 更新日至 2024/1/8 ：
增加了以下功能：
- [X]從個人頁面 [ index/<user> ] 到 願望清單 [ favorite/<user> ] 的路由。
- [X]從任何頁面到 搜尋結果 [ /search?<paras> ] 的路由。