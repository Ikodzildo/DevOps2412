from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("file:///C:/Users/goido/Downloads/tip_calc/tip_calc/index.html")
billamt = dr.find_element(by="id", value="billamt")
billamt.send_keys("100")
dr.find_element(by="xpath", value='//*[@id="serviceQual"]/option[3]').click()
dr.find_element(by="id", value='peopleamt').send_keys("5")
dr.find_element(by="id", value='musicquality').send_keys("5")
dr.find_element(by="id", value='calculate').click()
actual = dr.find_element(by="id", value="tip").text
expected = "7.00"
# if expected == actual:
#     print("all cool")
# else:
#     print("you have ruined the tip")
assert expected == actual
sleep(10)