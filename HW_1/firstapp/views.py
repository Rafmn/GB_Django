from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return render(request, 'index.html')

def about(request):
    logger.debug('Index page accessed')
    return render(request, 'aboutme.html')

