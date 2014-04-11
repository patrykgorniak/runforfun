from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from parser import main


def run_parser(request):
    content = main.rff_run(request)
    response = HttpResponse(content, content_type="text/plain")
    return response
