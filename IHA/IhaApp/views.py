from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .decorators import *
from .forms import UserForm, IhaCreateForm, IhaPropertyCreateForm, IhaProductUpdateForm, IhaPropertyUpdateForm
from .models import iha_product, iha_property
from .filters import IhaPropertyFilter


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        rememberMe = request.POST.get("remember")  # None or True -> ne kadar calisiyor bilmiyorum

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            if rememberMe is None:
                request.session.set_expiry(0)

            if request.GET.get('next') is not None:
                return redirect(request.GET.__getitem__('next'))
            return redirect('dashboard')
        messages.error(request, "Oturum sağlanamadı. Tekrar Deneyiniz")

    context = {}
    return render(request, 'pages-login.html', context=context)


def registerPage(request):
    userForm = UserForm()

    if request.method == 'POST':
        term = request.POST.get("terms")
        if term is None:
            messages.error(request, 'Şartlar ve koşullar kabul edilmelidir.')
        else:
            userForm = UserForm(request.POST)
            if userForm.is_valid():
                user_name = userForm.cleaned_data.get("username")
                userForm.save()

                messages.success(request, user_name + ' başarıyla oluşturuldu.')
                return redirect('index')

        messages.error(request, "Kullanıcı oluşturulamadı.")

    context = {'userForm': userForm}
    return render(request, 'pages-register.html', context=context)


def logoutPage(request):
    logout(request)
    return redirect("index")


@login_required(login_url='/')
def dashboard(request):
    all_iha = iha_property.objects.all()
    iha_property_filter = IhaPropertyFilter(request.GET, queryset=all_iha)
    all_iha = iha_property_filter.qs
    context = {'all_iha': all_iha, 'iha_property_filter': iha_property_filter}
    return render(request, 'pages-dashboard.html', context=context)


@login_required(login_url='/')
def create_iha(request):
    iha_form = IhaCreateForm()
    property_form = IhaPropertyCreateForm()

    if request.method == 'POST':
        iha_form = IhaCreateForm(request.POST)
        property_form = IhaPropertyCreateForm(request.POST, request.FILES)
        if iha_form.is_valid() and property_form.is_valid():
            i = iha_form.save()
            property_form.instance.iha_Product = i
            property_form.save()
            return redirect('dashboard')

        messages.error(request, "HATA iha oluşturulamadı.")
    context = {'iha_form': iha_form, 'property_form': property_form}
    return render(request, 'pages-iha-create.html', context=context)


@login_required(login_url='/')
def update_iha(request, iha_pk):
    try:
        iha_elem = iha_product.objects.get(pk=iha_pk)
    except iha_product.DoesNotExist:
        return redirect('404')
    update_iha_form = IhaProductUpdateForm(instance=iha_elem)
    update_property_form = IhaPropertyUpdateForm(instance=iha_elem.iha_property)
    if request.method == 'POST':
        update_iha_form = IhaProductUpdateForm(request.POST, request.FILES, instance=iha_elem)
        update_property_form = IhaPropertyUpdateForm(request.POST, request.FILES, instance=iha_elem.iha_property)
        if update_property_form.is_valid() and update_iha_form.is_valid():
            update_iha_form.save()
            update_property_form.save()
            return redirect('dashboard')

        messages.error(request, "HATA Iha güncellenemedi.")

    context = {'update_iha_form': update_iha_form, 'update_property_form': update_property_form}
    return render(request, 'pages-iha-update.html', context=context)


@login_required(login_url='/')
def delete_iha(request, iha_pk):
    try:
        iha_elem = iha_product.objects.get(pk=iha_pk)
    except iha_product.DoesNotExist:
        return redirect('404')
    if request.method == 'POST':
        iha_elem.delete()
        return redirect('dashboard')
    context = {'iha_elem': iha_elem}
    return render(request, 'pages-iha-delete.html', context=context)


def error_page_404(request):
    return render(request, "pages-error-404.html")
