from django.shortcuts import redirect

# if user authenticated, redirect to dashboard
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)

    return wrapper_func
