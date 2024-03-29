# Generated by Django 4.1.4 on 2023-01-28 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_productcategory_remove_product_short_description_and_more"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductInBasket",
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
                (
                    "session_key",
                    models.CharField(
                        blank=True, default=None, max_length=128, null=True
                    ),
                ),
                ("nmb", models.IntegerField(default=1)),
                (
                    "price_per_item",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "total_price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар в корзині",
                "verbose_name_plural": "Товари в корзині",
            },
        ),
    ]
