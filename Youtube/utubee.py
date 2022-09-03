from pytube import YouTube 
  
#where to save 
SAVE_PATH = "./" #to_do 
  
#link of the video to be downloaded 
link=["https://www.youtube.com/watch?v=BOxBcuvASag&list=PLve39GJ2D71yyECswi0lVaBm_gbnDRR9v&index=2", 
    "https://www.youtube.com/watch?v=RHqXEt2T_IQ&list=PLve39GJ2D71yyECswi0lVaBm_gbnDRR9v&index=3",
    "https://www.youtube.com/watch?v=DiZuxLbpkGg&list=PLve39GJ2D71yyECswi0lVaBm_gbnDRR9v&index=4",
    "https://www.youtube.com/watch?v=BUSn3GgR6DU&list=PLve39GJ2D71yyECswi0lVaBm_gbnDRR9v&index=5"
    ]
  
for i in link: 
    try: 
          
        # object creation using YouTube
        # which was imported in the beginning 
        yt = YouTube(i) 
    except: 
          
        #to handle exception 
        print("Connection Error") 
      
    #filters out all the files with "mp4" extension 
    mp4files = yt.filter('mp4') 
  
    # get the video with the extension and
    # resolution passed in the get() function 
    d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
    try: 
        # downloading the video 
        d_video.download(SAVE_PATH) 
    except: 
        print("Some Error!") 
print('Task Completed!') 