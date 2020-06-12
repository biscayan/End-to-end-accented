import scipy.io.wavfile as wav
import librosa
import os
import numpy as np


def mfcc_extraction(folder):

    num_data=5000
    avg_len=0

    for filename in os.listdir(folder):

        (rate,sig)=wav.read(folder+'/'+filename)
        avg_len+=len(sig)

    avg_len=avg_len//num_data
        
    #print(avg_len)

    mfcc_array=[]
    label_array=[]

    for filename in os.listdir(folder):

        (rate,sig)=wav.read(folder+'/'+filename)
        
        float_sig=np.array(sig,dtype=float)

        fixed_sig = librosa.util.fix_length(float_sig,avg_len)
        fixed_sig = (fixed_sig - np.mean(fixed_sig))/np.std(fixed_sig)
        
        mfcc=librosa.feature.mfcc(y=fixed_sig, sr=rate, n_fft=512, hop_length=256, n_mfcc=13) #32ms #16ms #13d
        #mfcc=librosa.feature.mfcc(y=fixed_sig, sr=rate,n_fft=512, hop_length=256, n_mfcc=39) #39d
        #mfcc=librosa.feature.mfcc(y=fixed_sig, sr=rate,n_fft=512, hop_length=256, n_mfcc=39, htk=True) #32ms #16ms #htk style

        mfcc=mfcc.reshape(mfcc.shape[1],mfcc.shape[0])
        print(filename, mfcc.shape)
        mfcc_array.append(mfcc)

        if folder.endswith("Australia"):
            label=np.zeros((mfcc.shape[0],1),dtype=int)
            label_array.append(label)
        elif folder.endswith("Canada"):
            label=np.ones((mfcc.shape[0],1),dtype=int)
            label_array.append(label)
        elif folder.endswith("England"):
            label=np.ones((mfcc.shape[0],1),dtype=int)*2
            label_array.append(label)
        elif folder.endswith("India"):
            label=np.ones((mfcc.shape[0],1),dtype=int)*3
            label_array.append(label)
        elif folder.endswith("US"):
            label=np.ones((mfcc.shape[0],1),dtype=int)*4
            label_array.append(label)

    mfcc_array=np.array(mfcc_array)
    mfcc_array=mfcc_array.reshape(mfcc_array.shape[1]*num_data,mfcc_array.shape[2])
    print("mfcc shape:",mfcc_array.shape)

    label_array=np.array(label_array)
    label_array=label_array.reshape(label_array.shape[1]*num_data,label_array.shape[2])
    print("label shape:",label_array.shape)
    
    result=np.hstack((mfcc_array,label_array))
    print("total shape:",result.shape)

    mfcc_folder='C:/Users/HyeongJu/Desktop/End-to-end accented/mfcc'

    if folder.endswith("Australia"):
        with open(mfcc_folder+'/'+"Australia_mfcc.csv", 'w') as Australia_csv:
            np.savetxt(Australia_csv, result, delimiter=",")
    elif folder.endswith("Canada"):
        with open(mfcc_folder+'/'+"Canada_mfcc.csv", 'w') as Canada_csv:
            np.savetxt(Canada_csv, result, delimiter=",")
    elif folder.endswith("England"):
        with open(mfcc_folder+'/'+"England_mfcc.csv", 'w') as England_csv:
            np.savetxt(England_csv, result, delimiter=",")
    elif folder.endswith("India"):
        with open(mfcc_folder+'/'+"India_mfcc.csv", 'w') as India_csv:
            np.savetxt(India_csv, result, delimiter=",")
    elif folder.endswith("US"):
        with open(mfcc_folder+'/'+"US_mfcc.csv", 'w') as US_csv:
            np.savetxt(US_csv, result, delimiter=",")


#mfcc_extraction('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/Australia') #(244,13)
#mfcc_extraction('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/Canada') #(256,13)
#mfcc_extraction('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/England') #(230,13)
#mfcc_extraction('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/India') #(245,13)
#mfcc_extraction('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/US') #(243,13)


