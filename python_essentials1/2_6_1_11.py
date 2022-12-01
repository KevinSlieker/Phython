hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hours= int(hour+((mins+dura)/60))%24
mins2 = (mins+dura)%60
end_time = (str(int(hour+((mins+dura)/60))%24) + ":" + str((mins+dura)%60))
print(hours,":",mins2)
print(end_time)