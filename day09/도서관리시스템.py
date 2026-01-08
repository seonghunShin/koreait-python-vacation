books = []
# {"book_id": "1", "book_name": "파이썬책"}
# [{},{},{}...{}]

while True:
    print("== 도서 관리 시스템 ==")
    print("1. 도서 등록")
    print("2. 전체 도서 조회")
    print("2-1. 특정 도서 조회")
    print("3. 도서 삭제")
    print("4. 종료\n")

    selected_menu = input("메뉴를 선택해주세요: ")
    if selected_menu == "1":
        # 도서 등록
        book = input("등록할 도서의 이름을 입력하여주세요: ")
        num = len(books) + 1

        is_duplicated = False
        for book_dict in books:
            is_book = book_dict[book]
            if is_book == book:
                is_duplicated = True
                print("이미 존재하는 도서입니다.")
                break

        if is_duplicated:
            continue

        new_book = {
            "book_id": num,
            "book_name": book,
        }

        books.append(new_book)
        print("등록이 완료되었습니다.")

    elif selected_menu == "2":
        # 전체 도서 조회

        if len(books) == 0:
            print("등록되어있는 도서가 존재하지 않습니다.")
            continue
        for search_book in books:
            num = search_book["book_id"]
            name = search_book["book_name"]
            print(f"도서번호: {num}, 도서이름: {name}")

    elif selected_menu == "2-1":
        # 특정 도서 조회
        if len(books) == 0:
            print("등록되어있는 도서가 존재하지 않습니다.")
            continue
        print("1. 도서번호, 2. 도서이름")
        choice_book = input("무엇으로 찾으시겠습니까: ")
        if choice_book == "1":
            select_book = input("조회할 도서의 번호를 입력하여주세요: ")
            for book_dict in books:
                if select_book == book_dict["book_id"]:
                    is_book_name = book_dict["book_name"]
                    print(f"도서 번호: {select_book} 도서 이름: {is_book_name}")
                    continue
                else:
                    print("해당 도서 번호는 없습니다.")
                    continue
        elif choice_book == "2":
            select_bookname = input("조회할 도서의 이름을 입력하여주세요: ")
            for book_dict in books:
                if select_bookname == book_dict["book_name"]:
                    is_book_id = book_dict["book_id"]
                    print(f"도서 번호: {is_book_id}, 도서 이름: {select_bookname}")
                    continue
                else:
                    print("해당 도서는 없습니다.")
                    continue

    elif selected_menu == "3":
        # 도서 삭제
        if len(books) == 0:
            print("삭제할 도서가 존재하지 않습니다.")
            continue

        print("1. 도서번호, 2. 도서이름")
        choice_remove = input("무엇으로 삭제하시겠습니까:")
        if choice_remove == "1":
            remove_book_id = input("삭제할 도서의 번호를 입력하여주세요: ")
            found = False
            for book_dict in books:
                if remove_book_id == book_dict["book_id"]:
                    found = True
                    book_name = book_dict["book_name"]
                    print(f"\"{remove_book_id}: {book_name}\" 정보가 삭제됩니다.")
                    books.remove(book_dict)
                    break
            if not found:
                print("해당 도서는 이미 존재하지 않습니다")
                continue
        elif choice_remove == "2":
            remove_book = input("삭제할 도서의 이름을 입력하여주세요: ")
            found = False
            for book_dict in books:
                if remove_book == book_dict["book_name"]:
                    found = True
                    book_id = book_dict["book_id"]
                    print(f"\"{book_id}: {remove_book}\" 정보가 삭제됩니다.")
                    books.remove(book_dict)
                    break
            if not found:
                print("해당 도서는 이미 존재하지 않습니다")
                continue

    elif selected_menu == "4":
        print("시스템 종료")
        break