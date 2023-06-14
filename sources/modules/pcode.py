import xmlrpc.client, re, os, openai, sys

proxy = xmlrpc.client.ServerProxy('http://localhost:13337')

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

def request_GPT(string):
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

def simple_source(input):
	
	# Cleaning filename
	filename = input
	regex_pattern = r"\.[^.]+$"
	stripped_filename = re.sub(regex_pattern, "", filename)
	
	# Writing pcode.c file
	source = proxy.rec_decomp()
	f = open(f'{stripped_filename}_pcode.c', 'w')
	for key, value in source.items():
		f.write('%s:%s\n' % (key, value))
	f.close()


def gpt_source(input):

	# Cleaning filename
	filename = input
	regex_pattern = r"\.[^.]+$"
	stripped_filename = re.sub(regex_pattern, "", filename)

	# Writing gpt_pcode.c file
	source = proxy.rec_decomp()
	f = open(f'{stripped_filename}_gpt_pcode.c', 'w')
	string = "Modify the following code snippet by adding comment explain what the code do and change variable and function name for more understeable one: "
	try:
		for key, value in source.items():
			msg = request_GPT(string + str(value))
			f.write('%s:%s\n' % (key, msg))
	except openai.OpenAIError as e:
		print(f"Error: {str(e)}")
		pass
	f.close()

def vuln_gpt(input):
	# Cleaning filename
	filename = input
	regex_pattern = r"\.[^.]+$"
	stripped_filename = re.sub(regex_pattern, "", filename)
	# Writing gpt_pcode.c file
	source = proxy.rec_decomp()
	f = open(f'{stripped_filename}_vuln_gpt_pcode.c', 'w')
	string = "Modify the following code snipped to add comment that: Analyze the following function and determine if there is a possible vulnerability: "
	try:
		for key, value in source.items():
			msg = request_GPT(string + str(value))
			f.write('%s:%s\n' % (key, msg))
	except openai.OpenAIError as e:
		print(f"Error: {str(e)}")
		pass
	f.close()

def mal_gpt(input):
	# Cleaning filename
	filename = input
	regex_pattern = r"\.[^.]+$"
	stripped_filename = re.sub(regex_pattern, "", filename)
	# Writing gpt_pcode.c file
	source = proxy.rec_decomp()
	f = open(f'{stripped_filename}_mal_gpt_pcode.c', 'w')
	string = "Modify the following code snipped to add comment that: Analyze the following function and determine if the behavior might harmfull / malware: "
	try:
		for key, value in source.items():
			msg = request_GPT(string + str(value))
			f.write('%s:%s\n' % (key, msg))
	except openai.OpenAIError as e:
		print(f"Error: {str(e)}")
		pass
	f.close()
