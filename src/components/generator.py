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
       provider=g4f.Provider.ChatgptAi,
       messages=[{"role": "user", "content": prompt}],
       stream=g4f.Provider.ChatgptAi.supports_stream,
       )

       fulltext = "".join([i for i in response])

       riddle = re.search("\{(\w+)\}", fulltext)
       answer = re.search("\((\w+)\)", fulltext)
       return (riddle,answer) 
    except:
        generate(prompt)
