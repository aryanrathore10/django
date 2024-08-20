from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    people=[
    {"name": "John", "age": 30 ,},
    {"name": "Ram", "age": 20},
    {"name": "Johnnny", "age": 34},
    {"name": "Jack", "age": 40},
    {"name": "Ganesh", "age": 46},
    
]
    
    text= """Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta dolor quae earum adipisci obcaecati nemo doloremque nobis maxime, voluptatem beatae reiciendis repellat velit voluptates assumenda molestias error libero praesentium sint quidem ex saepe? Nisi vitae corporis, aspernatur temporibus voluptatem quaerat rem aut voluptas assumenda error consequatur perferendis deleniti ratione repellendus sit necessitatibus blanditiis eos veritatis placeat porro itaque vel.
"""
    Veg=['patato','pumpkin', 'tomato','onion']
    return render(request, 'websites/index.html', context={'people': people, 'text': text , 'Veg': Veg} )

def about(request):
    context= {'page': about}
    return render(request,'websites/about.html',context )

def contact(request):
    context= {'page': contact}
    return render(request, 'websites/contact.html',context)


