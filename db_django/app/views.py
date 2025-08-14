from django.shortcuts import get_object_or_404, render

from .models import Note, UserProfile


def note_list(request):
    template_name = 'note_list.html'
    notes = (
        Note.objects
        .select_related('author', 'status')
        .prefetch_related('categories')
        .all()
    )
    context = {
        'notes': notes,
    }
    return render(request, template_name, context)


def note_detail(request, note_id):
    template_name = 'note_detail.html'
    note = get_object_or_404(Note, id=note_id)
    context = {
        'note': note,
    }
    return render(request, template_name, context)


def user_detail(request, user_id):
    template_name = 'user_detail.html'
    user_profile = get_object_or_404(UserProfile, user__id=user_id)
    context = {
        'user_profile': user_profile,
    }
    return render(request, template_name, context)


def users_list(request):
    template_name = 'users_list.html'
    users = (
        UserProfile.objects.select_related('user')
    )
    context = {
        'users': users,
    }
    return render(request, template_name, context)
