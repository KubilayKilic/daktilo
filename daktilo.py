"""by KubilayKilic"""

from __future__ import print_function, division

import string
import turtle

"""
daktiloyu kullanmak için harfler ve cokgen modülünüzün olması gerekmektedir.
"""

# bu modülün varlığını kontrol et harfler.py
try:
    import harfler
except ImportError as e:
    message = e.args[0]
    if message.startswith('Modül Yok'):
        raise ImportError(message + 
                          '\nharfler.py Modülünü bulundurmanız gerekmektedir.')


def isinlan(t, x, y):
    """çizgi çizmeden turtle'ı ışınlar.
    önkoşul: kalem aşağı konumda
    t: Turtle
    x: koordinat
    y: koordinat
    """
    t.pu()
    t.goto(x, y)
    t.pd()


def tus(char):
    """kullanıcının klavyesinde tuş basmasını kontrol eder.
    """
    # önceki harf çiziliyorsa çiziyorsak
    if oogway.busy:
        return
    else:
        oogway.busy = True

    # gerekli fonksiyonu çağır
    try:
        name = 'draw_' + char
        func = getattr(harfler, name)
    except AttributeError:
        print("bu karakteri çizmeyi bilmiyorum, henüz?..", char)
        oogway.busy = False
        return

    func(oogway, size)

    harfler.atla(oogway, size/2)
    oogway.busy = False


def carriage_return():
    """sonraki satıra ilerler.
    """
    isinlan(oogway, -180, oogway.ycor() - size*3)
    oogway.busy = False


def presser(char):
    """basılan karaktere dönen fonksiyon.
    char: çizilecek karakter
    returns: fonksyiona geri döner.
    """
    def func():
        tus(char)
    return func


# oogway'in pozisyonunu ayarla
size = 20
oogway = turtle.Turtle()
oogway.busy = False
isinlan(oogway, -180, 150)

# ekrana getir.
screen = oogway.getscreen()

for char in string.ascii_lowercase:
    screen.onkey(presser(char), char)

screen.onkey(carriage_return, 'Return')

screen.listen()
turtle.mainloop()
