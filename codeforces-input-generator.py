import bs4
import requests
from bs4 import BeautifulSoup
import sys


inp=""

inp=raw_input()

page=requests.get(inp,verify=True)

inputs_all=[]
outputs_all=[]



soup=BeautifulSoup(page.content,'html.parser')

for links in soup.find_all('div',class_="input"):
	inputs=links.find('pre')
	inputs_all.append(('\n'.join(inputs.findAll(text=True))))

for links in soup.find_all('div',class_="output"):
	inputs=links.find('pre')
	outputs_all.append(('\n'.join(inputs.findAll(text=True))))

size=len(inputs_all)
input_file=open("input.txt","w")
output_file=open("output.txt","w")

for i in range(size):
	input_file.write(inputs_all[i])
	output_file.write(outputs_all[i])

print("Input file created by the name input.txt")
print("Output file created by the name output.txt")
