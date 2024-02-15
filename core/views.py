from django.shortcuts import render, redirect
from .models import Account, Destination
from .forms import AddAccountForm, AddDestinationForm
from django.contrib import messages

# Create your views here.
def accounts(request):
	account_list = Account.objects.all()
	return render(request, 'accounts.html', {'account_list': account_list})


def add_account(request):
	form = AddAccountForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			add_record = form.save()
			messages.success(request, "Account Added...")
			return redirect('accounts')
		else:
			return render(request, "add_account.html", {"form": form})

	return render(request, 'add_account.html', {'form':form})

def view_account(request, pk):
	# Look Up Records
	account_details = Account.objects.get(account_id=pk)
	return render(request, 'account_details.html', {'account_details':account_details})

def delete_account(request, pk):
	delete_it = Account.objects.get(account_id=pk)
	delete_it.delete()
	messages.success(request, "Account Deleted Successfully...")
	return redirect('accounts')

def update_account(request, pk):
	current_record = Account.objects.get(account_id=pk)
	form = AddAccountForm(request.POST or None, instance=current_record)
	if form.is_valid():
		form.save()
		messages.success(request, "Account Has Been Updated!")
		return redirect('accounts')
	return render(request, 'update_account.html', {'form':form})




def destinations(request):
	destination_list = Destination.objects.all()
	return render(request, 'destinations.html', {'destination_list': destination_list})


def add_destination(request):
	form = AddDestinationForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			add_record = form.save()
			messages.success(request, "Destination Added...")
			return redirect('destinations')
		else:
			return render(request, "add_destination.html", {"form": form})

	return render(request, 'add_destination.html', {'form':form})

def view_destination(request, pk):
	# Look Up Records
	destination_details = Destination.objects.get(id=pk)
	return render(request, 'destination_details.html', {'destination_details':destination_details})

def delete_destination(request, pk):
	delete_it = Destination.objects.get(id=pk)
	delete_it.delete()
	messages.success(request, "Destination Deleted Successfully...")
	return redirect('destinations')

def update_destination(request, pk):
	current_record = Destination.objects.get(id=pk)
	form = AddDestinationForm(request.POST or None, instance=current_record)
	if form.is_valid():
		form.save()
		messages.success(request, "Destination Has Been Updated!")
		return redirect('destinations')
	return render(request, 'update_destination.html', {'form':form})


