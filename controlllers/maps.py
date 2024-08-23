from flask import Blueprint, render_template, jsonify

maps_bp = Blueprint('maps', __name__)

lokasi=[
    {
        "name": "Museum Barli",
        "address": "Jl. Prof. Dr. Sutami No. 91",
        "latitude": -6.8857,
        "longitude": 107.5953
    },
    {
        "name": "Museum Kebudayaan Tionghoa",
        "address": "Jl. Nana Rohana No. 37",
        "latitude": -6.921709,
        "longitude": 107.577381
    },
    {
        "name": "Museum 3D",
        "address": "Jl. Dr. Setiabudi",
        "latitude": -6.85127,
        "longitude": 107.596652
    },
    {
        "name": "Museum Preanger",
        "address": "Jl. Asia Afrika No. 81",
        "latitude": -6.920758,
        "longitude": 107.612391
    },
    {
        "name": "Museum Kota Bandung",
        "address": "Jl. Aceh No. 47",
        "latitude": -6.9141,
        "longitude": 107.6132
    },
    {
        "name": "Museum Mandala Wangsit Siliwangi",
        "address": "Jl. Lembong No. 38",
        "latitude": -6.914743,
        "longitude": 107.610146
    },
    {
        "name": "Museum Sri Baduga",
        "address": "Jl. BKR No. 185",
        "latitude": -6.942169,
        "longitude": 107.604953
    },
    {
        "name": "Museum Geologi Bandung",
        "address": "Jl. Diponegoro No. 57",
        "latitude": -6.89947,
        "longitude": 107.619123
    },
    {
        "name": "Museum Gedung Sate",
        "address": "Jl. Diponegoro No. 22",
        "latitude": -6.9025,
        "longitude": 107.6186
    },
    {
        "name": "Museum Konferensi Asia Afrika",
        "address": "Jl. Asia Afrika No. 65",
        "latitude": -6.921954,
        "longitude": 107.607045
    },
    {
        "name": "Museum Pos Indonesia",
        "address": "Jl. Cilaki No. 73",
        "latitude": -6.9003,
        "longitude": 107.6205
    },
    {
        "name": "Museum Lapas Banceuy",
        "address": "Jl. Banceuy No. 22",
        "latitude": -6.9143,
        "longitude": 107.6098
    },
    {
        "name": "Museum Mainan",
        "address": "Jl. Setiabudi No. 276",
        "latitude": -6.8382,
        "longitude": 107.5923
    },
    {
        "name": "Museum Virajati Seskoad",
        "address": "Jl. Gatot Subroto No. 165",
        "latitude": -6.9492,
        "longitude": 107.6308
    },
    {
        "name": "Museum Nike Ardilla",
        "address": "Jl. Soekarno-Hatta No. 484",
        "latitude": -6.9497,
        "longitude": 107.6331
    },
    {
        "name": "Hall of Fame Jawa Barat - Panggung Inohong",
        "address": "Jl. Braga No. 99-101",
        "latitude": -6.9182,
        "longitude": 107.6095
    },
    {
        "name": "Museum Pendidikan Nasional",
        "address": "Jl. Dr. Setiabudi No. 229",
        "latitude": -6.8605,
        "longitude": 107.5893
    },
    {
        "name": "Gedung Indonesia Menggugat",
        "address": "Jl. Perintis Kemerdekaan No. 5",
        "latitude": -6.9127,
        "longitude": 107.6081
    },
    {
        "name": "Museum Perjuangan Rakyat Jawa Barat",
        "address": "Jl. Dipati Ukur No. 48",
        "latitude": -6.8886,
        "longitude": 107.6109
    },
    {
        "name": "Museum Perbendaharaan",
        "address": "Jl. Wastukencana No. 2",
        "latitude": -6.9094,
        "longitude": 107.6052
    },
    {
        "name": "Museum Bio Farma",
        "address": "Jl. Pasteur No. 28",
        "latitude": -6.8991,
        "longitude": 107.5992
    }
]

@maps_bp.route('/lokasi')
def lokasi_view():
    return jsonify(lokasi)

@maps_bp.route('/maps')
def maps():
    return render_template('maps.html')