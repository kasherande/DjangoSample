from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .models import Review
from .forms import ReviewForm
# Create your views here.


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews/review.html", {
#             "form": form
#         })

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = int(review_id)
        print(request.session["favorite_review"])
        return HttpResponseRedirect("/reviews/" + review_id)


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         print(form)
#         form.save()
#         return super().form_valid(form)
    
    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

class ThankYouView(TemplateView):
    # def get(self, request):
    #     return render(request, "reviews/thank_you.html", {
    #         "has_error": False,
    #     })
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!" 
        return context
    
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query= super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data
        

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    # context_object_name = "review"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = context['object']
        # loaded_review = self
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = (favorite_id == loaded_review.id)
        return context
    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=reviews_id)
    #     context["review"] = selected_review
    #     return context
    