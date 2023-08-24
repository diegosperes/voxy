from django.views import View
from django.shortcuts import render

from words.form import WordForm
from words.domain.words import find_words_indexes, EnglishLanguage


class WordsView(View):
    async def get(self, request):
        form = WordForm()
        return render(request, "words-form.html", {"form": form})

    async def post(self, request):
        form = WordForm(request.POST)
        context = {"words": set(), "text": []}

        if form.is_valid():
            context["text"] = form.cleaned_data["text"].split()
            context["words"] = find_words_indexes(context["text"], EnglishLanguage)

        return render(request, "words-result.html", context=context)
