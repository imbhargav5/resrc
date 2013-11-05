from celery import task

@task()
def regenerate_list(alist_pk):
    from django.shortcuts import get_object_or_404
    from resrc.list.models import List
    alist = get_object_or_404(List, pk=alist_pk)
    from resrc.utils.templatetags.emarkdown import listmarkdown
    alist.html_content = listmarkdown(alist.md_content, alist)
    alist.save()
    return True
