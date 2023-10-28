import g4f
import regex as re
import pandas as pd

#generation function
def generate(prompt):
    g4f.debug.logging = False # enable logging
    g4f.check_version = False # Disable automatic version checking

    try: 
       response = g4f.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=[{"role": "user", "content": prompt}]
       )

       riddle = response
       return riddle
    except:
        generate(prompt)
