import csv

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import (IssueForm, RecieveForm, StockCreateForm, StockSearchForm,
                    StockUpdateForm , ReOrderLevelForm)
from .models import Stock

# Create your views here.

# def upload(request):
#     if request.method=='POST':
#         stock.resource=StockResource()



def home(request):
    title='welcome '
    context={
        "title":title
    }
    return render(request , 'home.html' , context)





def list_items(request):
    header='List of list item'
    queryset=Stock.objects.all()
    form=StockSearchForm(request.POST or None)
    context={
        'header':header,
        "queryset":queryset,
        'form':form

        }

    if request.method=='POST':
        # queryset=Stock.objects.filter(category__icontains=form['category'].value(),
        item_name__icontains=form['item_name'].value()

        if form['export_to_csv'].value()==True:
            response=HttpResponse(content_type='text/csv')
            response['Content-Disposition']='atachement filename="list of stock"'
            writer=csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME' , 'QUANTITY'])
            instance=queryset
            for stock in instance:
                writer.writerow([stock.category , stock.item_name ,stock.quantity])
            return response
        
    context={
        'header':header,
        "queryset":queryset,
        'form':form

        }

    return render(request , 'list_items.html' , context)



def add_items(request):
    form=StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request , 'Successflly  Added')

        return redirect('/list_items')
    context={
        'form':form,
        'title' : "Add item"

    }
    return render(request ,'add_items.html' , context)





def update_items(request , pk):
    queryset=Stock.objects.get(id=pk)
    form=StockUpdateForm(instance=queryset)
    if request.method=="POST":
        form=StockUpdateForm(request.POST , instane=queryset)
        if form.is_valid():
            form.save()
            messages.success(request , 'Successflly  Updated')

            return redirect('/list_item')
    context={
        "form":form
    }
    return render(request , 'add_items.html' ,context)


def delete_items(request , pk):
    queryset=Stock.objects.get(id=pk)
    if request.method=="POST":
            queryset.delete()
            messages.success(request , 'Successflly Deleted')
            return redirect('/list_item')
    
    return render(request , 'add_items.html')



def stock_detail(request , pk):
    queryset=Stock.objects.get(id=pk)
    context={
        "title":queryset.item_name,
        'queryset':queryset,

    }
  
    return render(request , 'stock_detail.html' ,context)



def issue_item(request, pk):
    queryset=Stock.objects.get(id=pk)
    form=IssueForm(request.POST or None , instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.quantity=instance.issue.quantity
        instance.issue_by=str(request.user)
        messages.success(request, "Isuued Successfully ." + str(instance.quantity) + ' ' + str(instance.item_name) + 'now left in store' )
        instance.save()
        return redirect('/stock_detail/'+str(instance.id))

    context={
        'title': "Issue" + str(queryset.item_name),
        "queryset": queryset,
        'form':form,
        'username': 'Issue by' + str(request.user),
    }

    return render(request, 'add_items.html' , context)



def recieve_item(request , pk):
    queryset=Stock.objects.get(id=pk)
    form=RecieveForm(request.POST or None , instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.quantity += instance.recieve_quantity
        instance.save()
        messages.success(request, "Isuued Successfully ." + str(instance.quantity) + ' ' + str(instance.item_name) + 'now left in store' )
        return redirect('/stock_details/' + str(instance.id))
    context={
        'title':'Recieve ' + str(queryset.item_name),
        'instance':queryset,
        'form':form,
        "username":'Recieve By :' + str(request.user),
    }
    return render(request , 'add_items.html' , context)


def reorder_level(request , pk):
    queryset=Stock.objects.get(id=pk)
    form=ReOrderLevelForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, 'ReOrder level for '+ str(instance.item_name)+ 'is updated to' + str(instance.reorder_level))

        return redirect('/list_items')
    context={
        'instance':queryset,
        'form':form
    }
    return  render(request ,'add_items.html', context)