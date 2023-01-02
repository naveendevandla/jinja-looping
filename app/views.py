from django.shortcuts import render

# Create your views here.
def loops(request):
    k={'jim':'kim','h':[78,67,90]}
    return render(request,'loops.html',k)