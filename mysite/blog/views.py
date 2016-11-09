from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.
def post_list(request):
    return render(request, 'blog/shablon.html', {})
data = {
    'f': [
        {'id': 1, 'text': 'ololo'},
        {'id': 2, 'text': 'ololo2'},
        {'id': 3, 'text': 'cheeeekii breeki'},
    ]
}
content=[
		{
			'id' : 1,
			'author' : "Путник",
			'text' : "Нет, я не видел Оазис",
			'info' : "Очередной встречный путник. Ничем не отличается от сотен других встречных. Иногда может расспалагать ценной информацией, но не факт что захочет делиться ею за просто так"
		},
		{
			'id' : 2,
			'author' : "Сторож",
			'text' : "Проходи не задерживайся",
			'info' : "Злющий черт. Зарплата пропивается в том же баре который охраняет - можно сказать, работает за еду. Обладает скудным набором фраз по типу 'Проходи, не задерживайся' и 'Тебе сюда нельзя'"
		},
		{
			'id' : 3,
			'author' : "Бандит",
			'text' : "A nyy, cheeeekii breeki!",
			'info' : "А кого еще вы ожидали повстречать в Зоне Отчуждения, и каких повадок ждали от человека с именем Вася Кабан?"
		}
	]
def books(request):
    return render(request, 'blog/spisok.html', {"Text":content}, {})


def govorit(request, pk):
	post = content[int(pk)-1]
	return render(request, 'blog/info.html', {"Text":post})

#def govorit(request, pk):

 #   return render(request, 'blog/info.html',{'post': post})