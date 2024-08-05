import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class fitpeo():
    def fitpeopage(self):
       driver: WebDriver =webdriver.Chrome()
       driver.implicitly_wait(5)
       driver.get("https://www.fitpeo.com/")
       driver.maximize_window()
       driver.find_element(By.XPATH,"//div[contains(text(),'Revenue Calculator')]").click()
       driver.execute_script("window.scrollTo(0, 500)")

       #slider move
       slide = driver.find_element(By.CSS_SELECTOR,".MuiSlider-rail.css-3ndvyc")
       ActionChains(driver).drag_and_drop_by_offset(slide,1,0).perform()

        #enter 560 in the text field
       text_box = driver.find_element(By.CSS_SELECTOR,".MuiInputBase-input")
       text_box.send_keys(Keys.CONTROL + "a")
       text_box.send_keys(Keys.BACKSPACE)
       text_box.send_keys("560")
       # get value 560
       slider = driver.find_element(By.CSS_SELECTOR,".MuiInputBase-input")
       slider_value = slider.get_attribute('value')
       print("Slider Value:", slider_value)
       driver.execute_script("window.scrollTo(0, 900)")
       #Check box click
       Checkbox = driver.find_elements(By.XPATH,"(//input[@type='checkbox'])")
       Checkbox[0].click()
       Checkbox[1].click()
       Checkbox[2].click()
       Checkbox[7].click()
       #verify Reimbursement text
       header= driver.find_element(By.XPATH,"//p[@class='MuiTypography-root MuiTypography-body1 inter css-hocx5c'][normalize-space()='$75600']")
       header_text = header.text.strip().replace('\n', ' ')
       expected_value = "$75600"
       assert header_text == expected_value, f"Expected '{expected_value}', but got '{header_text}'"

ft = fitpeo()
ft.fitpeopage()





