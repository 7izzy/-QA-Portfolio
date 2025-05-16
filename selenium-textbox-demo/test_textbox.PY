from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 啟動 Chrome 瀏覽器（你必須安裝 ChromeDriver）
driver = webdriver.Chrome()

# 開啟目標網頁
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

# 填入欄位資料
driver.find_element(By.ID, "userName").send_keys("Konan")
driver.find_element(By.ID, "userEmail").send_keys("konan@example.com")
driver.find_element(By.ID, "currentAddress").send_keys("123 Test Street")
driver.find_element(By.ID, "permanentAddress").send_keys("456 Permanent Street")

# 等待2秒讓頁面穩定 / 廣告消失
time.sleep(2)

# 提交表單
driver.find_element(By.ID, "submit").click()

# 等一下讓頁面渲染完成
time.sleep(2)

# 取得送出結果
output = driver.find_element(By.ID, "output").text
print("表單送出結果：")
print(output)

# 關閉瀏覽器
driver.quit()
