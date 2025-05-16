from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def login_and_capture(username, password, screenshot_name):
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    # 輸入帳號密碼
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "radius").click()

    time.sleep(2)
    
    # 擷取結果訊息
    message = driver.find_element(By.ID, "flash").text
    print(f"輸入：{username} / {password}")
    print("結果訊息：", message.strip())

    # 截圖存檔
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(f"screenshots/{screenshot_name}.png")
    
    driver.quit()
    return message

# 三種情境
login_and_capture("tomsmith", "SuperSecretPassword!", "TC01_success_login")
login_and_capture("tomsmith", "wrongpassword", "TC02_wrong_password")
login_and_capture("", "", "TC03_blank_input")
