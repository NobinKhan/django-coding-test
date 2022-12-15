from django import template

register = template.Library()


@register.filter
def start(currentPageNumber, perPageItem):
    if perPageItem == 2:
        return currentPageNumber + (currentPageNumber - 1)


@register.filter
def end(currentPageNumber, perPageItem):
    if perPageItem == 2:
        return currentPageNumber * perPageItem


#  p=1, c=2
#  p=2, c=4
#  p=3, c=6
#  p=4, c=8
#  p=5, c=10