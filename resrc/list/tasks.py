from celery import task

@task()
def regenerate_list(alist_pk):
    print "Go."
    from django.shortcuts import get_object_or_404
    alist = get_object_or_404(List, pk=alist_pk)
    from resrc.utils.templatetags.emarkdown import listmarkdown
    alist.html_content = listmarkdown(alist.md_content, alist)
    alist.save()
    print "Done."
    return True
