import os,shutil
fromdir="C:/Users/Manu/Desktop/whjr/C102_assets-main"
todir="C:/Users/Manu/Desktop/whjr/C102_assets-main"
listoffiles=os.listdir(fromdir)
for f in listoffiles:
    name,extension=os.path.splitext(f)
    if extension=="":
        continue
    if extension in['.gif','.png','.jpg','.jpeg','.jfif']:
        path1=fromdir+'/'+f
        path2=todir+'/'+"images"
        path3=todir+'/'+"images"+'/'+ f
        if os.path.exists(path2):
            print("moving ",f)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving ",f)
            shutil.move(path1,path3)