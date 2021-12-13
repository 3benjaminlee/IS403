from django.shortcuts import render
from django.http import HttpResponse
from activitysites.models import activity
# Create your views here.

def indexPageView(request) :
    return render(request, 'activitysites/index.html')


def couplesPageView(request) :

    data = activity.objects.all()

    context = {
        "activity" : data
    }

    return render(request, 'activitysites/couples.html', context)



def editPageView(request, id) :

    data = activity.objects.get(id=id)

    context = {
        "activity" : data
    }

    return render(request, 'activitysites/editactivity.html', context)

def updateActivityPageView(request) :
    if request.method == "POST" :

        id = request.POST.get("id", False)

        activities = activity.objects.get(id = id)

        activities.name = request.POST['name']
        activities.description = request.POST['description']
        activities.location = request.POST['location']
        activities.rating = request.POST['rating']
        activities.group_size = request.POST['groupsize']

        activities.save()

        return couplesPageView(request)


def deleteActivityPageView(request, id) :
    data = activity.objects.get(id = id)

    data.delete()

    return couplesPageView(request)


def addActivityPageView(request) :
    if request.method == 'POST' :
        activities = activity()

        activities.name = request.POST['name']
        activities.description = request.POST['description']
        activities.location = request.POST['location']
        activities.rating = request.POST['rating']
        activities.group_size = request.POST['groupsize']

        activities.save()

        return couplesPageView(request)
    else :
        return render(request, 'activitysites/addActivity.html')
