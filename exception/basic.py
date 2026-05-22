class InvalidChaiError(Exception):
    pass

def bill(flavor, cups):
    menu = {"masala" : 30, "ginger" : 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai is not available.")
        if not isinstance(cups, int):
            raise TypeError("Cups must be integer")
        total = menu[flavor] * cups
        print(f"Your bills for {cups} cups of {flavor} flavor is {total}")

    except Exception as e:
        print("Error :",e)
    
    finally:
        print("Thank you for visiting")

bill("ginger","THREE")
bill("masala",2)
bill("cardaman",3)