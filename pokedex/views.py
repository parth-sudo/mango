from django.shortcuts import render
from .forms import GuessPokemon,PokeSearch, PokeSearchByName
from .models import Region, AboutUs
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]


# Create your views here.

def home(request):
    return render(request, 'pokedex/home.html', {})

def regions(request):
    regions = Region.objects.all()
    context = {'regions': regions}
    return render(request, 'pokedex/regions.html', context)


def result(base_HP, attack, defense, special_attack, special_defense,
                   speed, generation, legendary):

    # ML Model begins.-----------------------------------------------
    df = pd.read_csv("C:/Users/Yadnesh/Downloads/pokemre.csv")

    df.head()

    Y = df.Name
    features = ['HP', 'Attack', 'Defense', 'Sp. Atk',
                'Sp. Def', 'Speed', 'Generation', 'Legendary']
    X = df[features]

    train_X, val_X, train_y, val_y = train_test_split(X, Y, test_size=0.3, random_state=66)

    iowa_model = RandomForestClassifier(random_state=1, criterion="entropy")

    iowa_model.fit(train_X, train_y)

    val_prediction = iowa_model.predict(val_X)
    # print(val_prediction)

    # print("Enter the following info")
    # Total1=input("Enter total-:")
    HP1 = base_HP
    Attack1 = attack
    Defense1 = defense
    SpAtk1 = special_attack
    SpDef1 = special_defense
    Speed1 = speed
    Generation1 = generation
    Legendary1 = legendary

    pre = [[HP1, Attack1, Defense1, SpAtk1, SpDef1, Speed1, Generation1, Legendary1]]

    answer = str((iowa_model.predict(pre)))[1:-1]

    return answer


def Guesser(request):
    if request.method == 'POST':
        form = GuessPokemon(request.POST)
        if form.is_valid():
            base_HP = form.cleaned_data['base_HP']
            attack = form.cleaned_data['attack']
            defense = form.cleaned_data['defense']
            special_attack = form.cleaned_data['special_attack']
            special_defense = form.cleaned_data['special_defense']
            speed = form.cleaned_data['speed']
            generation = form.cleaned_data['generation']
            legendary = form.cleaned_data['legendary']

            answer = result(base_HP,attack,defense,special_attack,special_defense,speed,generation,legendary)

            return render(request, 'pokedex/result.html', {'result': answer})

    else:
       form = GuessPokemon()

    return render(request, 'pokedex/forms.html', {'form':form})


def studs(request):
    studs = AboutUs.objects.all()
    context = {'studs': studs}
    return render(request, 'pokedex/about.html', context)

#search by pokemon number.
def search(request):
    context = {}
    names = ['no one', 'Bulbasaur', 'Ivysaur', 'Venusaur',
                     'Charmander', 'Charmeleon', 'Charizard',
                     'Squirtle', 'Wartortle', 'Blastoise',
                     'Caterpie', 'Metapod', 'Butterfree']

    if request.method == 'POST':
        form_2 = PokeSearchByName(request.POST)
        if form_2.is_valid():

            pokemon_name = form_2.cleaned_data['pokemon_name']

            dex_no = names.index(pokemon_name)


            dict = {
                    'pokemon': pokemon_name,

                       'names' : names}

             #number is a form input. names is the list.


            context = { 'dict' : dict,

                        'dex_number' : dex_no}


            return render(request, 'pokedex/search.html', context)

    else:
        form = PokeSearch()
        form_2 = PokeSearchByName()

    return render(request, 'pokedex/search.html', {
                                                   'form2' : form_2,
                                                   'names':names})

#search by pokemon name.
