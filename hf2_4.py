room_size = 75 #m^2
one_can_paint = 15 #m^2
one_can_paint_price = 4300 #Ft

number_of_cans = 2* (room_size / one_can_paint)
print(number_of_cans, " vödör festékre van szükség.")

price_of_cans = number_of_cans * one_can_paint_price
print(price_of_cans, " Ft értékben kell festéket vásárolni.")

painting_time_1m2_min = 13
painting_time_1m2_hour = painting_time_1m2_min / 60
wages_per_hour = 2100 #Ft, nettó
painting_time_for_room = room_size * painting_time_1m2_hour
painting_price_for_room = painting_time_for_room * wages_per_hour
print(painting_price_for_room, "Ft-ért festi ki az egész szobát.")

AFA = 1.27
painting_price_for_room_with_AFA = painting_price_for_room * AFA
print(painting_price_for_room_with_AFA, "Ft lesz az összeg Áfa hozzáadásával.")




