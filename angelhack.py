import os
from gtts import gTTS
from playsound import playsound
from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import pyautogui
import time

def text_to_speech():
	messsage = input("Enter the text you want to convert: ")
	speech = gTTS(messsage)
	speech.save('angel.mp3')
	playsound('angel.mp3')
	os.remove('angel.mp3')

def youtubeDownloader(): 
	link = input("Enter the url of the video: ")    
	url =YouTube(str(link))
	video = url.streams.first()
	video.download()

def getweather():
	city = input("Enter City Name: ")
	search = 'weather in ' + city 
	url = f'https://www.google.com/search?&q={search}'
	r = requests.get(url)
	s = BeautifulSoup(r.text,"html.parser")
	update = s.find("div",class_="BNeawe").text
	print(update)
def screenshot():
	choice = input("Do you want custom options? (y/n): ")
	if choice.lower() == 'y':
		file_name = input("Enter a file name: ")
		file_ext = input("Enter a file extension: ")
		delay = int(input("Enter time delay(seconds): "))
		name = f'{file_name}.{file_ext}'
		time.sleep(delay)
	elif choice.lower() == 'n':
		name = int(round(time.time() * 1000))
		name = f'{name}.png'
	else:
		print("Invalid Input")
	img = pyautogui.screenshot(name)
	img.show()



def bmicalclate():
	weight = float(input("Enter your weight in kilograms: "))
	height = float(input("Enter your height in meters: "))
	h = (height * height)

	bmi = weight / h
	if bmi > 18.5 and bmi < 24.9:
		print("You are healthy ")
	elif bmi >= 25:
		print("You are overweight")
	elif bmi < 18.5:
		print("You are underweight")

choice = int(input("Hello I am an angel and i can help you with multiple things. \n Choose from below options \n 1.Convert Text to Speech \n 2.Download Youtube videos \n 3.Get Weather details \n 4.Take a scrrenshot \n 5.Calculate you bmi \n"))

if choice == 1:
	text_to_speech()
elif choice == 2:
	youtubeDownloader()
elif choice == 3:
	getweather()
elif choice == 4:
	screenshot()
elif choice == 5:
	bmicalclate()
else:
	print("Invalid input")