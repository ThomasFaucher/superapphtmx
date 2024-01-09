from django.db.models import Max
from firsttuto.models import UserTask


def get_max_order(user):
    user_tasks = UserTask.objects.filter(user=user)
    if user_tasks:
        return user_tasks.aggregate(Max("order"))["order__max"] + 1
    else:
        return 1
