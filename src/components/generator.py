import g4f
from g4f.Provider import ChatBase as prov
import regex as re

#generation function
def generate(prompt):
    g4f.debug.logging = False # enable logging
    g4f.check_version = False # Disable automatic version checking

    try:
       response = g4f.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=[{"role": "user", "content": prompt}],
       stream=False,
       )
       riddle = re.search("\{(\w+)\}",response).groups()[0]
       answer = re.search("\((\w+)\)",response).groups()[0]
       return (riddle,answer) 
    except:
        generate(prompt)

    #if any((match := extr.match(x)) for x in response):
     #  if (match.group(0) == "None"):
      #     generate("context")
       #else:
        #return match.group(0)
