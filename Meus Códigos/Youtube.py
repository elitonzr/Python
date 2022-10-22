#python3

#https://pypi.org/project/pafy/
#https://pypi.python.org/pypi/pafy
#http://pythonhosted.org/pafy/
#

import pafy
video = pafy.new('gEpXY2zYZ5k') #'video id or video url'
bestaudio = video.getbestaudio()
bestaudio.bitrate #get bit rate
bestaudio.extension #extension of audio fileurl
...
bestaudio.url #get url
...
#download if you want
bestaudio.download()