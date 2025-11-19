from adrs import Address
from mail import Mailing

to_addr = Address("12345", "Москва", "Красная площадь", "1", "100")
from_addr = Address("54321", "Санкт-Петербург", "Невский проспект", "10", "50")

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    track="TRACK123456789",
    cost=250.0
)

print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.postal_code}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.building} - "
    f"{mailing.from_address.apartment} в "
    f"{mailing.to_address.postal_code}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.building} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
