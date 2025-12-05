# Biến lưu trữ dữ liệu: Mỗi bài hát là một dict {'title': '...', 'artist': '...', 'duration': 0}
songs = []


def add_song():
    print("\n--- Thêm bài hát ---")
    title = input("Nhập tên bài hát: ").strip()
    artist = input("Nhập tên ca sĩ: ").strip()
    duration = input("Nhập thời lượng (giây): ").strip()

    # Kiểm tra duration có phải số không
    if duration.isdigit():
        duration = int(duration)
    else:
        print("❌ Thời lượng phải là số! Không thể thêm.")
        return

    # Lưu vào playlist (danh sách toàn cục)
    song = {'title': title, 'artist': artist, 'duration': duration}
    songs.append(song)
    print("✔ Đã thêm bài hát vào playlist.")



def view_playlist():
    print("\n--- Danh sách phát ---")
    if not songs:
        print("Playlist hiện đang trống.")
        return
    
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song['title']} - {song['artist']} ({song['duration']}s)")



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
