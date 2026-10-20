import os
from flask import Flask, render_template, jsonify, Response

app = Flask(__name__)

@app.context_processor
def site_config():
    return dict(support_email=os.getenv('SUPPORT_EMAIL', 'support@girogato.com'),
                ios_url=os.getenv('IOS_APP_URL', ''), android_url=os.getenv('ANDROID_APP_URL', ''),
                privacy_updated='October 20, 2026')

@app.get('/')
def home(): return render_template('home.html', page='home')

@app.get('/privacy')
@app.get('/privacy-policy')
def privacy(): return render_template('privacy.html', page='privacy')

@app.get('/support')
def support(): return render_template('support.html', page='support')

@app.get('/health')
def health(): return jsonify(status='ok')

@app.get('/robots.txt')
def robots(): return Response('User-agent: *\nAllow: /\nSitemap: https://girogato.com/sitemap.xml\n', mimetype='text/plain')

@app.get('/sitemap.xml')
def sitemap():
    urls=['https://girogato.com/','https://girogato.com/privacy','https://girogato.com/support']
    body='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{url}</loc></url>' for url in urls)+'</urlset>'
    return Response(body, mimetype='application/xml')

if __name__ == '__main__': app.run(debug=True, port=8080)
