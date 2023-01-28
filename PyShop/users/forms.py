from django.contrib.auth.forms import UserCreationForm as _UserCreationForm
from django.contrib.auth import get_user_model
from users.models import User

User = get_user_model()


class UserCreationForm(_UserCreationForm):
    class Meta(_UserCreationForm.Meta):
        model = User

