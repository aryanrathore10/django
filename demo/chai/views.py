from django.shortcuts import render

def chai(request):
    return render(request, 'chaiwale/chai.html')
