#!/usr/bin/python
import requests, os
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

# Чтобы colorama работала на Windows
init(autoreset=True)

# Цвета
RED = "\033[1;31m"
GREEN = "\033[1;32m"
WHITE = "\033[1;37m"
YELLOW = "\033[1;33m"

os.system("clear")
print(RED + "[-----------------" + WHITE + "Python" + RED + "-" + WHITE + "Parser" + RED + "-----------------]")
print(WHITE + "  [" + GREEN + "+" + WHITE + "] По вопросам:")
print(WHITE + "  [" + GREEN + "+" + WHITE + "] Telegram -> @zharyqtyq")
print(WHITE + "  [" + GREEN + "+" + WHITE + "] Instagram -> @zharyqtyq_")
print("")
site = input(WHITE + "  [" + GREEN + "+" + WHITE + "] Введите сайт для парсинга: " + Style.RESET_ALL)
pars_class = input(WHITE + "  [" + GREEN + "+" + WHITE + "] Класс для парсинга: " + Style.RESET_ALL)

print("\033[0m" + "\n" + Style.RESET)

# User Agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36'}

# Получаем целый сайт
r = requests.get(site, headers=headers)

# Парсим наш сайт
html = BeautifulSoup(r.content, "html5lib")
res = html.find_all(class_=pars_class)

# Выводим ее на терминал 
for x in res:
  print(x.text)
