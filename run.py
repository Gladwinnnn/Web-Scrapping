from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.select_place_to_go(place_to_go='New York')
    bot.select_dates(check_in='2022-05-21', check_out='2022-05-30')
    bot.select_adults(count=5)
    bot.search()