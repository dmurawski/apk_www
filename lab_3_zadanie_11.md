wyświetl wszystkie obiekty modelu Osoba,

>>> from class3app.models import Osoba
>>> Osoba.objects.all()
<QuerySet [<Osoba: Sebastian Kowal>, <Osoba: Sebastian Kowal>, <Osoba: Daniel N>, <Osoba: Damian Nowak>, <Osoba: sebastian Nowak>, <Osoba: Test1 Test2>, <Osoba: Seaseda XNowak>, <Osoba: asdasas dasdasd>, <Osoba: sada12121 dasdasd>]>
>, <Osoba: Test1 Test2>, <Osoba: Seaseda XNowak>, <Osoba: asdasas dasdasd>, <Osoba: sada12121 dasdasd>]>

wyświetl obiekt modelu Osoba z id = 3,

>>> Osoba.objects.filter(id=3)
<QuerySet []>
>>> Osoba.objects.filter(id=8)                   
<QuerySet [<Osoba: Damian Nowak>]>

wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu (tak, żeby był co najmniej jeden wynik),

>>> Osoba.objects.filter(nazwisko__startswith="T") 
<QuerySet [<Osoba: Test1 Test2>]>


wyświetl unikalną listę drużyn przypisanych dla modeli Osoba, 

wyświetl nazwy drużyn posortowane alfabetycznie malejąco,

>>> from class3app.models import Druzyna
>>> Druzyna.objects.all().order_by('-nazwa')   
<QuerySet [<Druzyna: LEGIA WARSZAWA PL>, <Druzyna: FC BARCELONA SP>, <Druzyna: 121 12>]>

dodaj nową instancję obiektu klasy Osoba

>>> Osoba.objects.create(imie="Tony", nazwisko="Stark")        
<Osoba: Tony Stark>
