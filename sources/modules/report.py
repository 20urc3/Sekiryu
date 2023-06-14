import xmlrpc.client, re, os, datetime
import pandas as pd
from jinja2 import Template

proxy = xmlrpc.client.ServerProxy('http://localhost:13337')

def generate_infos():

  '''
  _TODO_ Infos:
      Scan summary and results
      List of identified file characteristics (e.g., file type, format, size, entry point, section headers, etc.)
      List of identified code features (e.g., function names, imports, exports, code sections, etc.)
      List of identified data features (e.g., strings, resources, metadata, etc.)
      List of identified anomalies or suspicious behavior (e.g., packers, obfuscation, anti-debugging, etc.)
      Recommendations for further analysis or actions (if necessary)
'''
  now = datetime.datetime.now()
  date_time = now.strftime("%Y-%m-%d %H:%M:%S")

def reporting():

    # Define the named blocks information and decompiled functions dictionaries
    named_blocks_infos =  proxy.rec_block_infos()
    decomp_function_dict = proxy.rec_decomp()

    # Convert the dictionaries to DataFrames
    named_blocks_df = pd.DataFrame(named_blocks_infos, index=[0])
    decomp_function_df = pd.DataFrame(decomp_function_dict, index=[0])

    template = Template('''
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Report</title>
      <style>
        body {
          margin: 0;
          padding: 0;
          font-family: Arial, sans-serif;
        }
        .container {
          max-width: 1000px;
          margin: 0 auto;
          padding: 20px;
        }
        .block {
          border: 1px solid #ddd;
          margin-bottom: 20px;
          padding: 10px;
          cursor: pointer;
          background-color: #E6F1F7;
        }
        .block h2 {
          display: inline-block;
          margin: 0;
        }
        .block .expand-icon {
          float: right;
          margin-left: 10px;
          font-size: 16px;
          line-height: 1;
          color: #555;
        }
        .block-content {
          max-height: medium;
          overflow: auto;
          text-align: center;
        }
        table {
          width: 100%;
          border-collapse: collapse;
          margin-bottom: 10px;
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
      <script>
        function toggleContent(blockId) {
          var content = document.getElementById(blockId + '-content');
          var expandIcon = document.getElementById(blockId + '-expand-icon');
          if (content.style.display === 'none') {
            content.style.display = 'block';
            expandIcon.innerHTML = '&#x25BC;';
          } else {
            content.style.display = 'none';
            expandIcon.innerHTML = '&#x25B6;';
          }
        }
      </script>
    </head>
    <body>
      <div class="container">
        <div class="block" onclick="toggleContent('named-blocks')">
          <h2>Named Blocks Information <span id="named-blocks-expand-icon" class="expand-icon">&#x25BC;</span></h2>
          <div id="named-blocks-content" class="block-content">
            <table>
              <thead>
                <tr>
                  {% for col in named_blocks_df.columns %}
                    <th>{{ col }}</th>
                  {% endfor %}
                </tr>
              </thead>
              <tbody>
                {% for _, row in named_blocks_df.iterrows() %}
                  <tr>
                    {% for value in row %}
                      <td>{{ value }}</td>
                    {% endfor %}
                  </tr>
                {% endfor %}
              </tbody>
            </table>
          </div>
        </div>
        <div class="block" onclick="toggleContent('decomp-functions')">
          <h2>Decompiled Functions <span id="decomp-functions-expand-icon" class="expand-icon">&#x25BC;</span></h2>
          <div id="decomp-functions-content" class="block-content">
            <table>
              <thead>
                <tr>
                  {% for col in decomp_function_df.columns %}
                    <th>{{ col }}</th>
                  {% endfor %}
                </tr>
              </thead>
              <tbody>
                {% for _, row in decomp_function_df.iterrows() %}
                  <tr>
                    {% for value in row %}
                      <td>{{ value }}</td>
                    {% endfor %}
                  </tr>
                {% endfor %}
              </tbody>
            </table>
          </div>
        </div>''')

    # Render the template with the data
    html_report = template.render(named_blocks_df=named_blocks_df, decomp_function_df=decomp_function_df)

    # Write the HTML report to a file
    with open('report.html', 'w') as f:
        f.write(html_report)

def report():
  reporting()
