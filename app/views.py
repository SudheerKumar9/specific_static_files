from django.shortcuts import render

# Create your views here.
def specific_static(request):
    return render(request,'specific_static.html')

def assignment8(request):
    return render(request,'assignment8.html')