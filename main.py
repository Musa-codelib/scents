from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

perfumes = [
    {"name": "Lavender Bliss", "description": "A calming lavender scent.", "price": "$25", "image": "images/Lavender.jpeg", "gender": "women", "category": "new"},
    {"name": "Citrus Burst", "description": "A refreshing citrus fragrance.", "price": "$30", "image": "images/lemon.jpg", "gender": "unisex", "category": "best"},
    {"name": "Rose Garden", "description": "A romantic rose aroma.", "price": "$28", "image": "images/Rose.jpg", "gender": "women", "category": "new"},
    {"name": "Ocean Breeze", "description": "A cool, marine-inspired scent.", "price": "$35", "image": "images/Ocean.jpg", "gender": "men", "category": "best"}
]

@app.route('/')
def home():
    return render_template('index.html', perfumes=perfumes)

@app.route('/men')
def men():
    men_perfumes = [p for p in perfumes if p['gender'] == 'men']
    return render_template('men.html', perfumes=men_perfumes)

@app.route('/women')
def women():
    women_perfumes = [p for p in perfumes if p['gender'] == 'women']
    return render_template('women.html', perfumes=women_perfumes)

@app.route('/new_arrivals')
def new_arrivals():
    new_arrivals = [p for p in perfumes if p.get('category') == 'new'] 
    return render_template('new_arrivals.html', new_arrivals=new_arrivals)

@app.route('/best_sellers')
def best_sellers():
    best_sellers = [p for p in perfumes if p.get('category') == 'best']
    return render_template('best_sellers.html', best_sellers=best_sellers)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# --- Admin Functionality (Basic Example) ---
# You'll need a better authentication system in a real app.
@app.route('/admin/add_perfume', methods=['GET', 'POST'])
def add_perfume():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        gender = request.form['gender']
        image = request.form['image']  # Placeholder, you'll need to handle image uploads
        category = request.form.get('category')  # "new" for New Arrivals, "best" for Best Sellers

        new_perfume = {
            'name': name,
            'description': description,
            'price': price,
            'gender': gender,
            'image': image,
            'category': category
        }
        perfumes.append(new_perfume)

        return redirect(url_for('new_arrivals')) # Redirect to the New Arrivals page

    return render_template('add_perfume.html') # Render a form for adding perfumes 
 
if __name__ == '__main__':
    app.run(debug=True, port=5001)
