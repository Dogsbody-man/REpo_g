city_map_list = [
    [1, 1, 0, 0, 1], 
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1]
]
courier_location = (84, 17)
orders_location = [(66, 32), (39, 75), (90, 10), (89, 60), (79, 77), (65, 38), (9, 5)]

def the_way_of_courier(city_map_list, courier_location, orders_location):
    route_1 = []
    current_courier_location = list(courier_location)
    current_courier_location.reverse()
    for delivery_location in orders_location:
        delivery_location = list(delivery_location)
        delivery_location.reverse()
        while current_courier_location != delivery_location:
            if current_courier_location[0] > delivery_location[0]:
                if city_map_list[current_courier_location[0] - 1][current_courier_location[1]] == 1:
                    current_courier_location[0] -= 1
                    a = (current_courier_location[1], current_courier_location[0])
                    route_1.append(a)
            elif current_courier_location[0] < delivery_location[0]:
                if city_map_list[current_courier_location[0] + 1][current_courier_location[1]] == 1:
                    current_courier_location[0] += 1
                    a = (current_courier_location[1], current_courier_location[0])
                    route_1.append(a)
            if current_courier_location[1] > delivery_location[1]:
                if city_map_list[current_courier_location[0]][current_courier_location[1] - 1] == 1:
                    current_courier_location[1] -= 1
                    a = (current_courier_location[1], current_courier_location[0])
                    route_1.append(a)        
            elif current_courier_location[1] < delivery_location[1]:
                if city_map_list[current_courier_location[0]][current_courier_location[1] + 1] == 1:
                    current_courier_location[1] += 1
                    a = (current_courier_location[1], current_courier_location[0])
                    route_1.append(a)
    return route_1
route = the_way_of_courier(city_map_list, courier_location, orders_location)
print(route)