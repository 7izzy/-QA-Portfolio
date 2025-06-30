from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_login_and_add_to_cart():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # 使用純無痕模式，不要指定 user-data-dir

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://automationexercise.com")

        # 清除所有 cookie，確保無登入狀態
        driver.delete_all_cookies()
        driver.refresh()

        # 等待並點擊 Signup / Login
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
        login_link.click()

        # 輸入帳號密碼登入
        wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("zxc2525123@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("cxz2525123")
        driver.find_element(By.XPATH, "//button[text()='Login']").click()

        # 驗證登入成功
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))
        assert "Logged in as" in driver.page_source

        # 建立資料夾並截圖 — 登入成功畫面
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot("screenshots/after_login.png")

        # 點擊第一個 Add to cart 按鈕
        add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='btn btn-default add-to-cart'])[1]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart)
        add_to_cart.click()

        # 驗證 View Cart 出現
        wait.until(EC.presence_of_element_located((By.XPATH, "//u[text()='View Cart']")))
        assert "View Cart" in driver.page_source

        # 截圖 — 加入購物車後畫面
        driver.save_screenshot("screenshots/after_add_to_cart.png")

    finally:
        driver.quit()
