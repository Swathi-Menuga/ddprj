from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	html = f'''

	<html>
		<body>
			<h1>welcome to Django Youtube</h1>
		</body>
	</html>

	'''
	return HttpResponse(html)