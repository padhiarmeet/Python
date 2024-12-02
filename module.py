import pyjokes

joke = pyjokes.get_joke()
# print("Printing a joke.....")
"""
so...this is how U can comment for multiple lines.....
"""
print(joke)
print('''
      helo....
      how are you ...
      by..by..''')

import pyttsx3
engine = pyttsx3.init()
engine.say('''He maadi rumjhum karti aavi
        He maadi rumjhum karti aavi
        Aanand utsav ne garba
        ni ramjhat saathe laavi
        He maadi rumjhum karti aavi
        He maadi rumjhum karti aavi
        Jhaanjhar ne jhankare maadi
        sakhiyo saathe laavi

        Moti Verana chawk ma aavya ambe maa
        Chawk ma jagmug thaay re aavya ambe maa
        Moti Verana chawk ma aavya ambe maa
        Chawk ma jagmug thaay re aavya ambe maa
        Udao laal gulaal k aavya ambe maa
        Chawk ma jagmug thaay re aavya ambe maa''')
engine.runAndWait()