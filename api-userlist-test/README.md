# API Test Project – User List Testing/# API 測試作品 – 用戶列表查詢測試

This project tests the /users API endpoint from [JSONPlaceholder](https://jsonplaceholder.typicode.com/).  
It verifies responses for user list retrieval, single user retrieval, querying non-existent users, and incorrect HTTP methods.

本作品針對 [JSONPlaceholder](https://jsonplaceholder.typicode.com/) 提供的 /users API 進行測試，涵蓋用戶列表查詢、單一用戶查詢、查詢不存在用戶及錯誤 HTTP 方法操作。

---

##  Test Objective / 測試目標

- Validate the normal and edge-case responses of the `/users` API endpoint.
- Confirm correct status codes, data structures, and API behaviors.
- Practice API test design and reporting with Postman.

- 驗證 `/users` API 端點的正常回應與邊界情境回應。
- 確認回傳狀態碼、資料結構及 API 行為是否正確。
- 練習使用 Postman 設計 API 測試並撰寫測試報告。

---

##  Scope of Testing / 測試範圍

- GET `/users` → 查詢全部用戶
- GET `/users/1` → 查詢單一用戶
- GET `/users/999` → 查詢不存在的用戶
- POST `/users` → 嘗試使用錯誤方法（模擬回傳）


##  Project Structure / 專案結構
api-userlist-test/ ├─ README.md ├─ test-report/ │ └─ Konan_UserList_API_Test_Report.docx ├─ postman-collection.json ├─ screenshots/ │ ├─ get-all-users.png │ ├─ get-user-1.png │ ├─ get-user-999.png │ └─ post-users-error.png


## Test Cases Summary / 測試案例摘要

| 測試編號 | 測試項目 | 結論 |
|----------|---------|------|
| TC01 | 查詢全部用戶 | ✅ |
| TC02 | 查詢單一用戶 | ✅ |
| TC03 | 查詢不存在用戶 | ✅ |
| TC04 | 錯誤方法 POST /users | ✅ |

---


##  Tools Used / 使用工具

- Postman
- Windows 11 / Chrome
- Microsoft Word (for test report)
