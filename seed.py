import os
import django
import uuid

# Django ortamını hazırla
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import User, Store, Category, Product, ProductVariant, Address

def run_seed():
    print("🚀 Veritabanı verileri oluşturuluyor...")

    # 1. Test Kullanıcısı Oluştur
    user, created = User.objects.get_or_create(
        gsm_number="5320000000",
        defaults={
            'name': 'Abdulsamet Kılıç',
            'is_seller': True,
            'is_buyer': True
        }
    )
    if created:
        user.set_password("1234")
        user.save()
        print("— Test kullanıcısı oluşturuldu.")

    # 2. Test Adresi (Checkout'ta hata almamak için kritik)
    Address.objects.get_or_create(
        user=user,
        title="Ev Adresim",
        defaults={
            'full_address': 'Merkez Mahallesi, Atatürk Caddesi No:1923',
            'city': 'İstanbul',
            'district': 'Arnavutköy',
            'is_default': True
        }
    )
    print("— Test adresi eklendi.")

    # 3. Mağaza Oluştur
    store, _ = Store.objects.get_or_create(
        seller=user,
        defaults={
            'name': 'Simurg Teknoloji Mağazası',
            'description': 'En iyi drone ve AI parçaları burada.',
            'is_approved': True
        }
    )
    print("— Mağaza oluşturuldu.")

    # 4. Kategoriler Oluştur
    elektronik, _ = Category.objects.get_or_create(name="Elektronik", slug="elektronik", level=0)
    drone, _ = Category.objects.get_or_create(name="İHA Parçaları", slug="iha-parcalari", parent=elektronik, level=1)
    
    print("— Kategoriler oluşturuldu.")

    # 5. 30 Tane Ürün ve Varyantlarını Oluştur
    for i in range(1, 31):
        product = Product.objects.create(
            store=store,
            category=drone,
            name=f"Drone Pervanesi V{i}",
            description=f"Yüksek performanslı karbon fiber pervane modeli {i}.",
            base_price=150.00 + (i * 5),
            images=["https://picsum.photos/seed/{}/400/400".format(i)]
        )

        # Senin modelindeki ProductVariant alanlarına göre (variant_type ve value):
        ProductVariant.objects.create(
            product=product,
            variant_type="Renk",
            value="Siyah",
            price_diff=0,
            stock=100
        )

    print(f"\n✅ BAŞARILI: 1 Kullanıcı, 1 Adres, 1 Mağaza ve {Product.objects.count()} ürün oluşturuldu!")

if __name__ == "__main__":
    run_seed()