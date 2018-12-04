from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.utils import json

from .models import CityOwned
from mainPage.models import Server, CityPositions
from .forms import CityOwnedForm
# Create your views here.
from worldMap.models import delete_attack


@login_required(login_url='../../../../../../../')
def main_page_city_list(request):
    delete_attack(5, schedule=10)
    user = request.user
    city_list = CityOwned.objects.filter(city_owner=user.id)
    return render(request, 'indexCityList.html', {'city_list': city_list})


@login_required(login_url='../../../../../../../')
def main_page_city_id(request, id_of_city):
    brak_miasta = 0
    user = request.user
    city = CityOwned.objects.get(city_owner=user.id, id=id_of_city)
    return render(request, 'indexCityMap.html', {'brak_miasta': brak_miasta, 'city': city})


@login_required(login_url='../../../../../../../')
def town_hall_city_id(request, id_of_city):
    return render(request, 'townhall.html', {'id_of_city': id_of_city})


@login_required(login_url='../../../../../../../')
def farms_city_id(request, id_of_city):
    city = CityOwned.objects.get(id = id_of_city)
    current_level = city.farms
    current_level_production = city.farms*10
    next_level = city.farms+1
    next_level_production =(city.farms+1) * 10
    return render(request, 'farms.html', {'next_level': next_level, 'current_level': current_level, 'current_level_production': current_level_production, 'next_level_production': next_level_production})


@login_required(login_url='../../../../../../../')
def roads_city_id(request, id_of_city):
    city = CityOwned.objects.get(id=id_of_city)
    current_level = city.roads
    current_level_production = city.roads * 2
    next_level = city.roads + 1
    next_level_production = (city.roads + 1) * 2
    return render(request, 'roads.html', {'next_level': next_level, 'current_level': current_level,
                                               'current_level_production': current_level_production,
                                               'next_level_production': next_level_production})


@login_required(login_url='../../../../../../../')
def powerPlant_city_id(request, id_of_city):
    city = CityOwned.objects.get(id=id_of_city)
    current_level = city.power_plant
    current_level_production = city.power_plant * 10
    next_level = city.power_plant + 1
    next_level_production = (city.power_plant + 1) * 10
    return render(request, 'powerPlant.html', {'next_level': next_level, 'current_level': current_level,
                                          'current_level_production': current_level_production,
                                          'next_level_production': next_level_production})


@login_required(login_url='../../../../../../../')
def mines_city_id(request, id_of_city):
    city = CityOwned.objects.get(id=id_of_city)
    current_level = city.mines
    current_level_production = city.mines * 10
    next_level = city.mines + 1
    next_level_production = (city.mines + 1) * 10
    return render(request, 'mines.html', {'next_level': next_level, 'current_level': current_level,
                                          'current_level_production': current_level_production,
                                          'next_level_production': next_level_production})


@login_required(login_url='../../../../../../../')
def barracks_city_id(request, id_of_city):
    return render(request, 'barracks.html', {'id_of_city': id_of_city})


@login_required(login_url='../../../../../../../')
def housing_city_id(request, id_of_city):
    return render(request, 'housing.html', {'id_of_city': id_of_city})


@login_required(login_url='../../../../../../../')
def main_page_city(request):
    user = request.user
    if request.method == 'POST':
        form = CityOwnedForm(request.POST)
        if form.is_valid():

            city = form.save(commit=False)
            city.city_owner = user

            server = Server.objects.get(id=1)
            city.pos_x = server.next_village_x
            city.pos_y = server.next_village_y
            server.next_village_id = server.next_village_id + 1
            server.save()
            next_city_pos = CityPositions.objects.get(id=server.next_village_id)
            server.update_village_pos(next_city_pos.village_x, next_city_pos.village_y)
            server.save()

            city.town_hall = 2
            city.barracks = 2
            city.roads = 1
            city.mines = 1
            city.power_plant = 1
            city.farms = 1
            city.is_capital = True
            city.save()
            return redirect('city_list/')
        else:
            city = CityOwned.objects.filter(city_owner=user.id)
            brak_miasta = 1
            return render(request, 'indexCityMap.html', {'city': city, 'brak_miasta': brak_miasta, 'form': form})

    elif user.is_authenticated:
        try:
            CityOwned.objects.get(city_owner=user.id, is_capital=True)
        except CityOwned.DoesNotExist:
            brak_miasta = 1
            form = CityOwnedForm()
            return render(request, 'indexCityMap.html', {'brak_miasta': brak_miasta, 'form': form})

        return redirect('city_list/')
    else:
        return redirect('../')


@login_required(login_url='../../../../../../../')
def colonize_new_city(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        have_enought_resources = data['resource_check']
        if have_enought_resources == 1:
            city = CityOwned(city_name=data['city_name'])
            city.city_owner = request.user

            server = Server.objects.get(id=1)
            city.pos_x = server.next_village_x
            city.pos_y = server.next_village_y
            server.next_village_id = server.next_village_id + 1
            server.save()
            nextCityPos = CityPositions.objects.get(id=server.next_village_id)
            server.update_village_pos(nextCityPos.village_x, nextCityPos.village_y)
            server.save()

            city.town_hall = 2
            city.barracks = 2
            city.roads = 1
            city.mines = 1
            city.power_plant = 1
            city.farms = 1
            city.is_Capital = False
            city.save()
            return redirect('../city_list/')
        return redirect('../city_list/')
    return redirect('../city_list/')
