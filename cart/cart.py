from django.conf import settings


# class Cart(object):
#
#     def __init__(self, request):
#         """
#         Инициализируем корзину
#         """
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)
#         if not cart:
#             # save an empty cart in the session
#             cart = self.session[settings.CART_SESSION_ID] = {}
#         self.cart = cart
#
#
#
# def add(self, printer,):
#     """
#     Добавить продукт в корзину или обновить его количество.
#     """
#     printer_id = str(printer.id)
#     if printer_id not in self.cart:
#         self.cart[printer_id] = {'quantity': 0,
#                                  'price': str(product.price)}
#     if update_quantity:
#         self.cart[product_id]['quantity'] = quantity
#     else:
#         self.cart[product_id]['quantity'] += quantity
#     self.save()
#
# def save(self):
#     # Обновление сессии cart
#     self.session[settings.CART_SESSION_ID] = self.cart
#     # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
#     self.session.modified = True