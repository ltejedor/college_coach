#              .';:cc;.
#            .,',;lol::c.
#            ;';lddddlclo
#            lcloxxoddodxdool:,.
#            cxdddxdodxdkOkkkkkkkd:.
#          .ldxkkOOOOkkOO000Okkxkkkkx:.
#        .lddxkkOkOOO0OOO0000Okxxxxkkkk:
#       'ooddkkkxxkO0000KK00Okxdoodxkkkko
#      .ooodxkkxxxOO000kkkO0KOxolooxkkxxkl
#      lolodxkkxxkOx,.      .lkdolodkkxxxO.
#      doloodxkkkOk           ....   .,cxO;
#      ddoodddxkkkk:         ,oxxxkOdc'..o'
#      :kdddxxxxd,  ,lolccldxxxkkOOOkkkko,
#       lOkxkkk;  :xkkkkkkkkOOO000OOkkOOk.
#        ;00Ok' 'O000OO0000000000OOOO0Od.
#         .l0l.;OOO000000OOOOOO000000x,
#            .'OKKKK00000000000000kc.
#               .:ox0KKKKKKK0kdc,.
#                      ...
#
# Author: peppe8o
# Date: Mar 10th, 2023
# Version: 1

# import required modules
import sys, os
from pathlib import Path
import speech_recognition as sr
from subprocess import Popen, DEVNULL, STDOUT

# Temporarily disable the shell printing and recognize speech using Google Speech Recognition
# for testing purposes, we're just using the default API key
# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
# instead of `r.recognize_google(audio)`
def silent_google_recognition(audio_file):
    sys.stdout = open(os.devnull, 'w')
    result = r.recognize_google(audio_file)
    sys.stdout = sys.__stdout__
    return result

# Allows to use bash commands with a simplified line
# remove stderr=STDOUT for debugging ffmpeg actions
def console(cmd):
    p = Popen(cmd, shell=True, stdout=DEVNULL, stderr=STDOUT)
    p.wait()
    #out, err = p.communicate()
    #return out.decode('ascii').strip()

# Converts any file to a .wav file using ffmpeg
def convert_to_wav(file):
    file_name = str(Path(file).resolve())
    file_type = Path(file).suffix
    name=file_name.split(file_type)[0]
    output_wav = name + "-converted.wav"
    console("ffmpeg -i " + file + " -b:a 192k " + output_wav)
    return output_wav

# Main program
input_file = sys.argv[1]
file_type = Path(input_file).suffix
if file_type != ".wav": input_file = convert_to_wav(input_file)

r = sr.Recognizer()
with sr.AudioFile(input_file) as source:
     audio = r.record(source)

try:
    print("Google Speech Recognition thinks you said:\n\n" + silent_google_recognition(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))