
from django.urls import path
from tax_app.views import calculate_tax
from django.http import HttpResponseRedirect
urlpatterns = [
      path('', lambda request: HttpResponseRedirect('calculate_tax/')),  # ルートにアクセスした場合にリダイレクト
    path('calculate_tax/', calculate_tax, name='calculate_tax'),
]
