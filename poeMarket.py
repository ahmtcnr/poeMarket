from selenium.webdriver.common.keys import Keys
import time
import selenium.webdriver
import rawJson
import jsonToText
from pynput.keyboard import Key, Controller
keyboard = Controller()
print("0- Custom")
print("1- Thread of Hope - Small")
print("2- Thread of Hope - Medium")
print("3- Thread of Hope - Large")
print("4- Thread of Hope - XLarge")
print("5- Mana Leech & Life Jewel")
print("6- Cinderswallow Urn Flask")
print("7- Vendor's Gamble")
print("8- Circle Types ")
print("9- Circle Types ")
print("10- Circle Types")
print("11- Circle Types")
print("12- Atziri Foible %24")
print("13- Atziri Foible %25 ve fazlası")
print("14- Abyssus 40%")
print("15- Mindsprial")




text_file = open("sample.txt", "w")
text1 = "/html/body/div[1]/div/div[1]/div[5]/div[6]/div[2]/div[{}]"

inputVal = int(input())
inputItem = ""
priceV=""
if (inputVal == 1): 
    inputItem = "https://www.pathofexile.com/trade/search/Delirium/YyqalGRUY"
    priceV = " 10c"

elif (inputVal == 2):
    
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/GvO7pr8Fb"
            priceV = " 10c"
    
elif (inputVal == 3):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/wvLByrnhb"
            priceV = " 10c"
    
elif (inputVal == 4):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/VR6VdqPtp"
            priceV = " 10c"
    
elif (inputVal == 5):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/KPnO36s5"
            priceV = " 10c"
    
elif (inputVal == 6):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/PvpzvYqsL"
            priceV = " 1ex"
    
elif (inputVal == 7):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/My509KPhJ"
            priceV = " 10c"
    
elif (inputVal == 8):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/glVzJ8jIQ"
            priceV = " 10c"
    
elif (inputVal == 9):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/nBvWZRT0"
            priceV = " 10c"
    
elif (inputVal == 10):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/EqX5eRT5"
            priceV = " 10c"
    
elif (inputVal == 11):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/aLp3wpMfe"
            priceV = " 10c"
    
elif (inputVal == 12):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/aV2j87RSe"
            priceV = " 4c"

elif (inputVal == 13):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/mvDDp5Mu6"
            priceV = " 10c"
    
elif (inputVal == 14):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/3nbPjBGU5"
            priceV = " 5c"

elif (inputVal == 15):
            inputItem = "https://www.pathofexile.com/trade/search/Delirium/8nb75lMcV"
            priceV = " 5c"
elif (inputVal == 0):
            print("Link> ")
            inputItem = input()
            print("Offering Price> ")
            priceV = input()
    
 



driver = selenium.webdriver.Firefox()
driver.get(inputItem)
lastElement = driver.find_elements_by_id("item-resultset-template")[-1]



time.sleep(4)

html = driver.find_element_by_tag_name('html')
i=1
while True:
    
    
    html.send_keys(Keys.END)
    i+=1
    if(i==1000):
        break


count = len(driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div[5]/div[6]/div[2]/div"))
                                           
j=1
while True:
    if(count == j):
        driver.quit()
        jsonToText.writeTxt(priceV)
        #keyboard.press(Key.f1)
        #keyboard.release(Key.f1)
        break
    login_form = driver.find_element_by_xpath(text1.format(j)).get_attribute("data-id")

    rawJson.makeJson(login_form,priceV);
    j+=1



