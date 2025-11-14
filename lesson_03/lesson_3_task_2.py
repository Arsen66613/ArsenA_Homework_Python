from smartphone import Smartphone

smartphone1 = (Smartphone("Apple", "iPhone 14", "+79990000001"))
smartphone2 = (Smartphone("Samsung", "Galaxy S23", "+79990000002"))
smartphone3 = (Smartphone("Xiaomi", "Redmi Note 12", "+79990000003"))
smartphone4 = (Smartphone("Google", "Pixel 7", "+79990000004"))
smartphone5 = (Smartphone("Huawei", "P50", "+79990000005"))

catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
