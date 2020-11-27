from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from inventory.models import (
    Elimination,
    PME,
    Inventory_location,
    Item,
    Item_info,
    Manufacturer,
    User
)
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)

# Create your views here.


def home(request):
    return render(request, 'inventory/home.html', context={'title': 'Home'})


class PMECreateView(LoginRequiredMixin, CreateView):
    model = PME
    template_name = "inventory/generic-form.html"

    fields = ['name', 'description']


class PMEListView(ListView):
    model = PME
    template_name = "inventory/pme-list.html"
    paginate_by = 10


class PMEDetailView(DetailView):
    model = PME
    template_name = "inventory/generic-detail.html"


class ManufacturerCreateView(LoginRequiredMixin, CreateView):
    model = Manufacturer
    template_name = "inventory/generic-form.html"

    fields = ['name', 'description']


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "inventory/manufacturer-list.html"
    paginate_by = 10


class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = "inventory/generic-detail.html"


class EliminationCreateView(LoginRequiredMixin, CreateView):
    model = Elimination
    template_name = "inventory/generic-form.html"

    fields = ['name', 'description']


class EliminationListView(ListView):
    model = Elimination
    template_name = "inventory/elimination-list.html"
    paginate_by = 10


class EliminationDetailView(DetailView):
    model = Elimination
    template_name = "inventory/generic-detail.html"


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Inventory_location
    template_name = "inventory/generic-form.html"

    fields = ['name', 'description']


class LocationListView(ListView):
    model = Inventory_location
    template_name = "inventory/location-list.html"
    paginate_by = 10


class LocationDetailView(DetailView):
    model = Inventory_location
    template_name = "inventory/generic-detail.html"


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "inventory/generic-form.html"

    fields = ['name', 'description', 'manufacturer',
              'barcode', 'nato_stock_number']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ItemListView(ListView):
    model = Item
    template_name = "inventory/item-list.html"
    paginate_by = 10


class ItemDetailView(DetailView):
    model = Item
    template_name = "inventory/item-detail.html"

def create(request):
    create_views = ['pme-create', 'manufacturer-create', 'elimination-create', 'location-create', 'item-create' ]
    return render(request, 'inventory/create.html', context={'title': 'Create', 'create_views' : create_views})

class ItemInfoCreateView(LoginRequiredMixin, CreateView):
    model = Item_info
    template_name = "inventory/generic-form.html"

    fields = ['item', 'description', 'inventory_location',
              'elimination', 'serialnumber']



class ItemInfoListView(ListView):
    model = Item_info
    template_name = "inventory/item-info-list.html"
    paginate_by = 10


class ItemInfoDetailView(DetailView):
    model = Item_info
    template_name = "inventory/item-info-detail.html"