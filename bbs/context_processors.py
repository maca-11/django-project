from .forms import SearchForm       # forms.pyからsearchFormクラスをインポート

def search_form(request):
    return {'searchform':SearchForm()}


# 各ビューに同じ記述を追記しなければならない