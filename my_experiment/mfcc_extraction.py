import scipy.io.wavfile as wav
import librosa
import os
import numpy as np


def mfcc_extraction(folder):

    for filename in os.listdir(folder):

        (rate,sig)=wav.read(folder+'/'+filename)

    label_array=[]
    mfcc_array=np.empty((0,13), float)
    
    for filename in os.listdir(folder):

        (rate,sig)=wav.read(folder+'/'+filename)
        
        float_sig=np.array(sig,dtype=float)

        mfcc=librosa.feature.mfcc(y=float_sig, sr=rate, n_fft=512, hop_length=256, n_mfcc=13) #32ms #16ms #13d
        #mfcc=librosa.feature.mfcc(y=fixed_sig, sr=rate,n_fft=512, hop_length=256, n_mfcc=39) #39d
        #mfcc=librosa.feature.mfcc(y=fixed_sig, sr=rate,n_fft=512, hop_length=256, n_mfcc=39, htk=True) #32ms #16ms #htk style

        mfcc=mfcc.reshape(mfcc.shape[1],mfcc.shape[0])

        #print(filename,mfcc.shape)
 
        mfcc_array=np.concatenate((mfcc_array,mfcc),axis=0)

    if folder.endswith("Australia"):
        label_array=np.zeros((mfcc_array.shape[0],1),dtype=int)
    elif folder.endswith("Canada"):
        label_array=np.ones((mfcc_array.shape[0],1),dtype=int)
    elif folder.endswith("England"):
        label_array=np.ones((mfcc_array.shape[0],1),dtype=int)*2
    elif folder.endswith("India"):
        label_array=np.ones((mfcc_array.shape[0],1),dtype=int)*3
    elif folder.endswith("US"):
        label_array=np.ones((mfcc_array.shape[0],1),dtype=int)*4

    print("mfcc shape:",mfcc_array.shape)
    print("label shape:",label_array.shape)
    
    result=np.hstack((mfcc_array,label_array))
    print("total shape:",result.shape)
    
    mfcc_folder='C:/Users/HyeongJu/Desktop/End-to-end accented/mfcc2'
    
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

if __name__=='__main__':
    mfcc_extraction('C:/Users/HyeongJu/Desktop/End-to-end accented/exp dataset/Australia') #(2701901, 14)
    mfcc_extraction('C:/Users/HyeongJu/Desktop/End-to-end accented/exp dataset/Canada') #(2751667, 14)
    mfcc_extraction('C:/Users/HyeongJu/Desktop/End-to-end accented/exp dataset/England') #(2586217, 14)
    mfcc_extraction('C:/Users/HyeongJu/Desktop/End-to-end accented/exp dataset/India') #(2825064, 14)
    mfcc_extraction('C:/Users/HyeongJu/Desktop/End-to-end accented/exp dataset/US') #(2392742, 14)



