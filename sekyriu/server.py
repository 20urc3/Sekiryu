from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from typing import Optional, Dict

import numpy as np
import pandas as pd
import dataplane as dp
import openai, os, sys, re, textwrap, sqlite3

# Starting screen

def starting():
	print('''

 ,,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
                                     .$"
                                     "

... Starting Sekiryu Server ...

''')

# Creating server:

server = SimpleXMLRPCServer(('localhost', 13337), logRequests=True, allow_none=True)

 
# Defining functions:

def api_key():

	"""
	Defining the API_KEY
	"""
	opeanai.api_key = os.getenv("OPEN_API_KEY")

def request_GPT(string):

	"""
	Simple request to ChatGPT
	"""
	try:
		response = openai.Completion.create(
			model="text-davinci-003",
			prompt=string,
			max_tokens=3000,
			temperature=0.6,
			frequency_penalty=1,
			presence_penalty=1
            )
	except openai.OpenAIError as e:
		raise print(f"Error: {str(e)}")
	try:
		answer = response["choices"][0]["text"]
	except(KeyError, IndexError) as e:
		pass
	return(answer) 

def analyse_GPT(string):
	
	"""
	Analyse funcs received with chatGPT
	"""

	string = "Modify the following code snippet by adding comment on how it works, change variable and function name for more understeable one and add [FUNC_START] before the snippet and newline [FUNC_END] after the snippet + string"
	try:
		response = openai.Completion.create(
            model="text-davinci-003",
            prompt=string,
            max_tokens=3000,
            temperature=0.6,
            frequency_penalty=1,
            presence_penalty=1
            )
	except openai.OpenAIError as e:
		raise print(f"Error: {str(e)}")
	try:
		answer = response["choices"][0]["text"]
	except(KeyError, IndexError) as e:
		pass
	f = open("analyzed_PCode.txt", "a")
	answer = "[START]" + answer + "\n[END]"
	f.write(str(answer))
	f.close()


def generate_sql(db_name, table_name, text):
    # Connect to the database
    conn = sqlite3.connect(db_name)

    # Create a table to store the extracted functions
    conn.execute(f'''CREATE TABLE {table_name}
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  function TEXT NOT NULL)''')

    # Define the regular expression pattern
    pattern = r'\[START\](.*?)\[END\]'

    # Find all matches in the text using the regex
    matches = re.findall(pattern, text, re.DOTALL)

    # Insert each function into the database
    for func in matches:
        conn.execute(f"INSERT INTO {table_name} (function) VALUES (?)", (func,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Register functions with the server instance:

#server.register_function(identify_vuln_GPT)
#server.register_function(find_vulnerability)
server.register_function(request_GPT)
server.register_function(analyse_GPT)
server.register_function(generate_sql)

if __name__ == '__main__':
	try:
		print(starting())
		server.serve_forever()
	except KeyboardInterrupt:
		print('My mission is done. Exiting.')
