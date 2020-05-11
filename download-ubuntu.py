# This program will download the ubuntu 20.04 iso file
try:
    import wget
except:
    import os
    os.system("python3 -m pip install wget")
    import wget

# https://releases.ubuntu.com/20.04/ubuntu-20.04-desktop-amd64.iso?_ga=2.243191300.728293399.1589169307-865266594.1589169307
print('Begin downloading ubuntu 20.04 desktop iso file')

url = 'https://releases.ubuntu.com/20.04/ubuntu-20.04-desktop-amd64.iso?_ga=2.250071680.728293399.1589169307-865266594.1589169307'
wget.download(url, 'ubuntu-20.04-desktop-amd64.iso')


print("Begin donwloading ubuntu 20.04 server iso file")
url2 = 'https://releases.ubuntu.com/20.04/ubuntu-20.04-live-server-amd64.iso?_ga=2.42847907.728293399.1589169307-865266594.1589169307'
wget.download(url2, 'ubuntu-20.04-live-server-amd64.iso')
