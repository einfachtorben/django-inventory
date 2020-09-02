from django.urls import path
from . import views
from inventory.views import (
    PMECreateView,
    PMEListView,
    PMEDetailView,
    ManufacturerCreateView,
    ManufacturerDetailView,
    ManufacturerListView,
    EliminationCreateView,
    EliminationDetailView,
    EliminationListView,
    LocationCreateView,
    LocationDetailView,
    LocationListView,
    ItemCreateView,
    ItemDetailView,
    ItemListView,
)
from iommi import Table
from inventory.models import Item_info


urlpatterns = [
    path('', views.home, name='inventory-home'),
    path('create/pme/', PMECreateView.as_view(), name='pme-create'),
    path('list/pme/', PMEListView.as_view(), name='pme-list'),
    path('list/pme/<int:pk>/', PMEDetailView.as_view(), name='pme-detail'),
    path('create/manufacturer/', ManufacturerCreateView.as_view(),
         name='manufacturer-create'),
    path('list/manufacturer/', ManufacturerListView.as_view(),
         name='manufacturer-list'),
    path('list/manufacturer/<int:pk>/',
         ManufacturerDetailView.as_view(), name='manufacturer-detail'),
    path('create/elimination/', EliminationCreateView.as_view(),
         name='elimination-create'),
    path('list/elimination/', EliminationListView.as_view(),
         name='elimination-list'),
    path('list/elimination/<int:pk>/',
         EliminationDetailView.as_view(), name='elimination-detail'),
    path('create/location/', LocationCreateView.as_view(), name='location-create'),
    path('list/location/', LocationListView.as_view(), name='location-list'),
    path('list/location/<int:pk>/',
         LocationDetailView.as_view(), name='location-detail'),
    path('create/item/', ItemCreateView.as_view(), name='item-create'),
    path('list/item/', ItemListView.as_view(), name='item-list'),
    path('list/item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('list/info/', Table(auto__model=Item_info).as_view(), name='item-list' ),
]
