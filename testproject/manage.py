import os, sys

if __name__ == "__main__":

    if 'DJANGO_SETTINGS_MODULE' in os.environ:
        del(os.environ['DJANGO_SETTINGS_MODULE'])
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    if len(sys.argv) == 1:
#        sys.argv[1:] = ['syncdb']
        sys.argv[1:] = ['runserver', '--noreload']
#        sys.argv[1:] = ['migrate', 'stock']
#        sys.argv[1:] = ['schemamigration', 'stock', '--auto', '--update']
    execute_from_command_line(sys.argv)
