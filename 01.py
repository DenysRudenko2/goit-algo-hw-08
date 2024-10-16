import heapq


def min_connection_cost(cables):
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cables)

    total_cost = 0

    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Беремо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо їх
        cost = first + second
        total_cost += cost

        # Додаємо об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost


# Приклад використання
cables = [4, 3, 2, 6]
result = min_connection_cost(cables)
print(f"Мінімальні витрати на з'єднання кабелів: {result}")
