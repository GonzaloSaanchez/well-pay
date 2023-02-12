import decimal

from django.shortcuts import render
from .models import Account, Transfer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def account_details(request):
    username = request.user.username
    user_account = Account.objects.get(email=username)
    return render(request, 'user_details.html', {'user': user_account})

@login_required
def transfer(request):
    if request.method == "POST":
        username = request.user.username
        origin_account = Account.objects.get(email=username)
        data = request.POST

        transfer = generate_transfer_data(request, data, origin_account)
        if not isinstance(transfer, Transfer):
            return transfer
        else:
            transfer.save()
            update_users_balances(transfer)

    return render(request, 'transfer.html')

def handler400(request, exception):
    return render(request, 'error.html', context={'error': "Bad request"}, status=400)

def handler404(request, exception):
    return render(request, 'error.html', context={'error': "Path does not exist"}, status=404)

def handler403(request, exception):
    return render(request, 'error.html', context={{'error': "Not authorized"}}, status=403)

def handler500(request):
    return render(request, 'error.html', context={'error': "There was an unexpected error"}, status=500)

def generate_transfer_data(request, data, origin_account):
    destination_account_email = data.get('destination_account_email')
    if not Account.objects.filter(email=destination_account_email).exists():
        messages.error(request, 'Destination account does not exist')
        return redirect('Transfer')
    else:
        destination_account = Account.objects.get(email=destination_account_email)

        type = data.get('transfer_type')
        currency = data.get('transfer_currency')

        amount = decimal.Decimal(data.get('transfer_amount'))
        fees = decimal.Decimal('0.01') * decimal.Decimal(amount)
        if amount < 0.1 or amount + fees > origin_account.balance:
            messages.error(request, f'Transfer amount should be more than 0 and should '
                                    f'not exceed your account limit of: {origin_account.balance} ')
            return redirect('Transfer')
        else:
            reference = data.get('transfer_reference')

            return Transfer(origin_account=origin_account,
                            destination_account=destination_account,
                            type=type,
                            currency=currency,
                            amount=amount,
                            fees=fees,
                            reference=reference)

def update_users_balances(transfer):
    origin_account = transfer.origin_account
    origin_account.balance -= transfer.amount + transfer.fees

    destination_account = transfer.destination_account
    destination_account.balance += transfer.amount

    origin_account.save()
    destination_account.save()