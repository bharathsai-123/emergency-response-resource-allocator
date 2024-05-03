class Resource:
    def __init__(self, id, type, status="Available"):
        self.id = id
        self.type = type
        self.status = status

#This part defines a class called Resource, which represents an emergency resource such as an ambulance, police unit, or fire truck. 
#It has three attributes: id, type, and status. The status attribute has a default value of "Available".

class EmergencyResourceAllocator:
    def __init__(self):
        self.resources = []

#This class EmergencyResourceAllocator represents the main system for managing emergency resources.
# It initializes an empty list resources to store instances of the Resource class.


    def add_resource(self, resource):
        self.resources.append(resource)

#This method add_resource adds a new resource to the list of resources managed by the allocator.

    def get_resource_by_id(self, resource_id):
        for resource in self.resources:
            if resource.id == resource_id:
                return resource
        return None

#This method get_resource_by_id retrieves a resource from the list based on its ID. It iterates through the list of resources and 
#returns the resource if its ID matches the provided resource_id. If no resource is found, it returns None.

    def update_resource_status(self, resource_id, new_status):
        resource = self.get_resource_by_id(resource_id)
        if resource:
            resource.status = new_status
            return True
        return False

#This method update_resource_status updates the status of a resource based on its ID. It first calls the get_resource_by_id method to retrieve the resource with the given resource_id. 
#If the resource exists, it updates its status attribute to the new_status provided and returns True. If the resource does not exist, it returns False.

    def delete_resource_by_id(self, resource_id):
        resource = self.get_resource_by_id(resource_id)
        if resource:
            self.resources.remove(resource)
            return True
        return False

#This method delete_resource_by_id deletes a resource from the list based on its ID. It first calls the get_resource_by_id method to retrieve the resource with the given resource_id. 
#If the resource exists, it removes it from the list of resources and returns True. If the resource does not exist, it returns False.

    def allocate_emergency_resources(self, request_id):
        # For simplicity, let's assume the request ID corresponds to the resource type needed
        required_resource_type = request_id
        for resource in self.resources:
            if resource.type == required_resource_type and resource.status == "Available":
                resource.status = "Allocated"
                return f"Allocated {required_resource_type} (Resource ID: {resource.id})"
        return f"No available {required_resource_type} found."


#This method allocate_emergency_resources allocates emergency resources based on a request ID. It iterates through the list of resources and checks if there is an available resource of the type specified by the request_id. 
#If an available resource is found, its status is updated to "Allocated", and a message indicating the allocation is returned. If no available resource is found, a message indicating that is returned.
    
    def monitor_resource_usage(self):
        for resource in self.resources:
            print(f"Resource ID: {resource.id}, Type: {resource.type}, Status: {resource.status}")

#This method monitor_resource_usage prints the details of all resources currently managed by the system. 
#It iterates through the list of resources and prints their ID, type, and status.

def main():
    allocator = EmergencyResourceAllocator()

    # Adding some initial resources
    allocator.add_resource(Resource(1, "Ambulance"))
    allocator.add_resource(Resource(2, "Police Unit"))
    allocator.add_resource(Resource(3, "Fire Truck"))

#The main function serves as the entry point of the program. It creates an instance of EmergencyResourceAllocator called allocator and adds some initial resources to it.

    while True:
        print("\n1. Allocate Emergency Resources")
        print("2. Monitor Resource Usage")
        print("3. Add Resource")
        print("4. Update Resource Status")
        print("5. Delete Resource")
        print("6. Exit")

#This part of the code displays a menu of options for the user to interact with the system.
        try:
            choice = input("Enter your choice: ")
            if choice == "1":
                request_id = input("Enter the type of emergency resource needed: ")
                print(allocator.allocate_emergency_resources(request_id))
            
#The try block is used to handle any potential errors that may occur during user input. The user is prompted to enter their choice, and based on the choice:
#If the user chooses option 1, they are prompted to enter the type of emergency resource needed (request_id), 
#and the allocate_emergency_resources method of the EmergencyResourceAllocator instance is called to allocate the requested resource.
            
            elif choice == "2":
                print("\nResource Usage:")
                allocator.monitor_resource_usage()

#If the user chooses option 2, the monitor_resource_usage method of the EmergencyResourceAllocator instance is called to display the details of 
#all resources currently managed by the system.

            elif choice == "3":
                resource_id = int(input("Enter resource ID: "))
                resource_type = input("Enter resource type: ")
                allocator.add_resource(Resource(resource_id, resource_type))
                print("Resource added successfully.")

#If the user chooses option 3, they are prompted to enter the details of a new resource (ID and type), and the add_resource method of the 
#EmergencyResourceAllocator instance is called to add the new resource to the system.

            elif choice == "4":
                resource_id = int(input("Enter resource ID to update status: "))
                new_status = input("Enter new status: ")
                if allocator.update_resource_status(resource_id, new_status):
                    print("Resource status updated successfully.")
                else:
                    print("Resource not found.")

#If the user chooses option 4, they are prompted to enter the ID of the resource whose status they want to update, as well as the new status.
#The update_resource_status method of the EmergencyResourceAllocator instance is called to update the status of the specified resource.
            
            elif choice == "5":
                resource_id = int(input("Enter resource ID to delete: "))
                if allocator.delete_resource_by_id(resource_id):
                    print("Resource deleted successfully.")
                else:
                    print("Resource not found.")

#If the user chooses option 5, they are prompted to enter the ID of the resource they want to delete. The delete_resource_by_id method of the 
#EmergencyResourceAllocator instance is called to delete the specified resource from the system.
            
            elif choice == "6":
                print("Exiting...")
                break

#If the user chooses option 6, the program exits the loop and terminates
            
            else:
                print("Invalid choice. Please try again.")
        except EOFError:
            print("\nExiting...")
            break

#If the user enters an invalid choice, they are notified and prompted to try again.
#The except EOFError block handles the case where the user inputs an EOF (End of File) signal, indicating that they want to exit the program. 
#In this case, the program prints a message and exits the loop.

if __name__ == "__main__":
    main()

#This block ensures that the main function is called when the script is executed as the main program. 
#It allows the code to be reusable as a module if needed.
