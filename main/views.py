from django.shortcuts import render

# Create your views here.
def upload_file(request):

    context={}
    return render(request,'index.html',context)