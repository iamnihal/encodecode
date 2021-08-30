from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import urllib.parse
import base64
import html
import hashlib
import requests
import re
import json


def index(request):
    return render(request, "app/index.html")


def urlencode(request):
    plainText = request.POST.get("url_encode")
    encodedText = urllib.parse.quote_plus(plainText)
    return HttpResponse(encodedText)


def urldecode(request):
    encodedText = request.POST.get("url_decode")
    decodedText = urllib.parse.unquote(encodedText)
    return HttpResponse(decodedText)


def base64encode(request):
    plainText = request.POST.get("base64_encode")
    encodedText = base64.b64encode(bytes(plainText, "utf-8"))
    return HttpResponse(encodedText)


def base64decode(request):
    encodedText = request.POST.get("base64_decode")
    decodedText = base64.b64decode(encodedText)
    return HttpResponse(decodedText)


def htmlencode(request):
    plainText = request.POST.get("html_encode")
    encodedText = html.escape(plainText)
    return HttpResponse(encodedText)


def htmldecode(request):
    encodedText = request.POST.get("html_decode")
    decodedText = html.unescape(encodedText)
    return HttpResponse(decodedText)


def md5generate(request):
    plainText = request.POST.get("md5_generate")
    md5Text = hashlib.md5(plainText.encode())
    return HttpResponse(md5Text.hexdigest())


def md5decrypt(request):
    md5Text = request.POST.get("md5_decrypt")
    url = f"https://md5decrypt.net/en/Api/api.php?hash={md5Text}&hash_type=md5&email=palesob641@fada55.com&code=da2e8c971a0f5d7a"
    try:
        source = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
            },
        )
        if source.text:
            return HttpResponse(source.text)
        else:
            return HttpResponse("Not Found")
    except:
        return HttpResponse("500 Server Error")


def json_prettify(request):
    input_json = request.POST.get("json_data")
    json_object = json.loads(input_json)
    json_prettify = json.dumps(json_object, indent=2)
    return HttpResponse(json_prettify)


def sha1generate(request):
    plainText = request.POST.get("sha1_generate")
    sha1Text = hashlib.sha1(plainText.encode())
    return HttpResponse(sha1Text.hexdigest())


def sha256generate(request):
    plainText = request.POST.get("sha256_generate")
    sha256Text = hashlib.sha256(plainText.encode())
    return HttpResponse(sha256Text.hexdigest())


def sha512generate(request):
    plainText = request.POST.get("sha512_generate")
    sha512Text = hashlib.sha512(plainText.encode())
    return HttpResponse(sha512Text.hexdigest())


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
    elif request.method == "POST" and "sha1_generate" in request.POST:
        return sha1generate(request)
    elif request.method == "POST" and "sha256_generate" in request.POST:
        return sha256generate(request)
    elif request.method == "POST" and "sha512_generate" in request.POST:
        return sha512generate(request)
    elif request.method == "POST" and "json_data" in request.POST:
        return json_prettify(request)
