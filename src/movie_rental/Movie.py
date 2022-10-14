class Movie:
    REGULAR: int = 0
    CHILDRENS: int = 1
    NEW_RELEASE: int = 2

    title: str
    price_code: int

    def __init__(self, title: str, price_code: int):
        self.title = title
        self.price_code = price_code

    def get_price_code(self) -> int:
        return self.price_code

    def set_price_code(self, price_code: int):
        self.price_code = price_code

    def get_title(self) -> str:
        return self.title
