from selenium import webdriver
chrome = webdriver.Chrome()
chrome.get("https://techstepacademy.com/trial-of-the-stones")

# Elements :Riddel of Stone
riddle_of_stone_input = chrome.find_element_by_css_selector("input#r1Input")
riddle_of_stone_button = chrome.find_element_by_css_selector("button#r1Btn")

# Elements :Riddle of Secrets
riddle_of_secret_input = chrome.find_element_by_css_selector("input#r2Input")
fill_riddle_of_secret_text = chrome.find_element_by_css_selector("#passwordBanner>h4")
riddle_of_secret_button  = chrome.find_element_by_css_selector("button#r2Butn")

# Elements :The two Merchants
the_two_merchants_input = chrome.find_element_by_id("r3Input")
the_two_merchants_button = chrome.find_element_by_id("r3Butn")

# Elements :Final Check
final_check_button = chrome.find_element_by_id("checkButn")

# Elements :Last Message
last_msg  = chrome.find_element_by_css_selector("div#trialCompleteBanner>h4")

# Richect Merchant Name
names = ['Jessica','Bernard']
def richest_merchant(names):
    name_with_wealth= []
    for name in names:
        name_with_wealth.append((name, int(chrome.find_element_by_xpath("//b[text()=\'{}\']/../../p".format(name)).text)))
        sorted_values = sorted(name_with_wealth, key = lambda x:x[1])
    for value in sorted_values:
        if value[1]==sorted_values[-1][1]:
            return value[0]

# Execution for Riddle of Stone
riddle_of_stone_input.send_keys("rock")
riddle_of_stone_button.click()

#Execution for Riddle of Secrets
fill_answer = fill_riddle_of_secret_text.text
riddle_of_secret_input.send_keys(fill_answer)
riddle_of_secret_button.click()

#Execution for The Two Merchants
the_two_merchants_input.send_keys(richest_merchant(names))
the_two_merchants_button.click()

#Execute final button
final_check_button.click()

assert last_msg.text == "Trial Complete"














