def allocate_books(books, N, M):

    if M > N:
        return -1

    def canAllocate(limit):
        students = 1
        pages = 0

        for book in books:
            if pages + book > limit:
                students += 1
                pages = book
            else:
                pages += book

        return students <= M

    left = max(books)
    right = sum(books)

    while left <= right:
        mid = (left + right) // 2

        if canAllocate(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left