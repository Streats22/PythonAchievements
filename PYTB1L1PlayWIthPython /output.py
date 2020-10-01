Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 100
300
>>>  100 - 10
 
SyntaxError: unexpected indent
>>> 25 / 5
5.0
>>> 100 - 10
90
>>> 10 / 3
3.3333333333333335
>>> 10 //3
3
>>> print('Mijn is Robin Schoenmaker')
Mijn is Robin Schoenmaker
>>> naam = 'Robin Schoenmaker'
>>> print(naam)
Robin Schoenmaker
>>> print(naam.upper())
ROBIN SCHOENMAKER
>>> print(naam[0:2])
Ro
>>> print(naam[::-1])
rekamneohcS niboR
>>> leeftijd = 22
>>> print('Hallo' + naam + 'Ben je al ' +str(leeftijd) + jaar ')
      
SyntaxError: EOL while scanning string literal
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Robin Schoenmaker ben je al 22 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
23
>>> leeftijd-=1
>>> leeftijd
22
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('over' +str(hoelang_tot18jaar) + 'jaar wordt je 18')
	elif leeftijd > 18:
		
SyntaxError: invalid syntax
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('over' +str(hoelang_tot18jaar) + 'jaar wordt je 18')
elif
SyntaxError: invalid syntax
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('over' +str(hoelang_tot18jaar) + 'jaar wordt je 18')
elif leeftijd > 18:
	hoelang_al18jaar = leeftijd - 18
	print('Het is alweer' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werdt')
else:
	print('Je bent precies ' + str(leeftijd) + ' Jaar')

	
Het is alweer4 jaar geleden dat je 18 werdt
>>> from random import rnadint
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    from random import rnadint
ImportError: cannot import name 'rnadint' from 'random' (/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/random.py)
>>> from random import randint
>>> randint(0, 1000)
157
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
772
>>> print('Willekeurig getal tussen de 0 en 1000:' + str(willekeurig_getal))
Willekeurig getal tussen de 0 en 1000:772
>>> from datetime import datetune
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    from datetime import datetune
ImportError: cannot import name 'datetune' from 'datetime' (/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/datetime.py)
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-10-01 13:25:12.951703
>>> datum.strftime('%A %d %b %Y')
'Thursday 01 Oct 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %b %Y')
'donderdag 01 okt 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %b %Y')
'Giovedì 01 Ott 2020'
>>> 