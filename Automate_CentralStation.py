from selenium import webdriver

browser = webdriver.Safari()
browser.get('https://centralstation.apple.com/nav_to.do?uri=%2Fsys_report_template.do%3Fjvar_report_id%3D4627e2e9c3715010c1ea47e8dd5d7596')

elem = browser.find_element_by_xpath('//*[@id="8a7a1132c30a101020fd4de8dd5d75fe_table"]/tbody')

print(elem)

