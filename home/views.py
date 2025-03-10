from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home_view(request: HttpRequest) -> HttpResponse:
    """Render the home page.

    This view renders the home page template.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTTP response.
    """
    return render(request, "home/home.html")


def about_view(request: HttpRequest) -> HttpResponse:
    """Render the about page.

    This view renders the about page template.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTTP response.
    """
    return render(request, "home/about.html")


def contact_view(request: HttpRequest) -> HttpResponse:
    """Render the contact page.

    This view renders the contact page template.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTTP response.
    """
    return render(request, "home/contact.html")


def post_view(request: HttpRequest, id: int) -> HttpResponse:
    """Render the post page.

    This view renders the post page template.

    Args:
        request: The HTTP request object.
        id: The ID of the post.

    Returns:
        A rendered HTTP response.
    """
    return render(request, "home/post.html", {"post_id": id})


def profile_view(request: HttpRequest, username: str) -> HttpResponse:
    """Render the profile page.

    This view renders the profile page template.

    Args:
        request: The HTTP request object.
        username: The username of the profile.

    Returns:
        A rendered HTTP response.
    """
    return render(request, "home/profile.html", {"username": username})


def event_view(request: HttpRequest, year: int, month: int, day: int) -> HttpResponse:
    """Render the event page.

    This view renders the event page template.

    Args:
        request: The HTTP request object.
        year: The year of the event.
        month: The month of the event.
        day: The day of the event.

    Returns:
        A rendered HTTP response.
    """
    return render(
        request, "home/event.html", {"year": year, "month": month, "day": day}
    )
