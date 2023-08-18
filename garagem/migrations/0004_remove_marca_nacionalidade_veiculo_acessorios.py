# Generated by Django 4.2.4 on 2023-08-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0003_remove_veiculo_capa_veiculo_capa"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="marca",
            name="nacionalidade",
        ),
        migrations.AddField(
            model_name="veiculo",
            name="acessorios",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                related_name="veiculos",
                to="garagem.acessorio",
            ),
        ),
    ]
