from django.http.response import HttpResponse
from django.shortcuts import render
import urllib.parse
import base64
import html
import hashlib
import requests
import re

def index(request):
    return render(request, 'app/index.html')

def urlencode(request):
    normalText = request.POST.get('url_encode')
    encodedText = urllib.parse.quote_plus(normalText)
    return HttpResponse(encodedText)

def urldecode(request):
    encodedText = request.POST.get('url_decode')
    decodedText = urllib.parse.unquote(encodedText)
    return HttpResponse(decodedText)

def base64encode(request):
    normalText = request.POST.get('base64_encode')
    encodedText = base64.b64encode(bytes(normalText, 'utf-8'))
    return HttpResponse(encodedText)

def base64decode(request):
    encodedText = request.POST.get('base64_decode')
    decodedText = base64.b64decode(encodedText)
    return HttpResponse(decodedText)

def htmlencode(request):
    normalText = request.POST.get('html_encode')
    encodedText = html.escape(normalText)
    return HttpResponse(encodedText)

def htmldecode(request):
    encodedText = request.POST.get('html_decode')
    decodedText = html.unescape(encodedText)
    return HttpResponse(decodedText)

def md5generate(request):
    normalText = request.POST.get('md5_generate')
    md5Text =  hashlib.md5(normalText.encode())
    return HttpResponse(md5Text.hexdigest())

def md5decrypt(request):
    md5Text = request.POST.get('md5_decrypt')
    url = f"https://md5decrypt.net/en/Api/api.php?hash={md5Text}&hash_type=md5&email=palesob641@fada55.com&code=da2e8c971a0f5d7a"
    source = requests.get(url).text
    try:
        normalText = re.search(r'(?<=body>)([^<]+)', source).group()
    except AttributeError:
        return HttpResponse("Not Found")
    return HttpResponse(normalText)


def main(request):
    if request.method == "GET":
       return index(request)
    elif request.method == "POST" and "url_encode" in request.POST:
        return urlencode(request)
    elif request.method == "POST" and "url_decode" in request.POST:
        print("Inside decode")
        return urldecode(request)
    elif request.method == "POST" and "base64_encode" in request.POST:
        return base64encode(request)
    elif request.method == "POST" and "base64_decode" in request.POST:
        return base64decode(request)
    elif request.method == "POST" and "html_encode" in request.POST:
        return htmlencode(request)
    elif request.method == "POST" and "html_decode" in request.POST:
        return htmldecode(request)
    elif request.method == "POST" and "md5_generate" in request.POST:
        return md5generate(request)
    elif request.method == "POST" and "md5_decrypt" in request.POST:
        return md5decrypt(request)





