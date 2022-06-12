import time

import pyfiglet
from pyfiglet import *
from selenium import webdriver
import os
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()

chrome_options.add_argument('log-level=3')
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)




def ref():
    global profile_name
    global profile_status
    global elements_1
    global amount_of_com
    os.system('cls')
    text = pyfiglet.Figlet(font="big")
    os.system("mode con: cols=200 lines=40")
    aut_text = Figlet(font='big')
    print(aut_text.renderText("selfiction \nand\n nxbodyevzncvre"))
    time.sleep(5)
    os.system('cls')
    print(text.renderText("VK LOGGER"))



    profile_id = input('Введите ID профиля: ')
    if profile_id == "__EXIT__":
        exit()
    url = f'https://vk.com/{profile_id}'
    driver.get(url)
    try:
        profile_name = driver.find_element(
            By.XPATH, '//*[@id="page_info_wrap"]/div[1]/h1').text
        profile_status = driver.find_element(
            By.XPATH, '//*[@id="page_info_wrap"]/div[1]/div[1]/div').text
    except:
        print('Ошибка, профиль может быть удалён либо закрыт!')
        ref()
    profile_exceptions = {"online", "онлайн"}
    if profile_status == profile_exceptions:
        profile_status = "пользователь онлайн!"
    else:
        profile_status = profile_status
    named_tuple = time.localtime()
    time_string = time.strftime("%m/%d, %H:%M:%S", named_tuple)
    driver.refresh()

    print("Статус пользователя: ", profile_status)
    print("Имя пользователя: ", profile_name)
    clickable = driver.find_element(By.XPATH, '//*[@id="profile_idols"]/a')

    ActionChains(driver) \
        .click(clickable) \
        .perform()
    time.sleep(1)
    com = driver.find_element(
        By.XPATH, '//*[@id="box_layer"]/div[2]/div/div[1]/div[3]/span').text

    clickable_2 = driver.find_element(
        By.XPATH, '//*[@id="box_layer"]/div[2]/div/div[1]/div[3]')
    ActionChains(driver)\
        .click(clickable_2) \
        .perform()
# Scroll down to bottom

    time.sleep(1)
    amount_of_com = int(com)


    for i in range(amount_of_com // 20):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        print(f'Процесс: {i + 1} из {amount_of_com // 20}')


        time.sleep(1.5)

        i += 1
        os.system('cls')
        elements_1 = driver.find_elements(By.CLASS_NAME, 'fans_idol_lnk')

    for e in elements_1:

        file = open(f"{profile_name}.txt", mode='a', encoding='utf-8')
        file.write(e.text + "\n")
        file.close()

    f = open('info.txt', mode='w')
    f.write(f"Профиль: {profile_name}" + "\n" + f"Статус профиля: {profile_status}" + "\n" +
            f"ID профиля: {profile_id}" + "\n" + f"Время проверки: {time_string}" + "\n" + "\n")
    f.write(f"Количество прокруток: {amount_of_com // 20} \n")
    # Get scroll height
    f.write(
        f"Список групп пользователей находится в файле {profile_name}.txt \n" + f"Количество групп пользователя: {amount_of_com}")
    f.close()
    print("Информация о пользователе обновлена!")
    time.sleep(5)





while True:
    ref()
