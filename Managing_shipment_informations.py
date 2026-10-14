# Using Dictionaries to Manage Shipment Information
print("==Question 1a==")
shipments = {
    "SHPID-01": "Delivered",
    "SHPID-02": "Pending",
    "SHPID-03": "In Transit",
    "SHPID-04": "Pending"
}

for shipment_id, status in shipments.items():
    print(f"{shipment_id}: {status}")

print("Shipment IDs:", list(shipments.keys()))
print("Shipment statuses:", list(shipments.values()))
print()

print("==Question 1b==")
# Retrieving the Status of a Specific Shipment
shipments = {
    "SHP101": "Delivered",
    "SHP102": "In Transit",
    "SHP103": "Pending"
}

status = shipments.get("SHP103", "Shipment not found")
print(f"Status of SHP103: {status}")
print()


print("==Question 2a==")
# Updating, Adding, and Removing Shipments
shipments = {
    "SHP101": "Delivered",
    "SHP102": "In Transit",
    "SHP103": "Pending"
}

# Update an existing shipment
shipments["SHP103"] = "Delivered"

# Add a new shipment
shipments["SHP104"] = "Pending"

# Remove a record if it exists
shipments.pop("SHP101", None)

print(shipments)
print()

print("==Question 2b==")
# Using Dictionary Methods to Generate Summaries
shipments = {
    "SHP101": "Delivered",
    "SHP102": "In Transit",
    "SHP103": "Pending",
    "SHP104": "Pending",
    "SHP105": "Delivered"
}

status_counts = {}

for shipment_id, status in shipments.items():
    status_counts[status] = status_counts.get(status, 0) + 1

print("Shipment summary:")
for status, count in status_counts.items():
    print(f"{status}: {count}")
print()



print("==Question 3a==")
# Creating Sets of Delivery Cities
north = {"New York", "Dallas", "Miami"}
south = {"Miami", "Atlanta", "Dallas"}
print("North cities ->",north)
print("South cities ->",south)
print()

print("==Question 3b")
# All unique delivery cities
all_cities = north.union(south)

# Cities served by both regions
common_cities = north.intersection(south)

# Cities served only by the North
north_only = north - south

# Cities served only by the South
south_only = south - north

print("All cities:", all_cities)
print("Shared cities:", common_cities)
print("North only:", north_only)
print("South only:", south_only)







