from flask import Flask, render_template

app = Flask(__name__)

perfumes = [
    {"name": "Lavender Bliss", "description": "A calming lavender scent.", "price": "$25", "image": "images/Lavender.jpeg", "gender": "women", "category": "new"},
    {"name": "Citrus Burst", "description": "A refreshing citrus fragrance.", "price": "$30", "image": "images/lemon.jpg", "gender": "unisex", "category": "best"},
    {"name": "Rose Garden", "description": "A romantic rose aroma.", "price": "$28", "image": "images/Rose.jpg", "gender": "women", "category": "new"},
    {"name": "Ocean Breeze", "description": "A cool, marine-inspired scent.", "price": "$35", "image": "/images/Ocean.jpg", "gender": "men", "category": "best"}
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
    new_arrival_perfumes = [p for p in perfumes if p.get('category') == 'new']
    return render_template('new_arrivals.html', perfumes=new_arrival_perfumes)

@app.route('/best_sellers')
def best_sellers():
    best_selling_perfumes = [p for p in perfumes if p.get('category') == 'best']
    return render_template('best_sellers.html', perfumes=best_selling_perfumes)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
