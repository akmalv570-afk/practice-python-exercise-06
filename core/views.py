from django.shortcuts import render
from .models import Dokon

# Create your views here.

def index(request):
    dokonlar = Dokon.objects.all()
    dokon_list = []

    for dokon in dokonlar:
        mahsulotlar = dokon.mahsulotlar.all()
        onmingdan_arzoni = dokon.mahsulotlar.filter(narxi__lt = 10000)
        maxsulotlar_soni = dokon.mahsulotlar.count()
        dokon_list.append (
            {
                "dokon":dokon,
                "mahsulotlar":mahsulotlar,
                "onmingdan_arzoni":onmingdan_arzoni,
                "maxsulotlar_soni":maxsulotlar_soni

            }
        )
    return render(request,'core/index.html',{'dokon_list':dokon_list})

