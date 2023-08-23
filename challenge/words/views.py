from django.views import View
from django.shortcuts import render

from words.form import AlphaWordForm
from words.domain.alpha_words import find_alpha_words_indexes


class AlphaWordsView(View):

    async def get(self, request):
        form = AlphaWordForm()
        return render(request, "alpha-words-form.html", {"form": form})


    async def post(self, request):
        form = AlphaWordForm(request.POST)
        context = {"alpha_words": set(), "text": []}

        if form.is_valid():
            context["text"] = form.cleaned_data["text"].split()
            context["alpha_words"] = find_alpha_words_indexes(context["text"])

        return render(request, "alpha-words-result.html", context=context)
