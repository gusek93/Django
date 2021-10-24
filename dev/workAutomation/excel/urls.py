from . import views
from django.urls import path

app_name = "excel"

urlpatterns = [
    path("", views.uploadFile, name="uploadFile"),
    path("downloadPayment/", views.downloadPayment, name="downloadPayment"),
    path("downloadTaxfree/", views.downloadTaxfree, name="downloadTaxfree"),
    path("payment/", views.transPayment, name="payment"),
    path("taxfree/", views.transTaxfree, name="taxfree"),
    #ath("employee/", views.transPayment, name="employee"),
]