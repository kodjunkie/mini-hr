from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME


def guest_only(func=None, redirect_field_name=REDIRECT_FIELD_NAME, redirect_to='/dashboard'):
    """
    Only anonymous users can request view
    :param func:
    :param redirect_field_name:
    :param redirect_to:
    :return:
    """
    actual_decorator = user_passes_test(
        lambda user: user.is_anonymous,
        login_url=redirect_to,
        redirect_field_name=redirect_field_name
    )
    if func:
        return actual_decorator(func)
    return actual_decorator
