# Generated by Django 4.2 on 2023-04-24 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_seller_shopavatar"),
    ]

    operations = [
        migrations.CreateModel(
            name="SellerDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("bannerImage", models.ImageField(upload_to="")),
                (
                    "sellerId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seller_detail",
                        to="users.seller",
                    ),
                ),
            ],
            options={
                "verbose_name": "Seller Details",
                "verbose_name_plural": "Seller Details",
            },
        ),
    ]
