from email.policy import default
import re
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tasklist(BaseModel):
    is_done = models.BooleanField(default=False)
    description = models.TextField(default='')

    @property
    def get_description(self) -> str:
        return self.description
    @property
    def get_done(self) -> bool:
        return 'checked' if self.is_done else ''
