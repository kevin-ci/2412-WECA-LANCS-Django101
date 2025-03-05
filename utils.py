from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect


def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, "You need to be an admin to access that page.")
            return redirect("homepage")
        return view_func(request, *args, **kwargs)
    return _wrapped_view