from django.urls import path
from . import views
from catboost import *

model = CatBoostRegressor()
model.load_model('final_model')

urlpatterns = [
    # path('', include('main.urls'))
    path('', views.func, {'model': model}, name='home'),
    path('about/',views.about, name='about')
]
