from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retreive_it_later(self):
		
		#Cheryl has so much stuff to do, she decides that she needs to start a to-do list and goes the superlists website!
		self.browser.get('http://localhost:8000')

		#She notices the header and page title say "To-Do"
		self.assertIn('To-Do',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)
		
		#She's invited to enter a an item to-do as soon as she lands on the page
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

		#She types "Buy Feathers"
		inputbox.sendkeys('Buy peacock feathers')

		#When she hits enter, the page updates and the list now includes "Boy Feathers"
		inputbox.sendkeys(keys.ENTER)

		table= self.browser.find_element_by_id('id_list_table')
		rows= table.find_elements_by_id('tr')

		self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows))

		#The site invites her to enter another item, she enters "Buy a hat"
		self.fail('finish the test!')
		#She presses enter and the page updates and includes both items in the list

		#Cheryl wonders if the site will remember her list. The site has generated a url for her list

		#She visits that URL and finds her to-do list in tact.

		#Satisfied, she goes back to sleep.
if __name__=='__main__':
	unittest.main(warnings='ignore')


