
---

# Selenium UI Test – Login Function

# Selenium 自動化測試作品 – 登入功能測試

This project performs automated testing on the login feature of [the-internet.herokuapp.com](https://the-internet.herokuapp.com/login) using Python + Selenium.
It covers login with correct credentials, incorrect password, and blank inputs to verify the system's response and error handling.

本作品使用 Python + Selenium 對 [the-internet.herokuapp.com](https://the-internet.herokuapp.com/login) 登入功能進行自動化測試，涵蓋正確登入、密碼錯誤、空白欄位三種情境，驗證系統反應與錯誤提示是否正確。

---

##  Test Objective / 測試目標

* Test login behavior under different input scenarios

* Validate success and error messages displayed on the UI

* Demonstrate basic test automation using Selenium

* 測試不同輸入情境下的登入功能反應

* 驗證畫面上顯示的成功與錯誤訊息

* 展示使用 Selenium 撰寫 UI 自動化測試的基本能力

---

##  Scope of Testing / 測試範圍

| Test Case | Input                               | Expected Result                    |
| --------- | ----------------------------------- | ---------------------------------- |
| TC01      | `tomsmith` / `SuperSecretPassword!` | Login success message              |
| TC02      | `tomsmith` / `wrongpassword`        | Error: "Your password is invalid!" |
| TC03      | (blank) / (blank)                   | Error: "Your username is invalid!" |

---


---

##  Tools Used / 使用工具

* Python 3.x
* Selenium 4.x
* ChromeDriver
* VS Code / Command Line

---


