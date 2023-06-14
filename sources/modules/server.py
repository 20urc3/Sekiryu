from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from typing import Optional, Dict

import numpy as np
import pandas as pd
import dataplane as dp
import threading, readline, os


class XMLServerThread(threading.Thread):
	def __init__(self, host='localhost', port=13337):
		super().__init__()
		self.server = SimpleXMLRPCServer((host, port), logRequests=False, allow_none=True)

		# Initiate variables
		self.decompiled_code = {}
		self.decompiled_block_infos = {}

		self.data = {}

		# Register functions with the server instance:
		self.server.register_function(self.rec_decomp)
		self.server.register_function(self.send_decomp)
		self.server.register_function(self.rec_block_infos)
		self.server.register_function(self.send_block_infos)
		self.server.register_function(self.send_data)
		self.server.register_function(self.recv_data)
		self.server.register_function(self.request_GPT)

	def send_data(self, input):
		"""
		Receive general data from User
		"""
		self.data = input

	def recv_data(self):
		"""
		Send general data to User
		"""
		return self.data

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
		get_openai_api_key()

		response = openai.Completion.create(
			model="text-davinci-003",
			prompt=string,
			max_tokens=4000,
			temperature=0.6,
			frequency_penalty=1,
			presence_penalty=1
			)
		try:
			answer = response["choices"][0]["text"]
			return(answer)
		except(KeyError, IndexError) as e:
			pass
