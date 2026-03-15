def architecture_decision(data):

    users = int(data.get("users", 0))
    realtime = data.get("realtime", False)
    payments = data.get("payments", False)

    architecture = {}

   #arch style
    if users < 1000:
        architecture["style"] = "Monolith"
    elif users < 10000:
        architecture["style"] = "Modular Monolith"
    else:
        architecture["style"] = "Microservices"

    services = ["User Service"]

    if payments:
        services.append("Payment Service")

    if realtime:
        services.append("Realtime Tracking Service")

    services.append("Notification Service")

    architecture["services"] = services

    databases = ["PostgreSQL"]

    if realtime:
        databases.append("Redis")

    architecture["databases"] = databases

    return architecture