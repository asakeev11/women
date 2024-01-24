menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'addpage'},
    {'title': 'Обратная cвязь', 'url_name': 'contact'},
]


class DataMixin:
    title_page = None
    category_selected = None
    extra_context = {}
    paginate_by = 4

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.category_selected is not None:
            self.extra_context['category_selected'] = self.category_selected

    def get_mixin_context(self, context, **kwargs):
        context['category_selected'] = None
        context.update(kwargs)
        return context