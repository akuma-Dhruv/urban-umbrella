import requests
import wget



print ('in main')
access_key = YOU ACCESS KEY HERE
url='https://api.unsplash.com/photos/random?client_id=' + access_key
params = {
            'query': 'HD wallpapers',
            'orientation': 'landscape'
            }

response = requests.get(url, params=params).json()
image_source = response['urls']['full']
image = wget.download(image_source, 'M:/z/walpaper.jpg')
#print(response.status_code)

'''ABOVE CODE WILL GET A WALLPAPER FROM UNSPLASH.COM AND WILL SAVE IT!!
'''
