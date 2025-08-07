from flask import Flask, render_template, request, send_file
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

app = Flask(__name__)

# 📁 Folder paths
BASE_FOLDER = 'uploads'
ORIGINAL_FOLDER = os.path.join(BASE_FOLDER, 'original')
ENCRYPTED_FOLDER = os.path.join(BASE_FOLDER, 'encrypted')
DECRYPTED_FOLDER = os.path.join(BASE_FOLDER, 'decrypted')

# ✅ Auto create folders
for folder in [ORIGINAL_FOLDER, ENCRYPTED_FOLDER, DECRYPTED_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 🔐 AES 128-bit key
key = get_random_bytes(16)

# 🔒 Encryption
def encrypt_file(input_path, output_path):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(input_path, 'rb') as f:
        data = f.read()
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    with open(output_path, 'wb') as f:
        f.write(cipher.iv + ciphertext)

# 🔓 Decryption
def decrypt_file(input_path, output_path):
    with open(input_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    with open(output_path, 'wb') as f:
        f.write(plaintext)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename:
            original_path = os.path.join(ORIGINAL_FOLDER, file.filename)
            encrypted_path = os.path.join(ENCRYPTED_FOLDER, file.filename + '.enc')
            file.save(original_path)
            encrypt_file(original_path, encrypted_path)
            return f"✅ File encrypted! Go back to download."
    files = os.listdir(ENCRYPTED_FOLDER)
    return render_template('index.html', files=files)

# 🔓 Route to download decrypted file
@app.route('/download/<filename>')
def download(filename):
    encrypted_path = os.path.join(ENCRYPTED_FOLDER, filename)
    decrypted_path = os.path.join(DECRYPTED_FOLDER, filename.replace('.enc', ''))
    decrypt_file(encrypted_path, decrypted_path)
    return send_file(decrypted_path, as_attachment=True)

# 🔐 Route to download encrypted file
@app.route('/download_encrypted/<filename>')
def download_encrypted(filename):
    path = os.path.join(ENCRYPTED_FOLDER, filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
