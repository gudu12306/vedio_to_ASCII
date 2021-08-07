from tkinter import *
import tkinter.messagebox
import base64
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import threading
import time
import os
import cv2
import subprocess
from cv2 import VideoWriter,VideoWriter_fourcc,imread,resize
from PIL import Image, ImageFont, ImageDraw ,ImageTk

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:oa+>!:+. ")
root=Tk()
root.title("欢迎关注知乎账号gudu12306")
path1=os.path.dirname(os.path.abspath(__file__))
# print(path1)
os.environ['PATH']+=os.pathsep+path1
# print(os.environ['PATH'])

width=700
height=800
screenwidth=root.winfo_screenwidth()
screenheight=root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/5)
root.geometry(alignstr)
root.resizable(0,0)

img=b'AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAlJSX/KSkp/y0tLf8wMDD/NjY2/0RERP+Dg4P/Pz8//x4eHv8hISH/IiIi/x0dHf8rKyv/Ly8v/4SEhP+jo6P/HBwc/yEhIf8mJib/KCgo/yEhIf9gYWH/PT4+/x4eHv8gICD/RERE/0xMTP8rKyv/ICAg/zExMf+QkJD/qKio/xoaGv8cHBz/HBwc/x4eHv8gICD/LS0t/x8fH/8fHx//LS0t/3l5ef9qamr/SkpK/yQkJP8oKSj/kZGQ/6ysrP8bGxv/HBwc/x0dHf8cHBz/Hx8f/yAgIP8hISH/NTY2/4OFhf+Xl5f/ampq/2JiYv8zNDL/Jycn/5OTk/+wsLD/Gxsb/xwcHP8dHR3/HR0d/x4eHv8hISH/RUVF/6Ghof/BwcH/tLS0/21ubP9FRkX/TU1N/yoqKv+VlZX/s7Oz/xwcHP8dHR3/HR0d/x0dHf8fHx//Pj4+/66urv/CwsL/ycnJ/7Gxsf89PT3/Nzc3/1tbW/89PT3/eXl5/7e3t/8cHBz/HR0d/x8fH/8fHx//JiYm/4qKiv/MzMz/w8PD/8rKyv+mpqb/QEBA/zs7O/9hYWH/VlZW/1tbW/+5ubn/HBwc/x0dHf8eHh7/ICAg/y0uLv/FxcX/1dXV/9XV1f/W1tb/1NTU/7Ozs/+Kior/bGxs/2JiYv9OTk3/t7e3/xwcHP8cHBz/HR0d/x8fH/8jJCT/ampp/8rKyv+Xl5b/i4yK/87Ozv/Dw8P/dnZ2/2hoaP9qamr/Q0ND/7e3t/8dHR3/Hh4e/x4eHv8fHx//KSkp/yoqKv9aWlr/dnZ2/4WFhf+np6f/iYmJ/y0tLf9LS0v/Y2Nj/1JSUv+/v7//MzQ0/zExMf8vLy//MzMz/6SkpP86Ojr/Jycn/3Nzc/+3t7b/r6+v/8zMzP9FRUX/MDAw/ysrK/9dXV3/v7+//0hJSf9FRUX/QkND/21ubv9nZ2f/RERE/yIiIv8nJyf/NDQ0/2tra/+en5//Ly8v/yMjI/8qKir/lJSU/729vf9ERUX/QENC/z4/P/9fYGD/V1dX/2lpaf8kJCT/Hx8f/yMjI/8pKSn/LCws/yIiIv8lJSX/Wlpa/66urv+6urr/MzMz/zExMf8uLi7/RkZG/15eXv8yMjL/KSkp/yoqKv8uLi7/KSkp/ycnJ/88Pj3/MjIy/2hoaP+mpqb/sLCw/yEhIf8gICD/Hx8f/x4eHv8dHR3/NjY2/yYmJv8cHBz/Hx8f/ycnJ/8mJib/aWpp/z4+Pv9tbW3/np6e/6Wlpf8vLy//MzQ0/y8vL/80NTX/MDAw/zU1Nf8gICD/Ghoa/xoaGv8aGhr/Kysr/0dHR/9BQUH/a2tr/5WUlf+bm5v/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=='
#设置窗口图标
tmp = open("tmp.ico","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
root.iconbitmap("tmp.ico")
os.remove("tmp.ico")

f=open('bg.txt','r')
imgdata=base64.b64decode(f.read())
tmp=open('bg.jpg','wb+')
tmp.write(imgdata)
f.close()
tmp.close()
canvas_root=tkinter.Canvas(root,width=700,height=800)
image=ImageTk.PhotoImage(Image.open('bg.jpg').resize((700,800),Image.NEAREST))
canvas_root.create_image(350,400,image=image)
canvas_root.pack()

#欢迎关注知乎账号
tip0=Label(root, text='欢迎关注知乎账号gudu12306',font = ('楷体',15),bg='#CCCEC4')
tip0.place(relx=0.03,rely=0.03,anchor=W)

#选择输入视频：
tip1=Label(root, text='请选择输入视频(必填！)：  ',font = ('楷体',25),bg='#CCCEC4',bd=0)
tip1.place(relx=0.1,rely=0.10,anchor=W)
#视频地址输入框
input_vedio_address= Entry(root,bg='#C4C7C5')
input_vedio_address.place(width=420,height=38,relx=0.1,rely=0.159,anchor=W)

#选择保存地址：
tip2=Label(root, text='请选择保存位置(必填！)：  ',font = ('楷体',25),bg='#CCCEC4',bd=0)
tip2.place(relx=0.1,rely=0.24,anchor=W)
#保存地址输入框
input_save_address= Entry(root,bg='#C4C7C5')
input_save_address.place(width=420,height=38,relx=0.1,rely=0.30,anchor=W)

#选择颜色模式
tip3=Label(root, text='请选择颜色模式               ',font = ('楷体',25),bg='#CCCEC4',bd=0)
tip3.place(width=500,relx=0.1,rely=0.385,anchor=W)
v=IntVar()
v.set(1)
radiobutton=Radiobutton(root,text='彩色',font = ('楷体',18),variable=v,value=1,bg='#CCCEC4')
radiobutton.place(relx=0.55,rely=0.385,anchor=W)
radiobutton=Radiobutton(root,text='黑白',font = ('楷体',18),variable=v,value=2,bg='#CCCEC4')
radiobutton.place(relx=0.65,rely=0.385,anchor=W)

#选择缩放比例
s=IntVar()
s.set(100)
scale=Scale(root, from_=0, to_=100, tickinterval=10, orient='horizontal',sliderrelief=RIDGE,bg='#CCCEC4',troughcolor='#D5CDC6',bd=0,resolution=10, variable=s,showvalue=False,length=500,borderwidth=0,label='请选择缩放比例!!!!!!数值越大越接近原视频,耗时更长;1080p(60~80),720p及以下(100)')
scale.place(relx=0.1,rely=0.49,anchor=W)

#为避免在下载时tkinter界面卡死，创建线程函数
def thread_it(func, *args):
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()

#浏览本地文件夹，选择输入视频
def browse_folder1():
    #浏览选择本地文件夹
    save_address = filedialog.askopenfilename()
    #把获得路径，插入保存地址输入框（即插入input_vedio_address输入框）
    input_vedio_address.insert(0,save_address)

#浏览本地文件夹，选择保存位置
def browse_folder2():
    #浏览选择本地文件夹
    save_address = filedialog.askdirectory()
    #把获得路径，插入保存地址输入框（即插入input_save_address输入框）
    input_save_address.insert(0,save_address)

#将像素转换为ascii码
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]

#将txt转换为图片
def txt2image(file_name,color_radio,scale_scale):
    im = Image.open(file_name).convert('RGB')
    im_width=im.width
    im_height=im.height
    im=im.resize((int(im.width/100*scale_scale),int(im.height/100*scale_scale)),Image.NEAREST)
    #gif拆分后的图像，需要转换，否则报错，由于gif分割后保存的是索引颜色
    raw_width = im.width 
    raw_height = im.height
    width = int(raw_width/6)
    height = int(raw_height/15)
    im = im.resize((width,height),Image.NEAREST)

    txt=""
    colors = []
    for i in range(height):
        for j in range(width):
            pixel = im.getpixel((j,i))
            if(color_radio==1):
                colors.append((pixel[0],pixel[1],pixel[2]))
            else:
                colors.append((0,0,0))
            if(len(pixel) == 4):
                txt += get_char(pixel[0],pixel[1],pixel[2],pixel[3])
            else:
                txt += get_char(pixel[0],pixel[1],pixel[2])  
        txt += '\n' 
        colors.append((255,255,255))

    im_txt = Image.new("RGB",(raw_width,raw_height),(255,255,255))
    dr = ImageDraw.Draw(im_txt)
    # font = ImageFont.truetype(os.path.join("fonts","timesbi.ttf"),12)
    font=ImageFont.load_default().font

    x=y=0
    #获取字体的宽高
    font_w,font_h=font.getsize(txt[1])
    font_h *= 1.37 #调整后更佳
    #ImageDraw为每个ascii码进行上色
    for i in range(len(txt)):
        if(txt[i]=='\n'):
            x+=font_h
            y=-font_w
        dr.text((y,x),txt[i], fill = colors[i])
        y+=font_w

    name = file_name
    stext.insert(END,name+' changed\n')
    stext.see(END)
    im_txt=im_txt.resize((im_width,im_height),Image.NEAREST)
    im_txt.save(name)

#将视频拆分成图片
def video2txt_jpg(file_name,color_radio,scale_scale):
    vc = cv2.VideoCapture(file_name)
    c=1
    if vc.isOpened():
        r,frame = vc.read()
        if not os.path.exists('Cache'):
            os.mkdir('Cache')
        os.chdir('Cache')
    else:
        r = False
    while r:
        cv2.imwrite(str(c)+'.jpg',frame)
        txt2image(str(c)+'.jpg',color_radio,scale_scale)#同时转换为ascii图
        r,frame = vc.read()
        c += 1
    os.chdir('..')
    return vc

#将图片合成视频
def jpg2video(outfile_name,fps):
    fourcc = VideoWriter_fourcc(*"MJPG")

    images = os.listdir('Cache')
    im = Image.open('Cache/'+images[0])
    if(os.path.exists(outfile_name+'avi')):
        os.remove(outfile_name+'avi')
    vw = cv2.VideoWriter(outfile_name+'.avi',fourcc,fps,im.size)

    os.chdir('Cache')
    for image in range(len(images)):
        #Image.open(str(image)+'.jpg').convert("RGB").save(str(image)+'.jpg')
        frame = cv2.imread(str(image+1)+'.jpg')
        vw.write(frame)
        stext.insert(END,str(image+1)+'.jpg'+' finished\n')
        stext.see(END)
    os.chdir('..')
    vw.release()   

#递归删除目录
def remove_dir(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            dirs = os.listdir(path)
            for d in dirs:
                if os.path.isdir(path+'/'+d):
                    remove_dir(path+'/'+d)
                elif os.path.isfile(path+'/'+d):
                    os.remove(path+'/'+d)
            os.rmdir(path)
            return
        elif os.path.isfile(path):
            os.remove(path)
        return

#调用ffmpeg获取mp3音频文件
def video2mp3(file_name):
    outfile_name = file_name.split('.')[-2]+'.mp3'
    if(os.path.exists(outfile_name)):
        os.remove(outfile_name)
    p = subprocess.Popen('ffmpeg -i '+file_name+' -f mp3 '+outfile_name,shell=True)
    while p.poll() is None:
        stext.insert(END,'正在提取音频......\n')
        stext.see(END)
        time.sleep(2)
    if p.poll()==0:
        stext.insert(END,'提取音频成功！\n')
        stext.see(END)
    else:
        stext.insert(END,'提取音频失败！\n')
        stext.see(END)
        tkinter.messagebox.showerror(title='Fail', message='转换失败！请查找原因并重试！')

#合成音频和视频文件
def video_add_mp3(file_name,mp3_file,OUTPUT):
    outfile_name = OUTPUT+'/'+file_name.split('.')[-2].split('/')[-1]+'-txt.mp4'
    if(os.path.exists(outfile_name)):
        os.remove(outfile_name)
    p = subprocess.Popen('ffmpeg -i '+file_name+' -i '+mp3_file+' -strict -2 -f mp4 '+outfile_name,shell=True)
    while p.poll() is None:
        stext.insert(END,'正在合成音频......\n')
        stext.see(END)
        time.sleep(2)
    if p.poll()==0:
        stext.insert(END,'合成音频成功！\n')
        stext.see(END)
    else:
        stext.insert(END,'合成音频失败！\n')
        stext.see(END)
        tkinter.messagebox.showerror(title='Fail', message='转换失败！请查找原因并重试！')
    if os.path.exists(outfile_name):
        tkinter.messagebox.showinfo(title='Success', message='转换完成！请退出程序！！！')
    else:
        tkinter.messagebox.showerror(title='Fail', message='转换失败！请查找原因并重试！')

def run():
    INPUT=input_vedio_address.get()
    OUTPUT=input_save_address.get()
    color_radio=v.get()
    scale_scale=s.get()
    print(color_radio)

    vc = video2txt_jpg(INPUT,color_radio,scale_scale)
    FPS = vc.get(cv2.CAP_PROP_FPS)#获取帧率
    vc.release()

    jpg2video(INPUT.split('.')[-2],FPS)
    stext.insert(END,INPUT.split('.')[-2]+'.mp3\n')
    video2mp3(INPUT)
    video_add_mp3(INPUT.split('.')[-2]+'.avi',INPUT.split('.')[-2]+'.mp3',OUTPUT)

    remove_dir("Cache")
    os.remove(INPUT.split('.')[-2]+'.mp3')
    os.remove(INPUT.split('.')[-2]+'.avi')


# “浏览文件夹”按钮
browse_folder_button = Button(root, text='浏览',font = ('楷体',15),bg="#C4C7C5",command=lambda :thread_it(browse_folder1))
browse_folder_button.place(relx=0.73,rely=0.159,anchor="w")

# “浏览文件夹”按钮
browse_folder_button = Button(root, text='浏览',font = ('楷体',15),bg='#C4C7C5',command=lambda :thread_it(browse_folder2))
browse_folder_button.place(relx=0.73,rely=0.30,anchor="w")

# “开始转换”按钮
browse_folder_button = Button(root, text='开始转换',font = ('楷体',15),bg='#C4C7C5',command=lambda :thread_it(run))
browse_folder_button.place(width=100,height=40,relx=0.75,rely=0.71,anchor="nw")

# ScrolledText组件（滚动文本框）
stext = ScrolledText(root, width=65, height=23, bg='#C4C7C5')
stext.place(width=420,height=300,relx=0.1,rely=0.58,anchor="nw")

root.mainloop()
