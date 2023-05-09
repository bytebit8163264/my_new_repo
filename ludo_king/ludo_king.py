from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pandas as pd




templist = []
driver_path = "C:/Users/dm669/OneDrive/Documents/chrome webdriver/chromedriver.exe"
chr_options = Options()
# chr_options.add_experimental_option("detach", True)
chr_driver = webdriver.Chrome(driver_path, options=chr_options)
chr_driver.maximize_window()
chr_driver.get("https://play.google.com/store/apps/details?id=com.ludo.king&gl=in&hl=en")
t_title=(chr_driver.title).split("-")[0]
print(t_title)
chr_driver.find_element(By.XPATH, "//i[@class='google-material-icons VfPpkd-kBDsod W7A5Qb']").click()
t_description=chr_driver.find_element(By.XPATH, "//div/div[@jsname='bN97Pc']").get_attribute("innerText")
print(t_description.splitlines())
chr_driver.get("https://play.google.com/store/apps/details?id=com.ludo.king&gl=in&hl=en")
rating=chr_driver.find_element(By.XPATH, "//div[@class='jILTFe']").text
print(rating)
total_rating=chr_driver.find_element(By.XPATH, "//div[@class='EHUI5b']").text
print(total_rating)
# chr_driver.close()
raw_data = {'title': t_title,
            'description': t_description,
            'avg_rating': rating,
            'total_rating': total_rating,
            }
# df=pd.DataFrame({'title': t_title,
#             'description': t_description,
#             'avg_rating': rating,
#             'total_rating': total_rating,
#             },)
templist.append(raw_data)
df = pd.DataFrame(templist)
df = pd.DataFrame(templist, columns = ['title', 'description', 'avg_rating','total_rating'])
print(df)
df.to_csv("Ludoking.csv")