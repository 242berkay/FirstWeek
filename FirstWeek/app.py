from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    return render_template('index.html')

@app.route('/admin/giris')
def admin_giris():
    return render_template('admin_giris.html')

@app.route('/admin/panel')
def admin_paneli():
    return render_template('admin_paneli.html')

@app.route('/admin/cikis')
def admin_cikis():
    return redirect(url_for('ana_sayfa'))

@app.route('/kayit')
def kayit():
    return redirect(url_for('ana_sayfa'))

@app.route('/kayit_formu')
def kayit_formu():
    return render_template('kayit_formu.html')

@app.route('/listele')
def listele():
    return render_template('listele.html')

@app.route('/guncelle/<int:ziyaretci_id>')
def guncelle_formu(ziyaretci_id):
    return render_template('guncelleformu.html')

@app.route('/sil/<int:ziyaretci_id>')
def sil(ziyaretci_id):
    return redirect(url_for('listele'))

@app.route('/filtrele')
def filtrele():
    return render_template('filtrele.html')

@app.route('/kayitli_ziyaretciler')
def kayitli_ziyaretciler():
    ziyaretciler = []
    return render_template('kayitli_ziyaretciler.html')

@app.route('/raporlar')
def raporlar():
    return render_template('raporlar.html')

@app.route('/kayitli_kullanici')
def kayitli_kullanici():
    return render_template('kayitli_kullanici.html')

if __name__ == '__main__':
    app.run(debug=True)