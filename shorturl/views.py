from django.shortcuts import render
from django.forms import URLField,EmailField
from django.shortcuts import render_to_response, get_object_or_404
import random, string, json
from shorturl.models import urls
from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.conf import settings
from django.template.context_processors import csrf
from django.core.exceptions import ValidationError
record = {} 
def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('shorturl/index.html', c)
 
def redirect_original(request, short_id):
    url = get_object_or_404(urls, pk=short_id) # get object, if not found return 404 error
    url.count += 1
    url.save()
    return HttpResponsePermanentRedirect(url.httpurl)
 
def shorten_url(request):
	url = request.POST.get("url", '')
	alias = request.POST.get("alias", '')
	valid_url,url=validate_url(url)
	if valid_url:
		if alias !='':
			for rec in record:
				if record[rec]==alias and url!=rec:
					return HttpResponse(json.dumps({"error":"error occurs", 'alias':-1, 'url':url}),content_type="application/json")

		if url in record:
			short_id = record.get(url)
			if alias !='' and alias != short_id:
				b = urls.objects.get(pk=short_id)
				b.short_id=alias
				b.save()		
				short_id = alias
				#record[url]=alias
			response_data = {}
			response_data['url'] = settings.SITE_URL + "/" + short_id
			return HttpResponse(json.dumps(response_data),  content_type="application/json")
		else:
			# check whether input is already short 
			
			if alias == '':
				short_id = get_short_code()
				record.update({url:short_id})
				b = urls(httpurl=url, short_id=short_id)
				b.save()
				response_data = {}
				response_data['url'] = settings.SITE_URL + "/" + short_id
				return HttpResponse(json.dumps(response_data),  content_type="application/json")

			elif is_already_short(url):
				response_data = {}
				return HttpResponse(json.dumps({"already_short": True}), content_type="application/json")

			else:
				record.update({url:alias})
				b = urls(httpurl=url, short_id=alias)
				b.save()
				response_data={}
				response_data['url'] = settings.SITE_URL + "/" + alias
				return HttpResponse(json.dumps(response_data),  content_type="application/json")
	return HttpResponse(json.dumps({"error": "error occurs", "valid_url":valid_url,'url':url}), content_type="application/json")

def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for _ in range(length))
        try:
            temp = urls.objects.get(pk=short_id)
        except:
            return short_id

'''
To check whether given URL is already short by checking existence of some popular URL shortners as a substring in URL

inputs 
url -> url link input

output
True -> if url is already short
False -> if url is not short
'''
def is_already_short(url):
    popular_shortening_urls = [
        'bit.ly/',
        'goo.gl/',
        'ow.ly/',
        'is.gd/',
        'buff.ly/',
        'adf.ly/',
        'tinyurl.com/',
        'bit.do/',
        'mcaf.ee/',
        't.co/',
        'tiny.cc/',
        'shorte.st/',
        'idek.net/',
        'po.st/',
        'yep.it/',
        'tr.im/',
        settings.SITE_URL,
    ]
    for shortening_url in popular_shortening_urls:
        if shortening_url in url:
            return True
    return False

def validate_url(url):
	protocols=[
		'http://',
		'https://',
	]
	flag=0
	url_form_field = URLField()
	email_field = EmailField()
	try :
		email_field.clean(url)
	except ValidationError:
		if url!='':
			for protocol in protocols:
				n=len(protocol)
				if url[0:n]==protocol:
					flag=1
					break
			if flag==0:
				flag1=1
				for protocol in protocols:
					new_url = protocol+url
					try:
						new_url == url_form_field.clean(new_url)
					except ValidationError:
						flag1=0
					else:
						url=new_url
						break
				if flag1==1:
					return True,url
				return False,url
			return True,url
		return False,url
	else:
		return False,url