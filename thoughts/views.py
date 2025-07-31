from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import ThoughtForm
from .models import Thought

@login_required
def create_thought(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ThoughtForm(request.POST)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()
            return JsonResponse({
                'status': 'success',
                'username': request.user.username,
                'content': thought.content,
                'created_at': thought.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'invalid'}, status=400)


# thoughs list view
@login_required
def home(request):
    thoughts = Thought.objects.all()[:20]
    form = ThoughtForm()
    return render(request, 'thoughts/home.html', {'form': form, 'thoughts': thoughts})