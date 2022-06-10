from selenium import webdriver
import time






driver = webdriver.Chrome(executable_path=r'C:\Users\hp\Desktop\proj\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("headless")


def ref():
    profile_id = input('Введите ID профиля: ')
    url = f'https://vk.com/{profile_id}'
    driver.get(url)
    try:
        profile_name = driver.find_element_by_xpath('//*[@id="page_info_wrap"]/div[1]/h1').text
        profile_status = driver.find_element_by_xpath('//*[@id="page_info_wrap"]/div[1]/div[1]/div').text
    except:
        print('Ошибка, профиль может быть удалён либо закрыт!')
        ref()
    named_tuple = time.localtime()
    time_string = time.strftime("%m/%d, %H:%M:%S", named_tuple)
    driver.refresh()

    f = open('info.txt', mode='a')
    f.write(f"Профиль: {profile_name}"+ "\n" + f"Статус профиля: {profile_status}" + "\n" + f"ID профиля: {profile_id}" + "\n" )
    f.close()


while True:
        ref()

