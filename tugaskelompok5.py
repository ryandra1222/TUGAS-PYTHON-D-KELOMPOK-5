import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
        )
        if connection.is_connected():
            print("Berhasil terhubung ke MySQL")
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS database_anggota")
        cursor.execute("USE database_anggota")
        print("Database 'database_anggota' siap digunakan")
    except Error as e:
        print(f"Error: '{e}'")

def create_table_and_insert_data(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("USE database_anggota")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY,
                nama VARCHAR(50),
                kota VARCHAR(50)
            )
        """)
        cursor.execute("""
            INSERT INTO users (id, nama, kota) VALUES
            (2, 'Doni', 'Jakarta'),
            (3, 'Ella', 'Surabaya'),
            (4, 'Fani', 'Bandung'),
            (5, 'Galih', 'Depok')
            ON DUPLICATE KEY UPDATE id=id
        """)
        connection.commit()
        print("Tabel 'users' siap digunakan dan data awal telah dimasukkan")
    except Error as e:
        print(f"Error: '{e}'")

def insert_data(connection):
    try:
        cursor = connection.cursor()
        id_user = int(input("Masukkan ID: "))
        nama = input("Masukkan nama: ")
        kota = input("Masukkan kota: ")
        query = "INSERT INTO users (id, nama, kota) VALUES (%s, %s, %s)"
        cursor.execute(query, (id_user, nama, kota))
        connection.commit()
        print("Data berhasil ditambahkan")
    except Error as e:
        print(f"Error: '{e}'")

def update_data(connection):
    try:
        cursor = connection.cursor()
        id_user = int(input("Masukkan ID data yang akan diupdate: "))
        nama = input("Masukkan nama baru: ")
        kota = input("Masukkan kota baru: ")
        query = "UPDATE users SET nama = %s, kota = %s WHERE id = %s"
        cursor.execute(query, (nama, kota, id_user))
        connection.commit()
        print("Data berhasil diupdate")
    except Error as e:
        print(f"Error: '{e}'")

def delete_data(connection):
    try:
        cursor = connection.cursor()
        id_user = int(input("Masukkan ID data yang akan dihapus: "))
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (id_user,))
        connection.commit()
        print("Data berhasil dihapus")
    except Error as e:
        print(f"Error: '{e}'")

def search_data(connection):
    try:
        cursor = connection.cursor()
        id_user = int(input("Masukkan ID data yang akan dicari: "))
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (id_user,))
        record = cursor.fetchone()
        if record:
            print("Data ditemukan: ", record)
        else:
            print("Data tidak ditemukan")
    except Error as e:
        print(f"Error: '{e}'")

def main():
    connection = create_connection()
    if connection:
        create_database(connection)  # Membuat database jika belum ada
        create_table_and_insert_data(connection)
        
        while True:
            print("\n=== Aplikasi Data Base ===")
            print("1. Koneksi untuk menghubungkan MySQL")
            print("2. Membuat insert data MySQL")
            print("3. Update data dari MySQL")
            print("4. Hapus data dari MySQL")
            print("5. Cari data")
            print("0. Keluar")
            choice = input("Pilih menu> ")
            
            if choice == '1':
                create_connection()
            elif choice == '2':
                insert_data(connection)
            elif choice == '3':
                update_data(connection)
            elif choice == '4':
                delete_data(connection)
            elif choice == '5':
                search_data(connection)
            elif choice == '0':
                break
            else:
                print("Pilihan tidak valid")
        
        if connection.is_connected():
            connection.close()
            print("Koneksi ke MySQL ditutup")

if __name__ == "__main__":
    main()
