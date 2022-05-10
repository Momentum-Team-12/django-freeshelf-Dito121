from books.models import Book
import csv


def run():
    with open('sample_books.csv') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            print(row)

            book = Book(title=row[0],
                        author=row[1],
                        url=row[2],
                        description=row[3])
            book.save()
