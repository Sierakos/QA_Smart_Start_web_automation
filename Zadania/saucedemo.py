import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SaucedemoTest(unittest.TestCase):

    # Konfigurowanie środowiska / przeglądarki
    def setUp(self):

        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_total_price_is_displayed_correctly(self):

        """
        Test that check if Total prace in checkout window is correct.
        """

        driver=self.driver
        driver.get("https://www.saucedemo.com/")

        login = driver.find_element(By.ID, 'user-name')
        login.send_keys("standard_user")

        password = driver.find_element(By.ID, 'password')
        password.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, 'login-button')
        login_button.click()

        add_backpack_to_cart = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack')
        add_backpack_to_cart.click()

        add_light_to_cart = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-bike-light')
        add_light_to_cart.click()

        add_jacker_to_cart = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-fleece-jacket')
        add_jacker_to_cart.click()

        shop_cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        shop_cart.click()

        checkout_button = driver.find_element(By.NAME, 'checkout')
        checkout_button.click()

        f_name = driver.find_element(By.NAME, 'firstName')
        f_name.send_keys("Grzegorz")

        l_name = driver.find_element(By.NAME, 'lastName')
        l_name.send_keys("Floryda")

        p_code = driver.find_element(By.NAME, 'postalCode')
        p_code.send_keys("Ameryka")

        continue_button = driver.find_element(By.NAME, 'continue')
        continue_button.click()

        total = driver.find_element(By.CLASS_NAME, 'summary_total_label')
        total_price = total.text[8::]

        self.assertEqual("97.17", total_price, "in this case, the total price should be 97.17")


        # Wiadomość pojawia się tylko gdy asercja powyżej się zgadza.
        # Wyświetla się szybciej niż są pokazane rezultaty testów więc
        # można założyć że kiedy się pojawi od razu to asercje przebiegły prawidłowo 
        print("THANK YOU FOR YOUR ORDER")

    # Kiedy wszystkie testy się zakończą zwolnij pamięć
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()