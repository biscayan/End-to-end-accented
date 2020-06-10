import os

def rename(folder,name):
    i=1
    for filename in os.listdir(folder):
        os.rename(folder+filename,folder+str(name)+str(i)+'.wav')
        i+=1

rename('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/Australia/','Australia')
rename('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/Canada/','Canada')
rename('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/England/','England')
rename('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/India/','India')
rename('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/US/','US')