time = "1h 45m,360s,25m,30m 120s,2h 60s"

new_time = time.replace(",", " ")

new_time = new_time.split(" ")

minutes = 0
for m in new_time:
    if "h" in m:
        minutes += int(m.replace("h", "")) * 60

    if "s" in m:
        minutes += int(m.replace("s", "")) // 60

    if "m" in m:
        minutes += int(m.replace("m", ""))


print(minutes)
