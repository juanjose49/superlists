from selenium import webdriver
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

#She notices the header says "To-Do"
		self.assertIn('To-Do',self.browser.title)
		self.fail('Finish the test!')
#She's invited to enter a an item to-do as soon as she lands on the page

#She types "Buy Feathers"

#When she hits enter, the page updates and the list now includes "Boy Feathers"

#The site invites her to enter another item, she enters "Buy a hat"

#She presses enter and the page updates and includes both items in the list

#Cheryl wonders if the site will remember her list. The site has generated a url for her list

#She visits that URL and finds her to-do list in tact.

#Satisfied, she goes back to sleep.
if __name__=='__main__':
	unittest.main(warnings='ignore')


