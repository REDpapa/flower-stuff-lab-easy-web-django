from django.http import request
from django.shortcuts import render
from django.views.generic import View


# NOTE:app/index.htmlが呼び出されるとからをリターン
# Create your views here.
class IndexView(View):
    def get(self, reqest, **args, **kwargs):
        return render(request, 'app/index.html', {
        })
