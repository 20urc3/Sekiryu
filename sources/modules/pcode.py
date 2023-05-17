import xmlrpc.client, re, os 

proxy = xmlrpc.client.ServerProxy('http://localhost:13337')

def simple_source(input):
	os.chdir("output")
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
	os.chdir("output")
	# Cleaning filename
	filename = input
	regex_pattern = r"\.[^.]+$"
	stripped_filename = re.sub(regex_pattern, "", filename)

	# Writing gpt_pcode.c file
	source = proxy.rec_decomp()
	f = open(f'{stripped_filename}_gpt_pcode.c', 'w')
	for key, value in source.items():
		f.write('%s:%s\n' % (key, value))
	f.close()
