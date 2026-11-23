class MenuItem:
    """카페의 개별 메뉴(음료 및 디저트) 정보를 관리하는 클래스입니다."""

    def __init__(self, name, price, is_ice=None):
        self.name = name
        self.price = price
        self.is_ice = is_ice

    def get_info(self):
        """메뉴명, 온도 옵션, 가격 정보를 문자열로 반환합니다."""
        if self.is_ice is True:
            temp_option = " (ICE)"
        elif self.is_ice is False:
            temp_option = " (HOT)"
        else:
            temp_option = ""

        return f"{self.name}{temp_option} - {self.price:,}원"

    def __str__(self):
        return self.get_info()


class Order:
    """손님의 장바구니와 주문 내역, 영수증 출력을 담당하는 클래스입니다."""

    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        """장바구니(items) 리스트에 MenuItem 객체를 추가합니다."""
        self.items.append(menu_item)
        print(f"-> [담기 완료] {menu_item.get_info()}\n")

    def get_total_price(self):
        """장바구니에 담긴 모든 메뉴 객체의 가격을 합산하여 반환합니다."""
        return sum(item.price for item in self.items)

    def print_receipt(self):
        """최종 주문 내역과 총 결제 금액 영수증을 출력합니다."""
        print("\n" + "=" * 44)
        print("            [ 카페 주문 영수증 ]")
        print("=" * 44)

        if not self.items:
            print("  장바구니에 담긴 메뉴가 없습니다.")
        else:
            for idx, item in enumerate(self.items, 1):
                print(f"  {idx}. {item.get_info()}")
            print("-" * 44)
            print(f"  총 주문 수량  : {len(self.items)}개")
            print(f"  최종 결제 금액: {self.get_total_price():,}원")

        print("=" * 44)


def main():
    menu_board = {
        1: ("아메리카노", 4000, True),
        2: ("카페라떼", 4500, True),
        3: ("바닐라라떼", 5000, True),
        4: ("치즈케이크", 6000, False),
        5: ("초코 브라우니", 4500, False),
    }

    order = Order()

    print("============================================")
    print("       어서오세요! 스마트 카페 키오스크")
    print("============================================")
    for num, (name, price, _) in menu_board.items():
        print(f"  {num}. {name:<10} : {price:,}원")
    print("  0. 주문 완료 및 영수증 출력")
    print("============================================\n")

    while True:
        try:
            choice = int(input("메뉴 번호를 선택하세요 (결제는 0): "))
        except ValueError:
            print("오류: 숫자로 입력해 주세요.\n")
            continue

        if choice == 0:
            break

        if choice not in menu_board:
            print("오류: 메뉴판에 있는 번호를 선택해 주세요.\n")
            continue

        name, price, is_drink = menu_board[choice]

        if is_drink:
            temp_input = input("온도를 선택하세요 (1: ICE / 2: HOT): ").strip()
            if temp_input == "1":
                is_ice = True
            elif temp_input == "2":
                is_ice = False
            else:
                print("오류: 1 또는 2만 입력해 주세요.\n")
                continue
        else:
            is_ice = None
        selected_item = MenuItem(name, price, is_ice)
        order.add_item(selected_item)

    order.print_receipt()


if __name__ == "__main__":
    main()
