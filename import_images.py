from pprint import pprint
import json
import os
import urllib

currDir = os.path.dirname(os.path.abspath(__file__)) + '/'

def importImages():  
	directory = currDir + 'chromecast_images/'
	if not os.path.exists(directory):
		os.makedirs(directory)

	#imageName = directory + "1.jpg"
	#urlStr = "https://lh6.googleusercontent.com/-3LiF-MBl6OE/UO5TXZ724aI/AAAAAAAAE50/JWLqdeEM9QY/s1920-w1920-h1080-c/Colorado%2BRiver%2BSunset.jpg"
	#urllib.urlretrieve(urlStr, imageName)

	bgJSN = currDir + "backgrounds.json"
	jsnFile = "https://raw.githubusercontent.com/dconnolly/chromecast-backgrounds/master/backgrounds.json"
	urllib.urlretrieve(jsnFile, bgJSN)

	with open('backgrounds.json') as json_data:    
		data = json.load(json_data)
        i = 1
        for urlJson in data:
        	pprint('url being retrieved --> ' + urlJson['url'])
        	urlStr = urlJson['url']
        	imageName = directory + str(i) + ".jpg"
        	pprint('image being saved --> ' + imageName)
        	urllib.urlretrieve(urlStr, imageName)
        	i += 1

        json_data.close()


if __name__ == "__main__":
	importImages()

