from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import ArgumentForm
from ..models import Argument


@login_required(login_url='common:login')
def argument_create(request):
    if request.method == "POST":
        form = ArgumentForm(request.POST)
        if form.is_valid():
            argument = form.save(commit=False)
            argument.author = request.user
            argument.create_date = timezone.now()
            argument.save()
            return redirect('intelin:index')
    else:
        form = ArgumentForm()
    context = {'form': form}
    return render(request, 'intelin/argument_form.html', context)

@login_required(login_url='common:login')
def argument_modify(request, argument_id):
    argument = get_object_or_404(Argument, pk=argument_id)
    if request.user != argument.author:
        messages.error(request, '아쎄이! 자네에겐 수정의 권한이 없다.') #Non-Field Error
        return redirect('intelin:detail', argument_id=argument.id)
    if request.method == 'POST':
        form = ArgumentForm(request.POST, instance=argument)
        if form.is_valid():
            argument = form.save(commit=False)
            argument.modify_date = timezone.now()
            argument.save()
            return redirect('intelin:detail', argument_id=argument.id)
    else:
        form = ArgumentForm(instance=argument)
    context = {'form': form}
    return render(request, 'intelin/argument_form.html', context)

@login_required(login_url='common:login')
def argument_delete(request, argument_id):
    argument = get_object_or_404(Argument, pk=argument_id)
    if request.user != argument.author:
        messages.error(request, '아쎄이! 자네에겐 기열시킬 권한이 없다')
        return redirect('intelin:detail', argument_id=argument.id)
    argument.delete()
    return redirect('intelin:index')

@login_required(login_url='common:login')
def argument_vote(request, argument_id):
    argument = get_object_or_404(Argument, pk= argument_id)
    if request.user == argument.author:
        messages.error(request, '기열!!! 스스로의 주장에 기합을 주려 하는가!')
    else:
        argument.voter.add(request.user)
    return redirect('intelin:detail', argument_id=argument.id)