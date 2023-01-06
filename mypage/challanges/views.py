from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challange_var = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for atleast 20 minutes every day!",
    "march": "Learn django atleast 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "May": "Walk for atleast 20 minutes every day!",
    "june": "Learn django atleast 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for atleast 20 minutes every day!",
    "september": "Learn django atleast 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for atleast 20 minutes every day!",
    # "december": "Learn django atleast 20 minutes every day!",
    "december": None,
}
# Create your views here.

def index(request):
    render_li = ""
    months = list(monthly_challange_var.keys())
    # for month in months:
    #     render_li_path = reverse('monthly-challange', args=[month])
    #     render_li += f"<li><a href='{ render_li_path }'>{ month.capitalize() }</a></li>"
    # render_ul = f"""<ul>{ render_li }</ul>"""
    # return HttpResponse(render_ul)
    return render(request, "challanges/index.html", {
        "months" : months
    })

def monthly_challange_by_number(request, month):
    months = list(monthly_challange_var.keys())
    if month > len(months):
        return HttpResponseNotFound("Invaild month!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challange", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return HttpResponse("Walk for atleast 20 minutes every day!")
    
# def march(request):
#     return HttpResponse("Learn django atleast 20 minutes every day!")

# def monthly_challange(request, month):
#     if month == "january":
#         challange_text = "Eat no meat for the entire month!"
#     elif month == "february":
#         challange_text = "Walk for atleast 20 minutes every day!"
#     elif month == "march":
#         challange_text = "Learn django atleast 20 minutes every day!"
#     else:
#         return HttpResponseNotFound("This minth is not supported!")

#     return HttpResponse(challange_text)

def monthly_challange(request, month):
    try:
        challange_text = monthly_challange_var[month]
        # render_text = f'<h1>{ challange_text }</h1>'
        return render(request, "challanges/challange.html", { "challange_text": challange_text, "challange_month": month })
        # render_text = render_to_string("challanges/challange.html")
        # return HttpResponse(render_text)
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)