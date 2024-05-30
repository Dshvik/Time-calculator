#Time calculator

seconds = 3666

hours = seconds // 3600
lefotver_sec = seconds % 3600

minutes = lefotver_sec // 60

last_sec = lefotver_sec % 60

print(seconds,"sekund", "to", hours,"godzin", minutes,"minut", last_sec,"sekund")