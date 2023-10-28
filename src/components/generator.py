import g4f
from g4f.Provider import ChatgptAi
import regex as re

#generation function
def generate(prompt):
    g4f.debug.logging = False # enable logging
    g4f.check_version = False # Disable automatic version checking

    try:
       response = g4f.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=[{"role": "user", "content": prompt}]
       )

       riddle = re.search("\{(.*?)\}",response)
       answer = response
       return (riddle,answer) 
    except:
        generate(prompt)
