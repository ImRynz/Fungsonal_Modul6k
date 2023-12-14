# TODO 0: Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open('D:\PIC\kocheng.png')  # Ganti dengan path gambar Anda

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text "DIKA_214" sesuai kriteria
draw = ImageDraw.Draw(gambarBW)
direktoriFont = 'C:/Windows/Fonts/Arial.ttf'  # Ganti dengan path font Anda
size = 50
font = ImageFont.truetype(direktoriFont, size)
text = "nama: rifki\nnim: 352"

# Mendapatkan ukuran teks tanpa menggunakan draw.textsize
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
text_x = (gambarku.width - text_width) // 2
text_y = (gambarku.height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill="black")

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save() di path yang diinginkan
save_path = r'D:\PIC\kocheng.png'
gambarBW.save(save_path)

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()