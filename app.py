from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from datetime import datetime
import json
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = 'modern-shop-secret-key-2024'

# Data storage
products = []
categories = []
cart_items = {}
orders = []
users = {}
product_id_counter = 1
order_id_counter = 1

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Silakan login terlebih dahulu', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Sample data
def init_sample_data():
    global products, categories, product_id_counter, users
    
    categories = [
        {'id': 1, 'name': 'Fashion', 'icon': 'fa-tshirt', 'color': '#ef4444'},
        {'id': 2, 'name': 'Elektronik', 'icon': 'fa-laptop', 'color': '#3b82f6'},
        {'id': 3, 'name': 'Makanan', 'icon': 'fa-utensils', 'color': '#f59e0b'},
        {'id': 4, 'name': 'Olahraga', 'icon': 'fa-dumbbell', 'color': '#10b981'},
        {'id': 5, 'name': 'Kesehatan', 'icon': 'fa-heart-pulse', 'color': '#ec4899'},
        {'id': 6, 'name': 'Rumah Tangga', 'icon': 'fa-house', 'color': '#8b5cf6'},
    ]
    
    products = [
        {
            'id': 1, 'name': 'Kaos Premium Cotton', 'category': 'Fashion',
            'price': 150000, 'stock': 50, 'sold': 125,
            'rating': 4.8, 'reviews': 89, 'discount': 20,
            'image': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500',
            'description': 'Kaos premium berbahan cotton 100% yang nyaman dipakai',
            'featured': True, 'new': True
        },
        {
            'id': 2, 'name': 'Laptop Gaming ROG', 'category': 'Elektronik',
            'price': 15000000, 'stock': 10, 'sold': 45,
            'rating': 4.9, 'reviews': 156, 'discount': 10,
            'image': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=500',
            'description': 'Laptop gaming dengan performa tinggi untuk gaming dan produktivitas',
            'featured': True, 'new': False
        },
        {
            'id': 3, 'name': 'Kopi Arabica Premium', 'category': 'Makanan',
            'price': 85000, 'stock': 200, 'sold': 567,
            'rating': 4.7, 'reviews': 234, 'discount': 15,
            'image': 'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=500',
            'description': 'Kopi arabica pilihan dengan cita rasa premium',
            'featured': True, 'new': True
        },
        {
            'id': 4, 'name': 'Sepatu Running Nike', 'category': 'Olahraga',
            'price': 1200000, 'stock': 30, 'sold': 89,
            'rating': 4.6, 'reviews': 67, 'discount': 25,
            'image': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500',
            'description': 'Sepatu running dengan teknologi cushioning terbaru',
            'featured': False, 'new': True
        },
        {
            'id': 5, 'name': 'Smartwatch Series 8', 'category': 'Elektronik',
            'price': 4500000, 'stock': 15, 'sold': 34,
            'rating': 4.9, 'reviews': 123, 'discount': 0,
            'image': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500',
            'description': 'Smartwatch dengan fitur lengkap untuk gaya hidup sehat',
            'featured': True, 'new': True
        },
        {
            'id': 6, 'name': 'Headphone Wireless', 'category': 'Elektronik',
            'price': 750000, 'stock': 40, 'sold': 178,
            'rating': 4.5, 'reviews': 95, 'discount': 30,
            'image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500',
            'description': 'Headphone wireless dengan noise cancellation',
            'featured': False, 'new': False
        },
    ]
    
    users = {
        'admin@shop.com': {
            'password': 'admin123',
            'name': 'Admin Shop',
            'role': 'admin'
        },
        'user@shop.com': {
            'password': 'user123',
            'name': 'Customer',
            'role': 'user'
        }
    }
    
    product_id_counter = 7

init_sample_data()

@app.route('/')
def index():
    featured_products = [p for p in products if p.get('featured')]
    new_products = [p for p in products if p.get('new')]
    
    stats = {
        'total_products': len(products),
        'total_orders': len(orders),
        'total_customers': len(set(o['user_email'] for o in orders)) if orders else 0,
        'total_revenue': sum(o['total'] for o in orders) if orders else 0
    }
    
    return render_template('shop_index.html', 
                         products=products,
                         featured_products=featured_products[:4],
                         new_products=new_products[:4],
                         categories=categories,
                         stats=stats,
                         cart_count=len(session.get('cart', {})))

@app.route('/products')
def products_page():
    category_filter = request.args.get('category', '')
    
    filtered_products = products
    if category_filter:
        filtered_products = [p for p in products if p['category'] == category_filter]
    
    return render_template('shop_products.html',
                         products=filtered_products,
                         categories=categories,
                         selected_category=category_filter,
                         cart_count=len(session.get('cart', {})))

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        flash('Produk tidak ditemukan', 'error')
        return redirect(url_for('index'))
    
    related_products = [p for p in products if p['category'] == product['category'] and p['id'] != product_id][:4]
    
    return render_template('shop_detail.html',
                         product=product,
                         related_products=related_products,
                         cart_count=len(session.get('cart', {})))

@app.route('/cart')
def cart():
    cart_data = session.get('cart', {})
    cart_products = []
    total = 0
    
    for product_id, quantity in cart_data.items():
        product = next((p for p in products if p['id'] == int(product_id)), None)
        if product:
            discounted_price = product['price'] * (100 - product['discount']) / 100
            cart_products.append({
                'product': product,
                'quantity': quantity,
                'subtotal': discounted_price * quantity
            })
            total += discounted_price * quantity
    
    return render_template('shop_cart.html',
                         cart_products=cart_products,
                         total=total,
                         cart_count=len(cart_data))

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    quantity = int(request.form.get('quantity', 1))
    
    if 'cart' not in session:
        session['cart'] = {}
    
    cart = session['cart']
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        cart[product_id_str] += quantity
    else:
        cart[product_id_str] = quantity
    
    session['cart'] = cart
    flash('Produk berhasil ditambahkan ke keranjang!', 'success')
    
    return redirect(request.referrer or url_for('index'))

@app.route('/update_cart/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    quantity = int(request.form.get('quantity', 1))
    
    if 'cart' in session:
        cart = session['cart']
        product_id_str = str(product_id)
        
        if quantity > 0:
            cart[product_id_str] = quantity
        else:
            cart.pop(product_id_str, None)
        
        session['cart'] = cart
        flash('Keranjang berhasil diupdate!', 'success')
    
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    if 'cart' in session:
        cart = session['cart']
        cart.pop(str(product_id), None)
        session['cart'] = cart
        flash('Produk dihapus dari keranjang', 'success')
    
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        global order_id_counter
        
        cart_data = session.get('cart', {})
        if not cart_data:
            flash('Keranjang kosong!', 'error')
            return redirect(url_for('cart'))
        
        order = {
            'id': order_id_counter,
            'order_number': f'ORD-{order_id_counter:05d}',
            'user_email': request.form.get('email'),
            'user_name': request.form.get('name'),
            'phone': request.form.get('phone'),
            'address': request.form.get('address'),
            'items': [],
            'total': 0,
            'status': 'Pending',
            'created_at': datetime.now().strftime('%d/%m/%Y %H:%M')
        }
        
        for product_id, quantity in cart_data.items():
            product = next((p for p in products if p['id'] == int(product_id)), None)
            if product:
                discounted_price = product['price'] * (100 - product['discount']) / 100
                subtotal = discounted_price * quantity
                
                order['items'].append({
                    'product_name': product['name'],
                    'quantity': quantity,
                    'price': discounted_price,
                    'subtotal': subtotal
                })
                order['total'] += subtotal
        
        orders.append(order)
        order_id_counter += 1
        
        session['cart'] = {}
        flash(f'Pesanan berhasil dibuat! Nomor Order: {order["order_number"]}', 'success')
        return redirect(url_for('order_success', order_id=order['id']))
    
    cart_data = session.get('cart', {})
    if not cart_data:
        flash('Keranjang kosong!', 'error')
        return redirect(url_for('cart'))
    
    cart_products = []
    total = 0
    
    for product_id, quantity in cart_data.items():
        product = next((p for p in products if p['id'] == int(product_id)), None)
        if product:
            discounted_price = product['price'] * (100 - product['discount']) / 100
            cart_products.append({
                'product': product,
                'quantity': quantity,
                'subtotal': discounted_price * quantity
            })
            total += discounted_price * quantity
    
    return render_template('shop_checkout.html',
                         cart_products=cart_products,
                         total=total,
                         cart_count=len(cart_data))

@app.route('/order_success/<int:order_id>')
def order_success(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        flash('Order tidak ditemukan', 'error')
        return redirect(url_for('index'))
    
    return render_template('shop_order_success.html', order=order, cart_count=0)

@app.route('/about')
def about():
    return render_template('about_shop.html', cart_count=len(session.get('cart', {})))

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    
    if query:
        results = [p for p in products if 
                  query in p['name'].lower() or 
                  query in p['category'].lower() or
                  query in p['description'].lower()]
    else:
        results = []
    
    return render_template('shop_search.html',
                         query=query,
                         results=results,
                         categories=categories,
                         cart_count=len(session.get('cart', {})))

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/images', exist_ok=True)
    
    print("=" * 60)
    print("MODERN SHOP - Platform Belanja Online Modern")
    print("=" * 60)
    print("Server berjalan di: http://127.0.0.1:8080")
    print("=" * 60)
    
    app.run(debug=True, host='127.0.0.1', port=8080)