from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import RefuteForm
from ..models import Argument, Refute

@login_required(login_url='common:login')
def refute_create(request, argument_id):
    argument = get_object_or_404(Argument, pk=argument_id)
    if request.method == "POST":
        form = RefuteForm(request.POST)
        if form.is_valid():
            refute = form.save(commit=False)
            refute.author = request.user
            refute.create_date = timezone.now()
            refute.argument = argument
            refute.save()
            return redirect('{}#refute_{}'.format(
                resolve_url('intelin:detail', argument_id=argument.id), refute.id))
    else:
        form = RefuteForm()
    context = {'argument': argument, 'form': form}
    return render(request, 'intelin/argument_detail.html', context)


@login_required(login_url='common:login')
def refute_modify(request, refute_id):
    refute = get_object_or_404(Refute, pk=refute_id)
    if request.user != refute.author:
        messages.error(request, '아쎄이! 자네에겐 수정의 권한이 없다.') #Non-Field Error
        return redirect('intelin:detail', argument_id=refute.argument.id)
    if request.method == 'POST':
        form = RefuteForm(request.POST, instance=refute)
        if form.is_valid():
            refute = form.save(commit=False)
            refute.modify_date = timezone.now()
            refute.save()
            return redirect('{}#refute_{}'.format(resolve_url('intelin:detail', argument_id=refute.argument.id), refute.id))
    else:
        form = RefuteForm(instance=refute)
    context = {'refute': refute, 'form': form}
    return render(request, 'intelin/refute_form.html', context)

@login_required(login_url='common:login')
def refute_delete(request, refute_id):
    refute = get_object_or_404(Refute, pk=refute_id)
    if request.user != refute.author:
        messages.error(request, '아쎄이! 자네에겐 기열의 권한이 없다')
    else:
        refute.delete()
    return redirect('intelin:detail', argument_id=refute.argument.id)

@login_required(login_url='common:login')
def refute_vote(request, refute_id):
    refute = get_object_or_404(Refute, pk=refute_id)
    if request.user == refute.author:
        messages.error(request, '기열!!! 스스로의 반박에 기합을 주려 하는가!')
    else:
        refute.voter.add(request.user)
    return redirect('{}#answer_{}'.format(resolve_url('intelin:detail', argument_id=refute.argument.id), refute.id))

