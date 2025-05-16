Selenium 自動化測試作品 – 表單填寫測試
This project uses Python + Selenium to perform a simple UI automation test on the DemoQA Text Box page.
It simulates user input and validates successful submission behavior.

本作品使用 Python + Selenium 對 DemoQA Text Box 頁面 進行簡單的自動化測試，模擬使用者填寫表單並送出，驗證其 UI 行為是否正常。



#Test Objective / 測試目標
Validate that the Text Box form accepts user input and displays results correctly.

Demonstrate ability to perform basic UI automation using Python and Selenium.

撰寫自動化腳本，驗證表單填寫功能是否如預期顯示送出結果。

展示使用 Python + Selenium 操作瀏覽器的基本能力。


#Scope of Testing / 測試範圍
填寫「Full Name」、「Email」、「Current Address」、「Permanent Address」四個欄位
點擊「Submit」按鈕
驗證送出結果是否正確顯示在畫面中（#output 元素）


#Tools Used / 使用工具
Python 3.x

Selenium 4.x

ChromeDriver

Visual Studio Code (or any editor)

#Execution & Result / 測試執行說明


安裝 Selenium：

pip install selenium


執行測試腳本：

python test_textbox.py
測試腳本會開啟瀏覽器、自動填寫表單、送出並擷取畫面，最後關閉。

