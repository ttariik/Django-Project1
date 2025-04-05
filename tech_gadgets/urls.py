from django.urls import path
from .views import start_page_view, single_gadget_int_view, GadgetView, RedirectToGadgetView

urlpatterns = [
    path('', start_page_view, name='start_page'),
    path('<int:gadget_id>/', single_gadget_int_view, name='single_gadget_int'),
    path('gadget/', GadgetView.as_view(), name='gadget_list'),
    path('gadget/<slug:gadget_slug>/', GadgetView.as_view(), name="gadget_slug_url"),
]
