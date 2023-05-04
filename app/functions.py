from random import choice
from django.conf import settings
from string import ascii_letters, digits

# NOTE: Best len?
SIZE = 7

AVAILABLE_CHARACTERS = ascii_letters + digits


def create_random_code(characters=AVAILABLE_CHARACTERS):
    return "".join([choice(characters) for _ in range(SIZE)])


def create_shortened_url(model_instance):
    random_code = create_random_code()

    model_class = model_instance.__class__

    qs = model_class.objects.filter(my_url=random_code).exists()
    if qs:
        return create_shortened_url(model_instance)

    return random_code
