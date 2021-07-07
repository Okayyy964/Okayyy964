from django.shortcuts import render
from .forms import Post_check,Post_generate_code

import json

def main(request):
	return render(request,'main/index.html')


def check(request):
	form = Post_check()
	return render(request,'main/check.html',{'form':form})

def generate(request):
	form = Post_generate_code()
	return render(request,'main/generate.html',{'form':form})


def post_check(request):
	text = ''
	n = 1
	if request.method == 'POST':
		form = Post_check(request.POST)
		if form.is_valid():
			try:
				group = form.cleaned_data.get('text_code')[:-8]
				code = int(form.cleaned_data.get('text_code')[-8:])
			except:
				text += 'error'
				return render(request,'main/check_done.html', {'text':text})

			with open('main/static/keys/dict.json','r') as file:
				DICT = json.load(file)

				for key,val in DICT.items():
					if key == 'len':
						continue
					elif (code in DICT[group]) and (group in DICT.keys()):
						text += 'This code is activated'
						
						DICT[group].remove(code)
						print(DICT)
						with open('main/static/keys/dict.json','w') as file:
							json.dump(DICT,file)
						return render(request,'main/check_done.html', {'text':text})
					else:
						n += 1

				if len(DICT.keys())	== n:
					text += 'error'
					return render(request,'main/check_done.html', {'text':text})
			
		else:	
			return render(request,'main/check.html', {'form':form})	
	else:	
		form = Post_check()
		return render(request, 'main/check.html', {'form':form})	

def post_generate(request):
	text = ''
	i = 10000000
	if request.method == 'POST':
		form = Post_generate_code()
		form = Post_generate_code(request.POST)	
		if form.is_valid():
			group = form.cleaned_data.get('group_name')
			number = form.cleaned_data.get('number_codes')
			with open('main/static/keys/dict.json','r') as file:
				DICT = json.load(file)
				print(DICT)
				if group not in DICT.keys():
					print('Not found')		
					DICT[group] = []
					for n in range(number):
						DICT['len'] = DICT['len'] + 1
						DICT[group].append(i + DICT['len'])
					with open('main/static/keys/dict.json','w') as file:
						json.dump(DICT,file)
				else:
					print('Find')
					for n in range(number):
						DICT['len'] = DICT['len'] + 1
						DICT[group].append(i + DICT['len'])
					with open('main/static/keys/dict.json','w') as file:
						json.dump(DICT,file)
			return render(request,'main/generate_done.html', {'number':number,'group':group})
		else:
			text += 'error'
			return	render(request,'main/generate.html', {'form':form})		
	else:
		form = Post_generate_code()
		return	render(request,'main/generate.html', {'form':form})			