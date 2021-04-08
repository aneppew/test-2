#coding: utf-8

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Style
import os, sys, time, traceback, pickle, random, colorama

def clear():
    
    os.system("cls" if os.name == "nt" else "echo -e \\\\033c")
    os.system("mode con: cols=105 lines=30")
    

def logo():
    try:
        text = """                                   
                         ▄▄▄▄▄▄▪  ▄ •▄▄▄▄▄▄▄      ▄ •▄    ▄▄▄▄·      ▄▄▄▄▄▄      
                          •██  ██ █▌▄▌▪•██  ▪     █▌▄▌▪   ▐█ ▀█▪▪     •██        
                           ▐█.▪▐█·▐▀▀▄· ▐█.▪ ▄█▀▄ ▐▀▀▄·   ▐█▀▀█▄ ▄█▀▄  ▐█.▪     
                           ▐█▌·▐█▌▐█.█▌ ▐█▌·▐█▌.▐▌▐█.█▌   ██▄▪▐█▐█▌.▐▌ ▐█▌· 
                           ▄██ ▄██·█  █ ▄██  ▀█▄▀▪·█ ▀█▄  ·▀███▀ ▀█▄▀▪ ▄██  \n                    
        """
        bad_colors = ['LIGHTCYAN_EX', 'CYAN']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in text]
        print(''.join(colored_chars))
        print(Fore.RESET + "\t\t\t          Follow Me on Youtube: Dr. Teilaw\n")

    except KeyboardInterrupt:
        sys.exit()

clear()
logo()

maxi = 0
start = '/@'
end = '/video/'
views = ' '

boosted_link = input('{}\n[>] {}TikTok Video Link ?: {}'.format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
print('  ')
username = boosted_link[boosted_link.find(start)+len(start):boosted_link.rfind(end)]
options = webdriver.ChromeOptions()
options.add_argument('window-size=1000,900')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
browser.minimize_window()
wait = WebDriverWait(browser, 2)

from selenium import webdriver

init()
os.system('title ' + ' TikTok Booster made by Teilaw#0001 - Boost: @{}'.format(username))

def countdown():
	while True:
		time.sleep(5)
		try:
			browser.find_element_by_xpath('//*[@id="show_tviews"]/div/div/div/form/div/div/button').click()
			wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="get_views"]/div/div[1]/div/form/button')))
			break
		except:
			continue
			pass
def run():
	global views
	global username
	try:
		browser.find_element_by_xpath('//*[@id="show_tviews"]/div/div/div/form/div/div/button').click() #Search link
		try:
			views = browser.find_element_by_xpath('//*[@id="get_views"]/div/div[1]/div/form/div').text #Show views
			time.sleep(1)
		except:
			pass
		time.sleep(5)
		while True:
			try:
				wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="get_views"]/div/div[1]/div/form/button')))
				break
			except:
				continue
				pass
		browser.find_element_by_xpath('//*[@id="get_views"]/div/div[1]/div/form/button').click() #Send Views
		print('  ')
		print('{}[>]{}Views Sent{}'.format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
		os.system('title ' + ' TikTok Booster by Teilaw#0001 ~ Boost: @{} - Views: {}'.format(username, views))
		time.sleep(5)
		countdown()
		run()
	except:
		print('  ')
		run()

def paste_link():
	global boosted_link
	try:
		browser.find_element_by_xpath('//*[@id="show_tviews"]/div/div/div/form/div/input').send_keys(boosted_link) #Link where is paste
		time.sleep(1)
		wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="show_tviews"]/div/div/div/form/div/div/button'))) #Search link
		print('  ')
		print("{}[>] {}Pasted link...{}".format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
		run()
	except:
		print("{}[>] {}Error, Cannot find Element{}".format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
		input()


def maximize():
	global maxi
	maxi += 1
	if maxi == 1:
		print('  ')
		print('{}[>] {}Please do the Captcha to continue.{}'.format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
		browser.maximize_window()
	elif maxi >= 1:
		pass
	else:
		pass

def start():
	try:
		browser.get("https://vipto.de/")
		time.sleep(2)
		while True:
			try:
				wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div/h2/span')))
				print('  ')
				print('{}\n[X] {}Please Disable Adblock.{}'.format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
				continue
			except:
				pass
				break
		while True:
			try:
				maximize()
				wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/form/div/input[1]')))
				continue
			except:
				pass
				browser.minimize_window()
				break
	except:
		try:
			wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/ul/li/a')))
			print('  ')
			print("{}[>] {}The Page didn't load.{}".format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
			input()
		except:
			pass
	print('  ')
	print('{}[>] {}Captcha OK.{}'.format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
	time.sleep(1)
	try:
		browser.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/button').click()
		time.sleep(1)
	except:
		print('  ')
		print("{}[>] {}Error, Cannot find Element{}".format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
		pass
	clear()
	logo()
	print('{}[>] {}Starting...{}'.format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
	paste_link()

start()