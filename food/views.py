from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import Food
from django.db.models import Avg
from .forms import FoodDetailForm


def menu_food_view(request):
    foods_list = Food.objects.all()
    paginator = Paginator(foods_list, 16)
    try:
        page = int(request.GET.get('page', '1'))
    except:

        page = 1

    try:
        foods = paginator.page(page)

    except (EmptyPage, InvalidPage):
        foods = paginator.page(paginator.num_pages)
    return render(request, 'food/menu-list.html', {'food_list': foods})


def detail_food_view(request, rid, slug):
    food_id = Food.objects.get(id=rid)
    rating_value = request.POST.get('rating')
    print(rating_value)
    print(request.POST)
    if request.is_ajax() and request.POST:

        # rank = Food.objects.get_or_create(rating=data[rating_value])
        rank = Food.objects.filter(food_id).annotate(rank=Avg(rating_value))
        food_id.rating = rank
        food_id.rating.save()
        data = {
                     "rating": True
                 }

        return JsonResponse(data, status=200)

    else:
        return render(request, 'food/detail_food.html', {'food_detail': food_id})

#     # print(rating_value)
#     print(request.is_ajax)
#     print(request.POST)
#     if request.is_ajax() and request.POST:
#
#         initial_rating = Food.objects.get_or_create('rating')
#         rating_value = Food.objects.get(initial_rating).annotate(avg_rating=Avg(food_id.rating))
#         rank += rating_value
#
#         data = {
#             "rating": True
#         }
#
#         return JsonResponse(data, status=200)
#     else:
#         return render(request, 'food/detail_food.html', {'food_detail': food_id})


    # some error occured
    # return JsonResponse({"error": ""}, status=400)
        # return  message to save rating
    # elif request.ajax:
    #      data = {
    #          'message':"Ok"
    #      }
    #      return JsonResponse(data)

    #     # food_detail = request.POST.get(food_rating).annotate(rating=Av)
    #
    #
    #     return render(request, 'food/detail_food.html', {'food_detail': food_rating})
    # else:
    # return render(request, 'food/detail_food.html', {'food_detail': food_rating})


# def detail_food_view(request, rid, slug):
#     food_id = Food.objects.get(id=rid)
#     if request.POST:
#         rating_value = request.POST.get('rating')
#         form = FoodDetailForm(request.POST)
#         print(rating_value)
#         if form.is_valid():
#             data = form.cleaned_data(request.POST)
#             rank = Food.objects.get_or_create(rating=data[rating_value])
#             rank.save()
#             print(form)
#             rank = Food.objects.filter(food_id).annotate(rank=Avg(rating_value))
#             food_id.rating = rank
#             food_id.rating.save()
#             return render(request, 'food/done.html')
#         else:
#             return render(request, 'food/detail_food.html', {'form': form})
#     else:
#         return render(request, 'food/detail_food.html', {'food_detail': food_id})



