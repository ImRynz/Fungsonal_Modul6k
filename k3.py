# TODO 0 : Import beberapa library lain yang dibutuhkan
from PIL import Image

# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open('D:\PIC\tes.jpg')
overlay_image = Image.open('D:\PIC\overlay.jpg')

# TODO 2 : Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert('RGBA')

# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
overlay_width, overlay_height = overlay_image.size
resize_factor = 0.6  # Misalnya, dapat diubah sesuai kebutuhan
overlay_image = overlay_image.resize((int(overlay_width * resize_factor), int(overlay_height * resize_factor)))

# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2
background_image.paste(overlay_image, (x_center, y_center), overlay_image)

# TODO 5 : Simpan gambar hasil edit
save_path = 'D:\PIC\after.jpg'
background_image.save(save_path)

# TODO 6 : Tampilkan
background_image.show()