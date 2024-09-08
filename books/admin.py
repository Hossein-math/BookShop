from django.contrib import admin

from books.models import Book, Comment

class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0


class BookAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

admin.site.register(Book, BookAdmin)
admin.site.register(Comment)