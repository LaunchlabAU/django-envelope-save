# -*- coding: utf-8 -*-

from django.db import models

from model_utils.models import TimeStampedModel


class Contact(TimeStampedModel):
    sender = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=True)


