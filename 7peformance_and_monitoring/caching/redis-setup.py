import redis


r = redis.Redis(host="localhost", port=6379, db=0)

try:
    if r.ping():
        print("Connected to redis")

except redis.ConnectionError:
    print("Redis connection failed")


r.set("framwork", "fastapi")

value = r.get("framwork")
print(value.decode())
