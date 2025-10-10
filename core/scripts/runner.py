from ..models import Dokon,Mahsulot


def run():
    dokon1 = Dokon.objects.create(nomi = 'Anor Market',manzil = 'Yunusobod')
    dokon2 = Dokon.objects.create(nomi = 'Grand',manzil = 'Chilonzor')
    dokon3 = Dokon.objects.create(nomi = 'Makro',manzil = 'Sergeli')
    
    dokon1.maxsulotlar.create(nomi = 'Olma',narxi = 8000)
    dokon1.maxsulotlar.create(nomi = 'Banan',narxi = 15000)
    dokon1.maxsulotlar.create(nomi = 'Uzum',narxi = 12000)

    
    dokon2.maxsulotlar.create(nomi = 'Non',narxi = 5000)
    dokon2.maxsulotlar.create(nomi = 'Sut',narxi = 12000)
    dokon2.maxsulotlar.create(nomi = 'Tuxum',narxi = 18000)

    
    dokon3.maxsulotlar.create(nomi = 'Guruch',narxi = 5000)
    dokon3.maxsulotlar.create(nomi = 'Yog',narxi = 7500)
    dokon3.maxsulotlar.create(nomi = 'Shakar',narxi = 12000)
    dokon3.maxsulotlar.create(nomi = 'Tuz',narxi = 3000)