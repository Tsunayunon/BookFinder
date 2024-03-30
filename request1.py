import requests

def get_book_info(book_title, author):
    url = f'https://www.googleapis.com/books/v1/volumes?q=intitle:{book_title}+inauthor:{author}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            first_book = data["items"][0]["volumeInfo"]
            title = first_book.get("title", "N/A")
            authors = first_book.get("authors", ["N/A"])[0]
            desc = first_book.get("description", "N/A")
            print(f"Kitap adı: {title}\nYazar: {authors}\nAçıklama: {desc}")
        else:
            print("Kitap bulunamadı.")
    else:
        print("Kitap bilgilerine erişilemedi.")

# Fonksiyon çağrısını yaparken hatayı düzelttim.
get_book_info("Cress", "Marissa Meyer")
get_book_info("Cress", "Marissa Meyer")  # Kitap adı: Cress, Yazar: Marissa Meyer, Açıklama: N/A