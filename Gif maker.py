from moviepy.editor import  *

(a,b)=map(int,input("Start:").split())
(c,d)=map(int,input("End:").split())
clip=(VideoFileClip("Sia - Cheap Thrills ft. Sean Paul (Sehck Remix)-G_JtNhTzg5s.MP4").subclip((a,b),(c,d)).speedx(0.3).resize(0.5))
#snapshot=(clip.crop(x2=593).to_ImageClip(0.2).set_duration(clip.duration))
composition=CompositeVideoClip([clip])
#clip=clip.crop(x1=115,x2=250)

composition.write_gif("Sia.gif")