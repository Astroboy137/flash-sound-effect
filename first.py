import wave
import pyaudio
import usb.core
dev1 = str(usb.core.find(idVendor=0x13fe, idProduct=0x4300))
dev2 = str(usb.core.find(idVendor=0x13fe, idProduct=0x4300))
CHUNK = 1024

while True:
    if dev2!=dev1 and dev2!="None" and dev1!="None":
        print("not none")
        with wave.open("C:/Users/User/Downloads/button3.wav", 'rb') as wf:
                    p = pyaudio.PyAudio()
                    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                    channels=wf.getnchannels(),
                                    rate=wf.getframerate(),
                                    output=True)

                    while len(data := wf.readframes(CHUNK)): 
                        stream.write(data)

                    stream.close()

                    p.terminate()

    dev2 = str(usb.core.find(idVendor=0x13fe, idProduct=0x4300))
    if dev2!=dev1:
        print("not none")
        with wave.open("C:/Users/User/Downloads/button3.wav", 'rb') as wf:
                    p = pyaudio.PyAudio()
                    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                    channels=wf.getnchannels(),
                                    rate=wf.getframerate(),
                                    output=True)

                    while len(data := wf.readframes(CHUNK)): 
                        stream.write(data)

                    stream.close()

                    p.terminate()
    dev1 = str(usb.core.find(idVendor=0x13fe, idProduct=0x4300))
    x=0
"""
просто-так сделал прогрумму которая будет проигрывать звут из хал-лайф когда вствляется флешка

мне 16 лет, скоро лето, за первый курс нашел друзей
недавно начал изучать математику, родители здоровы, продолжается война на украине, о ковиде новостей практически нет
узнал для себя много различных музыкальных жанров: рок,бреакоре, элетро свинг,эелектро

"""
