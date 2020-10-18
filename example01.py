from selenium import webdriver

    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
    # enable browser logging
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = { 'performance':'ALL' }

    driver = webdriver.Chrome(executable_path="c:\\windows\\chromedriver.exe",
                              service_args=["--verbose", "--log-path=D:\\temp3\\chromedriverxx.log"],
                              desired_capabilities=d)

    driver.get('https://api.ipify.org/?format=text')

    print(driver.title)

    print(driver.page_source)

    performance_log = driver.get_log('performance')
    print (str(performance_log).strip('[]'))

    for entry in driver.get_log('performance'):
        print (entry)