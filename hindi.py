from gtts import gTTS
hindi = ['कृपया ध्यान दीजिए','से चलकर','के रस्ते','को जाने बाली गाड़ी संख्या','कुछ ही समय में प्लेटफार्म संख्या','पर आ रही है']
num = []
temp = 0
for n in range(2, 14): 
    if n % 2 == 0:
        num.append(n)
for i in hindi:
    var = str(num[temp]) + '_hindi'
    language = 'hi'
    myobj = gTTS(text = i, lang = language, slow = False)
    myobj.save(var + '.mp3')
    temp = temp+1
print('Voice is Generated Succesfully')  