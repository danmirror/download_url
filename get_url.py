import webbrowser

url = input("enter your youtube url: ")
#1 way
custom_url = 'https://en.savefrom.net/17/'+url

#2 way
url = url[:8]+'ss'+url[8:] 
#exp
#12345678
#htt ps :// youtu.be/Zo5y5wcQjVU

#open
webbrowser.open(url)