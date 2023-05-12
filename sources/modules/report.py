import xmlrpc.client, re, os, datetime
import pandas as pd
from jinja2 import Template

proxy = xmlrpc.client.ServerProxy('http://localhost:13337')
if not os.path.exists("Report"):
    os.makedirs("Report")
os.chdir("Report")

def generate_infos():

  '''
  Infos:
      Scan summary and results
      List of identified file characteristics (e.g., file type, format, size, entry point, section headers, etc.)
      List of identified code features (e.g., function names, imports, exports, code sections, etc.)
      List of identified data features (e.g., strings, resources, metadata, etc.)
      List of identified anomalies or suspicious behavior (e.g., packers, obfuscation, anti-debugging, etc.)
      Recommendations for further analysis or actions (if necessary)

      Binary Analysis reports typically focus on analyzing the behavior and characteristics of binary files, 
      such as executable files, DLLs, and drivers. These reports may include information about the file's format, 
      headers, sections, imports and exports, function names, data structures, and other technical details.

Malware Analysis reports, on the other hand, focus on analyzing the behavior and characteristics of malicious 
software, such as viruses, Trojans, and ransomware. These reports may include information about the malware's 
functionality, behavior, persistence mechanisms, network communication, and other relevant details.

Your report may fall under both categories if your binary scanner is designed to detect and analyze malware. 
However, the specific category of your report will depend on the focus of your analysis and the type of information
you are reporting
'''
  now = datetime.datetime.now()
  date_time = now.strftime("%Y-%m-%d %H:%M:%S")

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
  for key, value in source.items():
    f.write('%s:%s\n' % (key, value))
  f.close()
    
def ploting():

    # Define the named blocks information and decompiled functions dictionaries
    named_blocks_infos =  proxy.rec_block_infos()
    decomp_function_dict = proxy.rec_decomp()

    # Convert the dictionaries to DataFrames
    named_blocks_df = pd.DataFrame(named_blocks_infos, index=[0])
    decomp_function_df = pd.DataFrame(decomp_function_dict, index=[0])

    # Define the Jinja2 template
    template = Template('''
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Report</title>
      <style>
        table {
          border-collapse: collapse;
          width: 100%;
        }
        th, td {
          text-align: left;
          padding: 8px;
          border: 1px solid #ddd;
        }
        th {
          background-color: #4CAF50;
          color: white;
        }
        tr:nth-child(even) {
          background-color: #f2f2f2;
        }
      </style>
    </head>
    <body>
      <h1>Named Blocks Information</h1>
      {{ named_blocks_df.to_html(index=False) }}
      <h1>Decompiled Functions</h1>
      {{ decomp_function_df.to_html(index=False) }}
    </body>
    </html>
    ''')

    # Render the template with the data
    html_report = template.render(named_blocks_df=named_blocks_df, decomp_function_df=decomp_function_df)

    # Write the HTML report to a file
    f = open('report.html', 'w')
    f.write(html_report)
    f.close