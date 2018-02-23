# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import render
from django.views import generic
from epoch import * 
import re
# Create your views here.
def epoch_convertor(request):
    data = {}
    if 'timestamp' in request.GET:
        data["timestamp"] = request.GET["timestamp"]
        dt = datetime.datetime.fromtimestamp(float(data['timestamp']))
        data["human_readable_date"] = dt
        return render(request, 'epoch.html', data)
    elif 'date' in request.GET:
        data["date"] = request.GET["date"] 
        datetime_spliter = re.split("T", data["date"])
        date_spliter = re.split("-", datetime_spliter[0])
        time_spliter = re.split(":", datetime_spliter[1])
        datetime_list = date_spliter + time_spliter
        date_info_list = [eval(x) for x in datetime_list] 
        time_stamp = datetime.datetime(*date_info_list).strftime('%s')
        data['time_stamp'] =  time_stamp
        return render(request, 'epoch.html', data)
    
    else:
        return render(request, 'base_template.html')
