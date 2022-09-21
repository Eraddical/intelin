from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Argument


def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    argument_list = Argument.objects.order_by('-create_date')
    if kw:
        argument_list = argument_list.filter(
            Q(subject__icontains=kw)  |
            Q(content__icontains=kw)  |
            Q(refute__content__icontains=kw)  |
            Q(author__username__icontains=kw)  |
            Q(refute__author__username__icontains=kw)
        ).distinct()
    paginator = Paginator(argument_list, 10)
    page_obj = paginator.get_page(page)
    context = {'argument_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'intelin/argument_list.html', context)

def detail(request, argument_id):
    argument = get_object_or_404(Argument, pk=argument_id)
    context = {'argument': argument}
    return render(request, 'intelin/argument_detail.html', context)