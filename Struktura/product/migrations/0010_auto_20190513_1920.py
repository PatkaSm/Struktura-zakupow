# Generated by Django 2.0.13 on 2019-05-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20190507_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Owoce', 'Owoce'), ('Warzywa', 'Warzywa'), ('Nabiał', 'Nabiał'), ('Produkty zbożowe', 'Produkty zbrożowe'), ('Tłuszcze i oleje', 'Tłuszcze i oleje'), ('Mięso', 'Mięso'), ('Alkohol', 'Alkohol'), ('Woda', 'Woda'), ('Napoje Słodkie', 'Napoje słodkie'), ('Przekaski Słone', 'Przekąski słone'), ('Cukier i śłodycze', 'Cukier i słodycze'), ('Elektronika', 'Elektronika'), ('Dom i ogród', 'Dom i ogród'), ('Chemia, śreodki czystości', 'Chemia, środki czystośi'), ('Zwierzęta', 'Zwierzęta'), ('Artykuły biurowe', 'Artykuły biurowe'), ('Usługi', 'Usługi'), ('Kultura i rozrywka', 'Kultura i rozrywka'), ('Ubrania', 'Ubrania'), ('Buty i dodatki', 'Buty i dodatki'), ('Uroda', 'Uroda'), ('Zdrowie', 'Zdrowie'), ('Dziecko', 'Dziecko'), ('Motoryzacja', 'Motoryzacja'), ('Pozostałe', 'Pozostałe')], default='Nieokreślony', max_length=100),
        ),
    ]
