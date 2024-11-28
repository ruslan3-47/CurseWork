menu = [{'title': "Главная страница", 'url': "mainpage"},
        {'title': "Номера", 'url': "rooms"},
        {'title': "Программы", 'url': "programs"},
        {'title': "О нас", 'url': "about"},
        {'title':"Питание", 'url': "food" },
        {'title': "Зарегистрировать", 'url': "addusers"}
        ]
title = 'Новая Заря'

class DataMixin:
    def get_user_context(self,**kwargs):
        context = kwargs
        context['menu'] = menu
        context['title']=title
        return context