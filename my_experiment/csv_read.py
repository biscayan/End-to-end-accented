import pandas as pd
import csv
import os
import shutil

dev_file=open('dev.csv','r',encoding='UTF8')
invalidated_file=open('invalidated.csv','r',encoding='UTF8')
other_file=open('other.csv','r',encoding='UTF8')
test_file=open('test.csv','r',encoding='UTF8')
train_file=open('train.csv','r',encoding='UTF8')
validated_file=open('validated.csv','r',encoding='UTF8')

accent_list=[]
accent_dict={}

dev_read=csv.reader(dev_file)
dev_header=next(dev_read)
for dev in dev_read:
    if dev[7] is not '':
        accent_list.append(dev[7])
        accent_dict[dev[1]]=dev[7]

invalidated_read=csv.reader(invalidated_file)
invalidated_header=next(invalidated_read)
for invalidated in invalidated_read:
    if invalidated[7] is not '':
        accent_list.append(invalidated[7])
        accent_dict[invalidated[1]]=invalidated[7]

other_read=csv.reader(other_file)
other_header=next(other_read)
for other in other_read:
    if other[7] is not '':
        accent_list.append(other[7])
        accent_dict[other[1]]=other[7]

test_read=csv.reader(test_file)
test_header=next(test_read)
for test in test_read:
    if test[7] is not '':
        accent_list.append(test[7])
        accent_dict[test[1]]=test[7]

train_read=csv.reader(train_file)
train_header=next(train_read)
for train in train_read:
    if train[7] is not '':
        accent_list.append(train[7])
        accent_dict[train[1]]=train[7]

validated_read=csv.reader(validated_file)
validated_header=next(validated_read)
for validated in validated_read:
    if validated[7] is not '':
        accent_list.append(validated[7])
        accent_dict[validated[1]]=validated[7]

def make_dir():
    accent_list2=list(set(accent_list))
    for accent in accent_list2:
        os.makedirs('C:/Users/HyeongJu/Desktop/SLP/corpus/Common Voice/en/data/{}'.format(accent))

make_dir()

original_path = "C:/Users/HyeongJu/Desktop/SLP/corpus/Common Voice/en/clips"
file_list = os.listdir(original_path)
goal_path = 'C:/Users/HyeongJu/Desktop/SLP/corpus/Common Voice/en/data'

def file_move():
    for accent_file_name in accent_dict:
        for file_name in file_list:
            if file_name == accent_file_name:
                shutil.move(original_path+'/'+accent_file_name,goal_path+'/'+accent_dict[accent_file_name]+'/'+accent_file_name)

file_move()
            


        


dev_file.close()
invalidated_file.close()
other_file.close()
test_file.close()
train_file.close()
validated_file.close()
