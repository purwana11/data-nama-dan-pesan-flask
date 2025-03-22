from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    nama = ""
    pesan = ""
    if request.method == "POST":
        # Mengambil data dari formulir
        nama = request.form.get("nama")
        pesan = request.form.get("pesan")
    # Menampilkan halaman utama dengan data yang dikirim
    return render_template("index.html", nama=nama, pesan=pesan)

if __name__ == "__main__":
    app.run(debug=True)