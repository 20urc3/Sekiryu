from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from typing import Optional, Dict

import numpy as np
import pandas as pd
import dataplane as dp
import openai, threading, readline, os

def get_openai_api_key():
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    if openai.api_key:
        return openai.api_key
    else:
        openai.api_key = input("Please enter your OpenAI API key: ")
        # Save the API key permanently in the system
        with open(os.path.expanduser("~/.bashrc"), "a") as f:
            f.write(f'\nexport OPENAI_API_KEY="{openai.api_key}"')
        os.environ['OPENAI_API_KEY'] = openai.api_key

get_openai_api_key()

class XMLServerThread(threading.Thread):
	def __init__(self, host='localhost', port=13337):
		super().__init__()
		self.server = SimpleXMLRPCServer((host, port), logRequests=False, allow_none=True)

		# Initiate variables
		self.decompiled_code = {}
		self.decompiled_block_infos = {}

		# Register functions with the server instance:
		self.server.register_function(self.request_GPT)
		self.server.register_function(self.analyse_GPT)
		self.server.register_function(self.rec_decomp)
		self.server.register_function(self.send_decomp)
		self.server.register_function(self.rec_block_infos)
		self.server.register_function(self.send_block_infos)

	def run(self):
		# Start server
		print("Server started.")
		self.server.serve_forever()

	def stop(self):
		# Exit server
		print("Server exited.")
		self.server.shutdown()

	def send_decomp(self, input):
		""" 
		Receive decompiled code from Ghidra
		"""
		self.decompiled_code = input

	def rec_decomp(self):
		""" 
		Return the decompiled code received
		"""
		return self.decompiled_code

	def send_block_infos(self, input):
		"""
		Receive infos about the decompiled binary
		"""
		self.decompiled_block_infos = input

	def rec_block_infos(self):
		"""
		Return info about decompiled binary
		"""
		return self.decompiled_block_infos


	def request_GPT(self, string):
		"""
		Generic request method to ChatGPT
		"""
		try:
			response = openai.Completion.create(
				model="text-davinci-003",
				prompt=string,
				max_tokens=4000,
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


	def analyse_GPT(self, string):
		"""
		Analyse funcs received with chatGPT
		"""

		# Specify request for commenting / analyse
		string = "Modify the following code snippet by adding comment on how it works and change variable and function name for more understeable one"
		self.request_GPT(string)