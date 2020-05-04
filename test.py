from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
#search_box = driver.find_element_by_id('search_query_top')
#search_box.send_keys('Hola Mundo')
driver.find_element_by_id('search_query_top').send_keys('Hola Mundo')
#search_box_button = driver.find_element_by_name('submit_search')
#search_box_button.click()
driver.find_element_by_name('submit_search').click()
time.sleep(2)
#results_label = driver.find_element_by_xpath('//*[@id="center_column"]/p')
#tc.assertEqual('No results were found for your search "Hola Mundo"',results_label.text)
tc.assertEqual('No results were found for your search "Hola Mundo"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text)
#women_link = driver.find_element_by_link_text('Women')
#women_link.click()
driver.find_element_by_link_text('Women').click()
time.sleep(2)
#dress_link = driver.find_element_by_partial_link_text('Dres')
#dress_linl.click()
driver.find_element_by_partial_link_text('res').click()
time.sleep(2)
driver.close()
driver.quit()