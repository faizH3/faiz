# newbie
#education
#python v3 in this android

import android

print ('===============================')
print ('   this is program speak.py')
print ('===============================')

droid = android.Android()
text = droid.dialogGetInput('TTS', 'your input text: ').result
droid.ttsSpeak(text)
