# Biến lưu trữ dữ liệu: Mỗi bài hát là một dict {'title': '...', 'artist': '...', 'duration': 0}
songs = []


def add_song():
    print("Đã thêm bài hát vào playlist.")


def view_playlist():
    # Duyệt list songs và in ra
    # Ví dụ: 1. Lạc Trôi - Sơn Tùng MTP (240s)
    pass


def search_by_artist():
    # Nhập tên ca sĩ
    # Duyệt list, so sánh artist (có thể dùng in hoặc ==), in ra bài hát
    pass


def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_song()
        elif choice == '2':
            view_playlist()
        elif choice == '3':
            search_by_artist()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
