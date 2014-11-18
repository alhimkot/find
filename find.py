#!/usr/bin/env python
# -*- coding:utf-8 -*-

import webbrowser

# ГЛАВНОЕ МЕНЮ
def main():
	print("1 Find 2 People 3 Info")
	kay4main = input("kay: ")
	if kay4main == "1":
		winFind()
	elif kay4main == "2":
		winPeople()
	elif kay4main == "3":
		winInfo()
	elif kay4main not in (1, 2, 3):
		main()

# ПОИСК ИНФОРМАЦИИ
def winFind():
	site2find = input("site: ")
	antislovo2find = input("antislovo: ")
	slovo2find = input("slovo: ")
	if site2find not in (""):
		if antislovo2find not in (""):
			if slovo2find not in (""):
				url = "http://yandex.ru/yandsearch?text=" + slovo2find + " ~~" + antislovo2find + "&safety=0&site=" + site2find
				webbrowser.open(url)
			else:
				winFind()
		else:
			url = "http://yandex.ru/yandsearch?text=" + slovo2find + "&safety=0&site=" + site2find
			webbrowser.open(url)
	else:
		if antislovo2find not in (""):
			if slovo2find not in (""):
				url = "http://yandex.ru/yandsearch?text=" + slovo2find + " ~~" + antislovo2find
				webbrowser.open(url)
			else:
				winFind()
		else:
			url = "http://yandex.ru/yandsearch?text=" + slovo2find
			webbrowser.open(url)
# ПОИСК ЛЮДЕЙ (ближайщая три дня)
# ПОИСК РЕШЕНИЙ (ближайшая неделя)

while True: main()
