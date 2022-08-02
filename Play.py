# import pstats
# from PyQt5 import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# import sys

# from PyQt5 import QtWidgets

# import pafy, vlc
# import threading

# class Play(threading.Thread):
#     def __init__(self,ui):

#         self.ui=ui
#         #self.url = url

#        # self.run()

#         threading.Thread.__init__(self)
    
#     # 영상 재생 
#     def run(self):
#         url = "https://youtu.be/_7h1-9I61vk" # 일단 확인 
#         video = pafy.new(url)
#         best = video.getbest()
#         playurl = best.url
#         Instance = vlc.Instance()
#         self.player = Instance.media_player_new()
#         Media = Instance.Media_new(playurl)
#         Media.get_mrl()
#         self.player.set_media(Media)
#         self.player.play()


#     # 재생, 일시정지, 정지 구현 
#     def playControl(self,num):
#         if num == 0:
#             if self.player.is_playing() == False:
#                 self.player.play()
#                 print("재생")

#         elif num == 1:
#             if self.player.is_playing() == False:
#                 self.player.pause()
#                 print("일시정지")

#         elif num == 2:
#             self.player.stop()
#             print("정지")

#         else:
#             pass
