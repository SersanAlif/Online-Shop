# 🛍️ APFA Modern Shop - E-Commerce Platform

Platform belanja online modern dengan tampilan menarik dan fitur lengkap menggunakan Flask.

## ✨ Fitur Utama

- 🏠 **Homepage** dengan hero section menarik dan statistik
- 📦 **Product Catalog** dengan filter kategori dan sorting
- 🔍 **Search Functionality** dengan suggestions
- 🛒 **Shopping Cart** dengan quantity management
- 💳 **Checkout Process** dengan multiple payment methods
- ✅ **Order Success** page dengan order tracking
- 📱 **Responsive Design** untuk semua device
- 🎨 **Modern UI/UX** dengan gradient dan animations

## 🚀 Cara Menjalankan

### 1. Persiapan

Pastikan Python 3.7+ sudah terinstall:
```bash
python --version
```

### 2. Install Flask

```bash
pip install flask
```

### 3. Struktur Folder

Buat struktur folder seperti ini:
```
modern-shop/
├── app.py
├── templates/
│   ├── shop_index.html
│   ├── shop_products.html
│   ├── shop_detail.html
│   ├── shop_cart.html
│   ├── shop_checkout.html
│   ├── shop_order_success.html
│   └── shop_search.html
├── static/
│   ├── css/
│   │   └── shop_style.css
│   └── js/
│       └── shop_script.js
```

### 4. Jalankan Aplikasi

```bash
python app.py
```

Aplikasi akan berjalan di: **http://127.0.0.1:8080**

## 📂 File-file yang Dibutuhkan

### Backend
- **app.py** - Main Flask application

### Templates (HTML)
- **shop_index.html** - Homepage
- **shop_products.html** - Product listing page
- **shop_detail.html** - Product detail page
- **shop_cart.html** - Shopping cart page
- **shop_checkout.html** - Checkout page
- **shop_order_success.html** - Order confirmation page
- **shop_search.html** - Search results page

### Static Files
- **shop_style.css** - Main stylesheet
- **shop_script.js** - JavaScript functionality

## 🎯 Halaman-halaman Utama

1. **Home** (`/`)
   - Hero section dengan animated cards
   - Browse categories
   - Featured products
   - New arrivals

2. **Products** (`/products`)
   - Filter by category
   - Sort options
   - Product grid view

3. **Product Detail** (`/product/<id>`)
   - Product gallery
   - Detailed information
   - Add to cart
   - Related products

4. **Cart** (`/cart`)
   - Cart items management
   - Quantity adjustment
   - Order summary

5. **Checkout** (`/checkout`)
   - Shipping information form
   - Payment method selection
   - Order summary

6. **Order Success** (`/order_success/<id>`)
   - Order confirmation
   - Order details
   - Next steps information

7. **Search** (`/search?q=`)
   - Search results
   - Popular searches
   - Category suggestions

## 🛠️ Teknologi yang Digunakan

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Font Awesome 6.4.0
- **Design**: Modern gradient UI with glassmorphism
- **State Management**: Flask sessions

## 📦 Data Sample

Aplikasi sudah dilengkapi dengan sample data:
- 6 produk demo
- 6 kategori
- Sample orders dan customers

## 🎨 Design Features

- Modern gradient backgrounds
- Smooth animations dan transitions
- Hover effects
- Responsive grid layouts
- Card-based design
- Flash notifications
- Loading indicators

## 🔒 Session Management

- Shopping cart disimpan di session
- Persistent across pages
- Auto-clear setelah checkout

## 💡 Tips Penggunaan

1. **Testing Cart**: Tambahkan produk ke cart dari berbagai halaman
2. **Search**: Coba search dengan keyword seperti "laptop", "kaos", dll
3. **Checkout**: Isi form dengan data valid untuk testing
4. **Categories**: Filter produk berdasarkan kategori

## 🐛 Troubleshooting

**Port sudah digunakan?**
```python
# Ubah port di app.py:
app.run(debug=True, host='127.0.0.1', port=5000)  # Ganti 5000
```

**Template not found?**
- Pastikan semua file HTML ada di folder `templates/`
- Check nama file sesuai dengan yang di routing

**Static files tidak load?**
- Pastikan folder `static/css/` dan `static/js/` ada
- Refresh browser dengan Ctrl+F5

**Gambar tidak muncul?**
- Aplikasi menggunakan Unsplash CDN
- Pastikan koneksi internet aktif

## 📝 Customization

### Ubah Warna
Edit di `shop_style.css`:
```css
:root {
    --primary: #6366f1;  /* Ubah warna primary */
    --secondary: #ec4899;  /* Ubah warna secondary */
}
```

### Tambah Produk
Edit di `app.py` function `init_sample_data()`:
```python
products.append({
    'id': 7,
    'name': 'Produk Baru',
    'category': 'Fashion',
    'price': 200000,
    # ... dst
})
```

### Ubah Logo
Ganti di setiap template:
```html
<div class="logo">
    <i class="fas fa-shopping-bag"></i>
    <span>NAMA TOKO ANDA</span>
</div>
```

## 🚀 Development Roadmap

Future features yang bisa ditambahkan:
- [ ] User authentication & registration
- [ ] Product reviews & ratings
- [ ] Wishlist functionality
- [ ] Order history
- [ ] Admin dashboard
- [ ] Real payment gateway integration
- [ ] Email notifications
- [ ] Product recommendations
- [ ] Advanced filters (price range, rating)
- [ ] Multi-language support

## 📞 Support

Jika ada pertanyaan atau issue:
1. Check dokumentasi di README ini
2. Review kode di app.py untuk logic flow
3. Inspect browser console untuk JavaScript errors
4. Check Flask terminal output untuk backend errors

## 📄 License

Free to use for learning and development purposes.

---

**Happy Shopping! 🛍️✨**

Dibuat dengan ❤️ menggunakan Flask dan Modern Web Technologies