total_time_seconds = int(input("Введите время в секундах: "))

# total_time_seconds = 14530

hours = (total_time_seconds // 60) // 60
minutes = (total_time_seconds % 3600) // 60
seconds = total_time_seconds % 60
print("=========================")
if hours < 10 and minutes < 10 and seconds < 10:
    print(f"0{hours}:0{minutes}:0{seconds}")
elif hours >= 10 > minutes > seconds:
    print(f"{hours}:0{minutes}:0{seconds}")
elif hours >= 10 > seconds and minutes >= 10:
    print(f"{hours}:{minutes}:0{seconds}")
elif hours < 10 <= seconds and minutes < 10:
    print(f"0{hours}:0{minutes}:{seconds}")
elif hours < 10 <= minutes <= seconds:
    print(f"0{hours}:{minutes}:{seconds}")

else:
    print(f"{hours}:{minutes}:{seconds}")

