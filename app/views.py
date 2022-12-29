from django.shortcuts import render

# Create your views here.
def filter(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'Hai DjanGo And PytHon','dt':dt,'c':1}
    return render(request,'filter.html',d)

def userdefine'dfilters(request):
    d={'data':'HI PYTHON how R you'}
    return render(request,'userdefinedfilters.html',d)