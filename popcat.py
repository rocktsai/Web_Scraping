# 操作 browser 的 API
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 期待元素出現要透過什麼方式指定，通常與 EC、WebDriverWait 一起使用
from selenium.webdriver.common.by import By

# 加入行為鍊 ActionChain (在 WebDriver 中模擬滑鼠移動、點繫、拖曳、按右鍵出現選單，以及鍵盤輸入文字、按下鍵盤上的按鈕等)
from selenium.webdriver.common.action_chains import ActionChains

# 加入鍵盤功能 (例如 Ctrl、Alt 等)
from selenium.webdriver.common.keys import Keys

# 強制等待 (執行期間休息一下)
from time import sleep

# 啟動瀏覽器工具的選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")  # 最大化視窗
my_options.add_argument("--incognito")  # 開啟無痕模式
my_options.add_argument("--disable-popup-blocking")  # 禁用彈出攔截
my_options.add_argument("--disable-notifications")  # 取消通知

# 使用 Chrome 的 WebDriver
driver = webdriver.Chrome(
    options=my_options,
    service=Service(ChromeDriverManager().install())
)

# 前往頁面 popcat.click 啵啵貓Popcat點擊競賽
driver.get('https://popcat.click/')
sleep(3)
more = driver.find_element(By.CSS_SELECTOR, 'button.show')

# 建立行為鍊
ac = ActionChains(driver)

ac.move_by_offset(745, 300)

count = 0

for i in range(10):
    ac.pause(1)
    for _ in range(100):
        ac.click()
        ac.pause(0.1)
        count += 1
    ac.move_to_element(more).click()
    ac.pause(3)
    ac.move_to_element(more).click()

ac.perform()

driver.quit()

print(f'啵啵貓被揍了{count}下')
