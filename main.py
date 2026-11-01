from urllib.parse import urlparse
import yt_dlp
print("--------Youtube Downloader By Yuvraj--------")
print("1.Download Video")
print("2.Download Audio")
print("3.Exit")

video_quality={    #video quality selection
    1:"144p",
    2:"240p",
    3:"360p",
    4:"480p",
    5:"720p",
    6:"1080p",
    7:"Best quality"
    }
audio_quality={    #audio quality selection

    1:"64kbps",
    2:"96kbps",
    3:"128kbps",
    4:"192kbps",
    5:"256kbps",
    6:"320kbps"}
try:
    n=int(input("Choose Option : "))

    if n == 1:
        print("1.144p")     #cli of video qulity
        print("2.240p")
        print("3.360p")   
        print("4.480p")
        print("5.720p (HD)")
        print("6.1080p (Full HD)")
        print("7.Best quality")
        
        print("----Video Quality----")
        vid_qlt=int(input("Enter Video Quality : "))
        if vid_qlt > 7 or vid_qlt < 1:
            print("Invalid video quality!")
        else:
            select_video_quality=video_quality[vid_qlt]
            print("Video quality selecter successfully!")
            print("You select video ",select_video_quality)
            if select_video_quality == "Best quality":
                format_selector="bestvideo+bestaudio"
            else:
                height=select_video_quality.replace("p","")
                format_selector=f"bestvideo[height<={height}]+bestaudio"

            options={
                "format":format_selector,
                "noplaylist":True
            }
            url=input("Enter video URL :")
            parsed_url=urlparse(url)
            domain=parsed_url.hostname
            allowed_domain=("youtube.com","www.youtube.com","youtu.be")
            if domain in allowed_domain:
                print("Valid URL")
                with yt_dlp.YoutubeDL(options) as ydl:
                    ydl.download([url])
            else:
                print("Invailid URL")
            
    elif n == 2:
        print("1.64kbps")
        print("2.96kbps")
        print("3.128kbps")
        print("4.192kbps")
        print("5.256kbps")
        print("6.320kbps")
        print("----Audio Quality----")
        aud_qlt=int(input("Enter Audio Quality : "))        
        if aud_qlt > 6 or aud_qlt < 1:
            print("Invalid audio quality!")
        else:
            select_audio_quality=audio_quality[aud_qlt]
            print("Audio quality selected successfully!")
            print("You select audio",select_audio_quality)
            abr=select_audio_quality.replace("kbps","")
            format_selector=f"bestaudio[abr<={abr}]"
            options={
                "format":format_selector,
                "noplaylist":True
            }

            url=input("Enter audio   URL :")
            parsed_url=urlparse(url)
            domain=parsed_url.hostname
            allowed_domain=("youtube.com","www.youtube.com","youtu.be")
            if domain in allowed_domain:
                print("Valid URL")
                with yt_dlp.YoutubeDL(options) as ydl:
                    ydl.download([url])
                    print("Download successfully!")
            else:
                print("Invailid URL")
    elif n == 3 :
        print("Exiting...")
    else:
        print("Invalid operation!")
except ValueError:
    print("Invalid operation!")

finally:
    print("Thanks For Visiting My YT Downloader! ")
