class Book:
    def __init__(self,book_name):
        self.book_name=book_name
class Library(Book):
    def __init__(self,book_name,issue_date=None,return_date=None):
        super().__init__(book_name)
        self.issue_date=issue_date
        self.return_date=return_date
        self.borrowed=False

    def borrow_book(self,issue_date):
        if not self.borrowed:
            self.issue_date=issue_date
            self.borrowed=True
        else:
            print(f"'{self.book_name}' already borrowed")   

    def return_book(self,return_date):
        if self.borrowed:
            self.return_date=return_date
            self.borrowed=False
        else:
            print(f"'{self.book_name}' already returned")








