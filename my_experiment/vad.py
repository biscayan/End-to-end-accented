from auditok import split

def VAD(folder,new_folder):
    for filename in os.listdir(folder):
        audio_regions = split(folder+'/'+filename)
        for region in audio_regions:
            region.play(progress_bar=True)
            newname = region.save(new_folder+'/'+filename)
            print("region saved as: {}".format(newname))

VAD('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/Australia','C:/Users/HyeongJu/Desktop/End-to-end accented/exp_data/Australia')
VAD('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/Canada','C:/Users/HyeongJu/Desktop/End-to-end accented/exp_data/Canada')
VAD('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/England','C:/Users/HyeongJu/Desktop/End-to-end accented/exp_data/England')
VAD('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/India','C:/Users/HyeongJu/Desktop/End-to-end accented/exp_data/India')
VAD('C:/Users/HyeongJu/Desktop/End-to-end accented/dataset/US','C:/Users/HyeongJu/Desktop/End-to-end accented/exp_data/US')