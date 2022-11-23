from django.shortcuts import render, redirect
from polls.forms import VendorCategoryForm
from polls.forms import VendorForm
from polls.models import VendorCategory
from polls.models import Vendor


# Create your views here.
def show_all(request):
    vendor_categories = VendorCategory.objects.all()
    vendors = Vendor.objects.all()
    return render(request, 'show.html', {'vendor_categories': vendor_categories, 'vendors': vendors})


def show_filtered(request, vendor_category):
    vendor_categories = VendorCategory.objects.all()
    vendors = Vendor.objects.filter(vendorCategory=vendor_category).all()
    return render(request, 'show.html', {
        'vendor_categories': vendor_categories,
        'vendors': vendors,
        "filtered_by": vendor_category
    })


def add_vendor_category(request):
    if request.method == "POST":
        form = VendorCategoryForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("/show")


def update_vendor_category(request, vendor_category):
    vendor_category = VendorCategory.objects.get(vendorCategory=vendor_category)
    form = VendorCategoryForm(request.POST, instance=vendor_category)
    if form.is_valid():
        form.save()
    return redirect("/show")


def destroy_vendor_category(request, vendor_category):
    VendorCategory.objects.get(vendorCategory=vendor_category).delete()
    if Vendor.objects.filter(vendorCategory=vendor_category).exists():
        Vendor.objects.get(vendorCategory=vendor_category).delete()
    return redirect("/show")


def add_vendor(request):
    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("/show")


def update_vendor(request, vendor_id):
    vendor = Vendor.objects.get(vendorId=vendor_id)
    form = VendorForm(request.POST, instance=vendor)
    if form.is_valid():
        form.save()
    return redirect("/show")


def destroy_vendor(request, vendor_id):
    vendor = Vendor.objects.get(vendor=vendor_id)
    vendor.delete()
    return redirect("/show")
