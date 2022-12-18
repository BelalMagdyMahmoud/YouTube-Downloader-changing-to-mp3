import os,sys
from pytube import YouTube, Playlist
SAVE_PATH = {"Videos": "D:/YouTube" , "Playlist":"D:/YouTubePlayList"}
SAVE_PATHVideos = "D:/YouTube" 

#link of the video to be downloaded
links= [ "https://www.youtube.com/playlist?list=PLATlJNRzYr-A2AUsntjR_iWDl-nIylPnP","https://www.youtube.com/playlist?list=PLATlJNRzYr-B25vGJ27SX77a8RIlgy1xJ"]

def LetsDownload(SAVE_PATH):

	# object creation using YouTube which was imported in the beginning
	yt = YouTube(link)
	d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
	outfileName = d_video.download(SAVE_PATH)
	titleName = yt.title
	return outfileName, titleName
n=0

for link in links:

	if "playlist" in link:

		playlist = Playlist(link)
		PlaylistPath= SAVE_PATH["Playlist"]
		
		PlayListLinks = playlist.video_urls
		N = len(PlayListLinks)

		print(f'This link found to be a Playlist "{playlist.title}" with number of videos equal to {N} ')
		print(f"\n Lets Download all {N} videos")

		for i,link in enumerate(PlayListLinks):

			outfileName, titleName = LetsDownload("D:/"+ playlist.title)

			print(i+1, '.', titleName,' has been Downloaded.')

	else:
		VideosPath= SAVE_PATH["Videos"]

		print("This link found to be a Video Link")

		outfileName, titleName = LetsDownload(SAVE_PATH["Videos"])
		n=n+1
		print(n, '.', titleName, '  Video has been Downloaded.')

# change the extension from mp4 to mp3
folder = "D:/"+ playlist.title

for filename in os.listdir(folder):
           infilename = os.path.join(folder,filename)
           newname = infilename.replace('.mp4', '.mp3')
           output = os.rename(infilename, newname)

           print ("File : "+filename+" has been changed")
