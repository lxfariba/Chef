from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from food.models import Food, FoodQuantity, Order


def add_to_cart_view(request):
    food = Food.objects.get(id=request.POST.get('food-id'))
    quantity = int(1)
    if request.session.get('foods'):
        request.session['foods'].append({'name': food.name,
                                         'food_id': food.id,
                                         'price': food.price,
                                         'picture': food.picture_food.url,
                                         'quantity': quantity,
                                         })
        # for key, value in request.session.items():
        #     print('{} => {}'.format(key, value))

        subtotal = 0
        shipping = 5
        # total = 0

        for food in request.session['foods']:
            subtotal += food['price'] * food['quantity']
            total = subtotal + shipping

            request.session['subtotal'] = subtotal
            request.session['total'] = total
        request.session.save()
    else:
        request.session['foods'] = [{'name': food.name,
                                    'food_id': food.id,
                                    'price': food.price,
                                    'picture': food.picture_food.url,
                                    'quantity': quantity,
                                     }]

        subtotal = 0
        shipping = 5
        # total = 0

        for food in request.session['foods']:
            subtotal += food['price'] * food['quantity']
            total = subtotal + shipping

            request.session['subtotal'] = subtotal
            request.session['total'] = total
        request.session.save()
    return HttpResponseRedirect(reverse('food:cart'))


def cart_view(request):
    if request.session.get('foods'):
        if request.POST:
            # subtotal = request.POST.get('subtotal')
            # total = request.POST.get('total')
            # fid = request.POST.get('food-id')
            # for key, value in request.session.items():
            #     print('{} => {}'.format(key, value))
            # for food in request.session['foods']:
            #     food['quantity'] = (request.POST[food['food_id']])
            subtotal = 0
            shipping = 5
            # total = 0
            for food in request.session['foods']:
                subtotal += food['price'] * food['quantity']
                total = subtotal + shipping

                request.session['subtotal'] = subtotal
                request.session['total'] = total
            request.session.save()
    return render(request, 'Chef/cart.html')


def cart_item_delete_view(request):
    # //Delete items one by one
    if request.session.get('foods'):
        subtotal = request.session['subtotal']
        shipping = 5
        fid = request.POST.get('food-id')
        for food in request.session['foods']:
            if food['food_id'] == int(fid):
                subtotal -= food['price'] * int(food['quantity'])
                request.session['foods'].remove(food)
                request.session['subtotal'] = subtotal
                request.session['total'] = subtotal + shipping
            request.session.save()
        return HttpResponseRedirect(reverse('food:cart'))


def cart_delete_view(request):
    # /// Delete all orders in cart
    if request.session.get('foods'):
        del request.session['foods']

    return HttpResponseRedirect(reverse('food:menu_food'))
# def cart_view(request):
#     if request.session.get('foods'):
#         print("here111")
#         if request.POST:
#             print("here222")
#             for food in request.session['foods']:
#                 print(food['quantity'])
#                 food['quantity'] = (request.POST['food-' + str(food['food_id'])])
#             subtotal = 0
#             salestax = 0
#             shiping = 5
#             total = 0
#             for food in request.session['foods']:
#                 subtotal += food['price'] * food['quantity']
#                 salestax += subtotal * 0.05
#                 total += subtotal + shiping + salestax
#                 request.session['subtotal'] = subtotal
#                 request.session['total'] = total
#
#             request.session.save()
#     return render(request, 'Chef/cart.html')


def checkout_view(request):
    if request.user.is_authenticated():
        if request.session.get('foods'):
            if request.POST:
                order = Order.objects.create(customer=request.user, status='PEN')
                for session_food in request.session['foods']:
                    print(session_food['quantity'])
                    food_quantity = FoodQuantity.objects.create(food_id=session_food['food_id'],
                                                                quantity=session_food['quantity']
                                                                )
                    order.foods.add(food_quantity)
                    print(order)
                del request.session['foods']
                return render(request, 'food/checkout_list.html', {'msg': 'Ok'})
            else:
                return render(request, 'food/checkout_list.html')
    else:
        # if request.is_ajax():
            data = {
                'message': "You have to login !!!"
            }
            return JsonResponse(data)
            # return HttpResponseRedirect(reverse('account:login'), {'ok':ok})


