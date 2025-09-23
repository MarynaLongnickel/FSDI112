from django.db import migrations

def populate_status(apps, schemaeditor):
    entries = {
        "published": "A post available for all to view.",
        "draft": "A post only visible to the author.",
        "archived": "An older post visible only to the logged user.",
    }
    Status = apps.get_model("posts", "Status")
    for k, v in entries.items():
        status_obj = Status(name=k, description=v)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_status'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]
    