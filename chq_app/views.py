from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, auth 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from .models import master, order, replacement, new_order, boat_ticket
from .forms import chq_form, order_form, replace_form, new_order_form, boat_ticket_form
from django.db.models.functions import Concat
from django.db.models import Value




# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')
        

        if password!=confirm_password:
            try:

                messages.info(request, 'Password and confirm password are not same')
            except:
                print("An exception occurred")
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This user id is already exist')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                return redirect('login')
                
    else:


        return render(request, 'register.html')




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('home')

def entry(request):
    
    form=chq_form()
    if request.method == 'POST':
        form=chq_form(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Cheque details submitted successfully')
            return redirect('entry')
            



    context={'form':form}


    return render(request, 'entry.html', context)


def view_update(request):
    
    
    if request.method == 'POST':
        chq=request.POST['chq']
        details = master.objects.all()

        if chq:
            details=details.filter(chq__icontains = chq)

        context={'details':details}

        
        return render(request, 'view_update.html', context)
        
    
    elif request.method == 'GET':
        return render(request, 'view_update.html')
    else:
        return HttpResponse('An Exception Occured')



def edit(request, id):
    if request.method == 'POST':
        chq_id=master.objects.get(pk=id)
        form = chq_form(request.POST, instance=chq_id)
        if form.is_valid():
            form.save()
            messages.info(request, 'Cheque details updated successfully')
            return render(request, 'edit.html', {
                'form':form,
                'success':True
            })
    else:
        chq_id=master.objects.get(pk=id)
        form=chq_form(instance=chq_id)
        return render(request, 'edit.html',{
            'form':form
        })


def filter_chq(request):
    if request.method == 'POST':
        agent=request.POST['agent']
        status=request.POST['status']
        filter_details=master.objects.all()

        if agent:
            filter_details=filter_details.filter(agent=agent)
        if status:
            filter_details=filter_details.filter(status=status)
        
        context={
            'filter_details':filter_details
        }

        return render(request, 'filter_chq.html', context)
    
    elif request.method =='GET':
        return render(request, 'filter_chq.html')
    else:
        return HttpResponse('An Exception Occureed')

def delete(request, id):
    if request.method == 'POST':
        details = master.objects.get(pk=id)
        details.delete()
        return HttpResponseRedirect(reverse('view_update'))


def delivery_main(request):
    form2=order_form()
    if request.method == 'POST':
        form2=order_form(request.POST)
        if form2.is_valid():
            form2.save()
            messages.info(request,'Delivery details submitted successfully')
            return redirect('delivery_main')

    context={'form2':form2}

    return render(request,'order_main.html',context)



def filter_delivery(request):
    if request.method =='POST':
        date=request.POST['date']
        invoice=request.POST['invoice']
        agent=request.POST['agent']
        deliverysts=request.POST['deliverysts']
        deliveryagt=request.POST['deliveryagt']
        paymentsts=request.POST['paymentsts']

        dlvry=order.objects.all()

        if date:
            dlvry=dlvry.filter(date__icontains =date)
        if invoice:
            dlvry=dlvry.filter(invoice__icontains =invoice)
        if agent:
            dlvry=dlvry.filter(agent=agent)
        if deliverysts:
            dlvry=dlvry.filter(deliverysts=deliverysts)
        if deliveryagt:
            dlvry=dlvry.filter(deliveryagt=deliveryagt)
        if paymentsts:
            dlvry=dlvry.filter(paymentsts=paymentsts)

        context={
            'dlvry':dlvry
        }
        return render(request,'filter_order.html',context)
    
    elif request.method =='GET':
        return render(request, 'filter_order.html')
    else:
        return HttpResponse('An Exception Occureed')


def edit_delivery(request, id):
    if request.method == 'POST':
        delv_id=order.objects.get(pk=id)
        delv_form=order_form(request.POST, instance=delv_id)

        if delv_form.is_valid():
            delv_form.save()
            messages.info(request, 'Delivery details updated successfully')
            return render(request, 'delv_edit.html',{
                'delv_form':delv_form,
                'success':True
            })
    else:
        delv_id=order.objects.get(pk=id)
        delv_form=order_form(instance=delv_id)
        return render(request, 'delv_edit.html',{
            'delv_form':delv_form
        })


def replacement_main(request):
    form_repl=replace_form()
    if request.method == 'POST':
        form_repl=replace_form(request.POST, request.FILES)
        if form_repl.is_valid():
            form_repl.save()
            messages.info(request,'Replacement details submitted successfully')
            return redirect('replacement_main')
    
    context={'form_repl':form_repl}

    return render(request, 'replacement.html',context)



def filter_replacement(request):
    if request.method =='POST':
        date=request.POST['date']
        recv_challan=request.POST['recv_challan']
        client=request.POST['client']
        item=request.POST['item']
        agent=request.POST['agent']
        status=request.POST['status']
        delv_doc=request.POST['delv_doc']
        delv_date=request.POST['delv_date']
        bar=request.POST['bar']

        repl=replacement.objects.all()

        if date:
            repl=repl.filter(date__icontains =date)
        if recv_challan:
            repl=repl.filter(recv_challan__icontains =recv_challan)
        if client:
            repl=repl.filter(client__icontains =client)
        if item:
            repl=repl.filter(item__icontains =item)
        if agent:
            repl=repl.filter(agent=agent)
        if status:
            repl=repl.filter(status=status)
        if delv_doc:
            repl=repl.filter(delv_doc__icontains =delv_doc)
        if delv_date:
           repl=repl.filter(delv_date__icontains =delv_date) 
        if bar:
            repl=repl.filter(bar__icontains=bar)
        
        context={
            'repl':repl
        }
        return render(request, 'replacement_filter.html',context)
    elif request.method =='GET':
        return render(request, 'replacement_filter.html')
    else:
        return HttpResponse('An Exception Occureed')


def edit_replacement(request,id):
    if request.method == 'POST':
        repl_id=replacement.objects.get(pk=id)
        repl_form=replace_form(request.POST, request.FILES, instance=repl_id)
        tttt=replace_form(request.GET, request.FILES, instance=repl_id)

        if repl_form.is_valid():
            repl_form.save()
            messages.info(request, 'Replacement details updated successfully')
            
            return render(request,'replacement_edit.html',{
                'repl_form':repl_form,
                'success':True,
                'tttt':tttt,
            })

    else:
        repl_id=replacement.objects.get(pk=id)
        repl_form=replace_form(instance=repl_id)
        return render(request, 'replacement_edit.html',{
            'repl_form':repl_form
        })

def delete_delivery(request, id):
    if request.method == 'POST':
        dlvry = order.objects.get(pk=id)
        dlvry.delete()
        return HttpResponseRedirect(reverse('filter_delivery'))

def delete_replacement(request, id):
    if request.method == 'POST':
        repl= replacement.objects.get(pk=id)
        repl.delete()
        return HttpResponseRedirect(reverse('filter_replacement'))
    
def note_calculator(request):
    return render(request, 'note_calculator.html')

def video_gallery(request):
    return render(request, 'vid.html')


def cat_boat(request):
    return render(request, 'cat_boat.html')

def b_neckband(request):
    return render(request, 'b_neckband.html')

def b_airdopes(request):
    return render(request, 'b_airdopes.html')

def b_headphone(request):
    return render(request, 'b_headphone.html')

def b_overhead(request):
    return render(request, 'b_overhead.html')

def b_smartwatch(request):
    return render(request, 'b_smartwatch.html')

def b_speaker(request):
    return render(request, 'b_speaker.html')

def b_bar(request):
    return render(request, 'b_bar.html')


def new_order_entry(request):
    form_NewOrder=new_order_form()
    if request.method == 'POST':
        form_NewOrder=new_order_form(request.POST)
        if form_NewOrder.is_valid():
            form_NewOrder.save()
            messages.info(request, 'Order submitted successfully')
            return redirect('new_order_entry')
    
    context={'form_NewOrder':form_NewOrder}

    return render(request, 'new_order.html',context)

def new_order_filter(request):
    if request.method == 'POST':
        agent=request.POST['agent']
        status=request.POST['status']
        shop=request.POST['shop']

        n_order=new_order.objects.all()

        if agent:
            n_order=n_order.filter(agent=agent)
        if status:
            n_order=n_order.filter(status=status)
        if shop:
            n_order=n_order.filter(shop__icontains=shop)

        context={
            'n_order':n_order
        }

        return render(request, 'new_order_filter.html', context)
    
    elif request.method == 'GET':
        return render(request, 'new_order_filter.html')
    else:
        return HttpResponse('An Exception Occureed')
    

def edit_new_order(request, id):
    if request.method == 'POST':
        nOrder_id=new_order.objects.get(pk=id)
        nOrder_form=new_order_form(request.POST, instance=nOrder_id)

        if nOrder_form.is_valid():
            nOrder_form.save()
            messages.info(request, 'Order Updated successfully')
            return render(request, 'new_order_edit.html', {
                'nOrder_form':nOrder_form,
                'success':True
            })
        
    else:
        nOrder_id=new_order.objects.get(pk=id)
        nOrder_form=new_order_form(instance=nOrder_id)
        return render(request, 'new_order_edit.html',{
            'nOrder_form':nOrder_form
        })



def delete_new_order(request, id):
    if request.method == 'POST':
        n_order=new_order.objects.get(pk=id)
        n_order.delete()
        return HttpResponseRedirect(reverse('new_order_filter'))
    


def boat_ticket_entry(request):
    
    form_new_ticket=boat_ticket_form()
    if request.method == 'POST':
        form_new_ticket=boat_ticket_form(request.POST , request.FILES)
        if form_new_ticket.is_valid():
            form_new_ticket.save()
            messages.info(request, 'New Ticket issued successfully')
            return redirect(boat_ticket_entry)
        
    context={'form_new_ticket':form_new_ticket}


    return render(request,'boat_ticket_entry.html',context)

def boat_ticket_view(request):

    return render(request, 'boat_ticket_view.html')


def boat_pricelist(request):
    return render(request, 'boat_pricelist.html')


def voxg_product_pricelist(request):
    return render(request, 'voxg_product_pricelist.html')

def voxg_battery_pricelist(request):
    return render(request, 'voxg_battery_pricelist.html')

def jbl_pricelist(request):
    return render(request, 'jbl_pricelist.html')

def fingers_pricelist(request):
    return render(request, 'fingers_pricelist.html')

def fastrack_pricelist(request):
    return render(request, 'fastrack_pricelist.html')

def agent_activities(request):
    return render(request, 'agent_activities.html')

def special_discount(request):
    return render(request, 'special_discount.html')