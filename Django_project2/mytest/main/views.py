from django.shortcuts import render,get_object_or_404,redirect,reverse
from .models import Customer
from django.db.models import Q
from .forms import CustomerForm

# Create your views here.

def index_view(request):
    search = request.GET.get('q', None)
    customers = Customer.objects.all()
    if search:
        customers = customers.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(phon_number__icontains=search) |
            Q(addres__icontains=search)
        )
    return render(
        request,
        'main/index.html',
        {'customers':customers}
    )

def customer_add_view(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            customer = Customer(**form.cleaned_data)
            customer.save()
            return redirect(reverse('index-url'))
    return render(request,'main/customer_add.html',{'form':form})


def customer_delete_view(request, customer_id):
    if request.method == 'POST':
        customer = get_object_or_404(Customer,id=customer_id)
        customer.delete()
    return redirect(reverse('index-url'))


def customer_edit_view(request,customer_id):
    customer = get_object_or_404(Customer,id=customer_id)
    if request.method == 'POST':

        for key,value in request.POST.items():
            setattr(customer,key,value)
        customer.save()
        return redirect(reverse('index-url'))

    return render(
        request,
        'main/customer_edit.html',
        {'customer': customer}
    )