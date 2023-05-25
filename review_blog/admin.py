from django.contrib import admin
from .models import Blog, Review, Comment, NLPReviewStored

admin.site.register(Blog)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(NLPReviewStored)