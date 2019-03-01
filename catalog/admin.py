from django.contrib import admin
from .models import Type, Brand, Item, Favorites, Shopping_cart, Delivery_company, Delivery, Pay, Complaint_type, Complaint, Re_complaint, Return_type, Return_service, Problem_type, Problem_report, Re_problem, Comment, Re_comment

admin.site.register(Type)
admin.site.register(Brand)
admin.site.register(Item)
admin.site.register(Favorites)
admin.site.register(Shopping_cart)
admin.site.register(Delivery_company)
admin.site.register(Delivery)
admin.site.register(Pay)
admin.site.register(Complaint_type)
admin.site.register(Complaint)
admin.site.register(Re_complaint)
admin.site.register(Return_type)
admin.site.register(Return_service)
admin.site.register(Problem_type)
admin.site.register(Problem_report)
admin.site.register(Re_problem)
admin.site.register(Comment)
admin.site.register(Re_comment)

from . import models

admin.site.register(models.User)
