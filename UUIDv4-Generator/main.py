# UUIDv4 Gen
import uuid

f = open("uuids.txt", "w")

number = int(input("How many UUIDs do you want to generate? "))

for i in range(number):
  f.write(str(f"{uuid.uuid4()}\n"))

f.close()

# Find more about uuid library here: https://docs.python.org/3/library/uuid.html
# Find more about UUIDs here: https://en.wikipedia.org/wiki/Universally_unique_identifier
