from urllib.request import Request, urlopen
from sys import argv

def fetch_html_text(url):
  req = Request(
          url, 
          headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0'}
        )
  web_byte = urlopen(req).read()
  return web_byte.decode('utf-8')
 
class Testcase:
  def __init__(self, input_text, output_text):
    self.input_text = input_text
    self.output_text = output_text

def generate_testcases(html_text):
  testcases_data = html_text.split('<div class="input"><div class="title">Input</div><pre>')[1:]

  testcases_data[-1] = testcases_data[-1].split("</div></div></div><p>  </p></div>")[0];

  testcases = list()
  for testcase in testcases_data:
    inp, out = testcase.split('</pre></div><div class="output"><div class="title">Output</div><pre>')
    out = out.split('</pre></div>')[0]
    testcases.append(Testcase(inp, out))
  return testcases

# Assumes that the problems directory is created
def save_testcases(testcases, problem_letter):
  for index, testcase in enumerate(testcases):
    base = problem_letter + "/" + str(index + 1)
    with open(base + ".in", "w") as input_file:
      input_file.write(testcase.input_text.strip())
    with open(base + ".out", "w") as output_file:
      output_file.write(testcase.output_text.strip())
    
def main():
  url = argv[1]
  
  html_text = fetch_html_text(url)

  testcases = generate_testcases(html_text)

  save_testcases(testcases, url[-1])

if __name__ == "__main__":
    main()
