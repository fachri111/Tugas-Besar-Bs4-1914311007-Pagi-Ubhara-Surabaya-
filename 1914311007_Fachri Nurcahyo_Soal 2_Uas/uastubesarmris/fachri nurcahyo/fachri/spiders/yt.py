# imported the requests library
import requests
image_url = "https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/famous/manson_believe_me.wav"
 
#URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
 
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("python_logo.png",'wb') as f:
        '''
        Saving recieved content as a png file in binary format
        '''
 
        #write the contents of the response (r.content)
        # to a new file in binary mode.
        f.write(r.content)