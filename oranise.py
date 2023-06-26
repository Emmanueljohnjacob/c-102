import os,shutil
fromdir="C:/Users/Manu/Downloads"
todir="C:/Users/Manu/Desktop"
listoffiles=os.listdir(fromdir)
for f in listoffiles:
    name,extension=os.path.splitext(f)
    if extension=="":
        continue
    if extension==".pdf":
        path1=fromdir+'/'+f
        path2=todir+'/'+"notes"
        path3=todir+'/'+"notes"+'/'+ f
        if os.path.exists(path2):
            print("moving ",f)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving ",f)
            shutil.move(path1,path3)