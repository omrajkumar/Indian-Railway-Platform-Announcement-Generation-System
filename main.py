import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

# pip3 install pyaudio
# pip3 install pydub
# pip3 install pandas
# pip3 install gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi-in'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    

# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from-city
        textToSpeech(item['from'], '3_hindi.mp3')

        # 4 - Generate via-city
        textToSpeech(item['via'], '5_hindi.mp3')

        # 6 - Generate to-city
        textToSpeech(item['to'], '7_hindi.mp3')

        # 8 - Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '9_hindi.mp3')

        # 10 - Generate platform number
        textToSpeech(item['platform'], '11_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,14)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")
        

if __name__ == "__main__":
    print("Generating Skeleton...")
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
    

