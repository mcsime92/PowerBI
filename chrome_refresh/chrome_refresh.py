import datetime
from selenium import webdriver
from time import sleep, time

### TODO on to make it work
# TODO 1: Update your version of chrome
# TODO 2: Download proper version of chromedriver.exe http://chromedriver.chromium.org/
# TODO 3: Add it to the path where python script can be found

# Starts Chrome
driver = webdriver.Chrome('chromedriver.exe')

# Goes to URL
driver.get("ADD HERE YOUR URL")

# In case the user needs to log into some platform
def log_in():
    print('Log-in time - sleep')
    start_time = time()
    sleep(35)
    end_time = time()
    total_time = int(end_time - start_time)
    print("Log-in took: " + str(total_time))
    print('End log-in time - sleep')

# Comment out if not needed.
log_in()

# Refreshes page every 15 seconds
while True:
    now = datetime.datetime.now()
    sleep(15)
    #sleep(60)
    driver.refresh()
    print('Refreshed: ' + str(now.strftime("%Y-%m-%d %H:%M:%S")))
