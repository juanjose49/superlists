from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class NewVisitorTest(StaticLiveServerTestCase):
	
	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table= self.browser.find_element_by_id('id_list_table')
		rows= table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retreive_it_later(self):
		
		#Cheryl has so much stuff to do, she decides that she needs to start a to-do list and goes the superlists website!
		self.browser.get(self.live_server_url)

		#She notices the header and page title say "To-Do"
		self.assertIn('To-Do',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)
		
		#She's invited to enter a an item to-do as soon as she lands on the page
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

		#She types "Buy Feathers"
		inputbox.send_keys('Buy peacock feathers')

		#When she hits enter, she is taken to a new URL
		#and the page now lists 1: buy peacock feathers as an item in list
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		#The site invites her to enter another item, she enters "Buy a hat"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy a hat')
		


		#She presses enter and the page updates and includes both items in the list
		inputbox.send_keys(Keys.ENTER)

		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Buy a hat')


		# a new user, Francis, goes to the site

		#we launch a new browser
		self.browser.quit()
		self.browser = webdriver.Firefox()

		#Francis visits the homepage and none of Edith's items are present
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('Buy a hat', page_text)


		#Francis starts his own list
		inputbox = self.browser.find_element_by_id('id_new_item')

		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		#Francis gets his own unique url
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url,edith_list_url)

		#there is no trace of Edith's list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)

	def test_layout_and_styling(self):
		#Edith goes to the home page
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024, 768)

		#she notices the input box is nicely centered
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2, 512,
			delta=5
			)

		#she starts a new list and the input box is centered there too
		inputbox.send_keys('testing\n')
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2, 512,
			delta=5
			)



