from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from referrals.models import Referral


def index(request):
    context = RequestContext(request)
    referrals_list = Referral.objects.order_by('-datetime')[:5]
    context_dict = {'referrals': referrals_list}

    return render_to_response('referrals/index.html', context_dict, context)