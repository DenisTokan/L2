def distribute_funds(total_sum, participants):
    # Считывание данных посещаемости для каждого участника
    attendance_counts = []
    total_attendance = 0

    for i in range(participants):
        attendance = input(f"Введите посещаемость для участника {i+1} (используйте '+' для каждого посещения): ")
        count = attendance.count('+')
        attendance_counts.append(count)
        total_attendance += count

    # Распределение суммы на основе посещаемости
    if total_attendance == 0:
        print("Никто не посещал, адену распределить нельзя.")
        return

    distributed_sum = 0
    print("\nРаспределение сумм:")
    for i, count in enumerate(attendance_counts):
        participant_sum = (count * total_sum) // total_attendance  # Используем целочисленное деление
        distributed_sum += participant_sum
        print(f"Участник {i+1} получает: {participant_sum} адены")
    
    # Расчет и вывод неразделенного излишка
    remainder = total_sum - distributed_sum
    print(f"Неразделенный излишек: {remainder} адены")

# Основная часть программы
if __name__ == "__main__":
    total_sum = int(input("Введите общую сумму для распределения: "))
    participants = int(input("Введите количество участников: "))

    distribute_funds(total_sum, participants)
