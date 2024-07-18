from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


monthly_challenges = {
    "january": "Eat no meat for the month",
    "february": "Walk atleast for 20 mins everyday",
    "march": "Learn Django for 20 mins everyday",
    "april": "Eat no meat for the month",
    "may": "Learn Django for 20 mins everyday",
    "june": "Walk atleast for 20 mins everyday",
    "july": "Learn Django for 20 mins everyday",
    "august": "Walk atleast for 20 mins everyday",
    "september": "Walk atleast for 20 mins everyday",
    "october": "Learn Django for 20 mins everyday",
    "november": "Learn Django for 20 mins everyday",
    "december": "Walk atleast for 20 mins everyday"
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months":months
    })
    # for month in months:
    #     capitalized_month = month.capitalize() 
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        sentence = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": sentence,
            "month_name": month
        })
    except:
        raise Http404()


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        sentence = monthly_challenges[months[month-1]]
        return HttpResponse(sentence)
    except:
        return HttpResponseNotFound("Enter valid month")
