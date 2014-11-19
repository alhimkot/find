#!/usr/bin/env python
# -*- coding:utf-8 -*-

import webbrowser

# ГЛАВНОЕ МЕНЮ
# поисковик будет заменен на duckduckGo, яндекс перенесу в поиск людей.
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
# ПОИСК ЛЮДЕЙ (ближайщие три дня)
def winPeople():
    print("╔---------------------------------------------------------------╗")
    print("║(1) Друзья                                (2)          Новости ║")
    print("║(3) Сообщества                            (4)      Аудиозаписи ║")
    print("║(5) Видеозаписи                           (6)          Маркеры ║") 
    print("║(7) Поиск через поисковик                 (8)            назад ║")
    print("╚---------------------------------------------------------------╝")


    vk=input(" Где искать? Введите: ")


    if vk == "1":
        chel=input(" Кого вы хотите найти?: ") 
        url = "http://vk.com/search?c[name]=1&c[q]="+chel+"&c[section]=people"
        webbrowser.open(url) 
        print("-----------------------------------------------------------------")

	
    elif vk == "2":
        new=input(" Что вас интересует?: ") 
        url = "http://vk.com/search?c[q]="+new+"&c[section]=statuses" 
        webbrowser.open(url) 
        print("-----------------------------------------------------------------")
    
	
    elif vk == "3":
        com=input(" Введите название сообщества?: ") 
        url = "http://vk.com/search?c[q]="+com+"&c[section]=communities" 
        webbrowser.open(url) 
        print("-----------------------------------------------------------------")
    
	
    elif vk == "4":
        aud=input(" Название песни или исполнителя: ") 
        url = "http://vk.com/search?c[q]="+aud+"&c[section]=audio" 
        webbrowser.open(url) 
        print("-----------------------------------------------------------------")
    
	
    elif vk == "5":
        vid=input(" Что будем смотреть?: ") 
        url = "http://vk.com/search?c[q]="+vid+"&c[section]=video" 
        webbrowser.open(url) 
        print("-----------------------------------------------------------------")
    
	
    elif vk == "6":
        mar=input(" Что вас интересует?: ") 
        url = "http://vk.com/feed?q=%23"+mar+"&section=search" 
        webbrowser.open(url) 
        print("-----------------------------------------------------------------")
# ПОИСК РЕШЕНИЙ (ближайшая неделя)

while True: main()
