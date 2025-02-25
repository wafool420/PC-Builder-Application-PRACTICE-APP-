#Classes

class Computer:
    def __init__(self, Build):
        self.cpu = Build.cpu
        self.gpu = Build.gpu
        self.ram = Build.ram
        self.storage = Build.storage
        self.motherboard = Build.motherboard
        self.psu = Build.psu

class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None
        self.motherboard = None
        self.psu = None

    def cpu_model(self, cpu): 
        self.cpu = cpu
        if cpu in Display.parts_list["CPU"]:
            return self
        else:
            print("Out of stock / Invalid Part")
            return self.cpu_model(input("Cpu Model: "))

    def gpu_model(self, gpu):
        self.gpu = gpu
        if gpu in Display.parts_list["GPU"]:
            return self
        else:
            print("Out of stock / Invalid Part")
            return self.gpu_model(input("Gpu Model: "))

    def ram_model(self, ram):
        self.ram = ram
        if ram in Display.parts_list["RAM"]:
            return self
        else:
            print("Out of stock / Invalid Part")
            return self.ram_model(input("Ram Model: "))

    def storage_model(self, storage):
        self.storage = storage
        if storage in Display.parts_list["Storage"]:
            return self
        else:
            print("Out of stock / Invalid Part")
            return self.storage_model(input("Storage Model: "))

    def motherboard_model(self, motherboard):
        self.motherboard = motherboard
        if motherboard in Display.parts_list["Motherboard"]:
            return self
        else:
            print("Out of stock / Invalid Part")
            return self.motherboard_model(input("Motherboard Model: "))

    def psu_model(self, psu):
        self.psu = psu
        if psu in Display.parts_list["PSU"]:
            return self
        else:
            print("Out of stock / Invalid Part")
            return self.psu_model(input("Psu Model: "))

    def BuildPC(self):
        return Computer(self)

class Display:

    parts_list: dict = {
        'CPU': ['Intel Core i9-14900K', 'AMD Ryzen 9 7950X', 'Intel Core i7-13700K', 'AMD Ryzen 7 7800X3D', 'Intel Core i5-13600K'],
        'GPU': ["NVIDIA RTX 4090","AMD Radeon RX 7900 XTX","NVIDIA RTX 4080 Super","AMD Radeon RX 7800 XT","NVIDIA RTX 4070 Ti Super"],
        'RAM': ["G.Skill Trident Z5 RGB DDR5-6000","Corsair Vengeance DDR5-5600","Kingston Fury Beast DDR4-3200","Crucial Ballistix DDR4-3600","TeamGroup T-Force Delta RGB DDR5-6400"],
        'Storage': ["Samsung 990 Pro 2TB NVMe SSD", "WD Black SN850X 1TB NVMe SSD", "Kingston NV2 2TB NVMe SSD", "Crucial P5 Plus 1TB NVMe SSD", "Seagate FireCuda 530 2TB NVMe SSD"],
        'Motherboard': ["Asus ROG Strix X670E-E Gaming WiFi", "MSI MPG B650 Tomahawk WiFi", "Gigabyte Z790 AORUS Master", "Asus TUF Gaming B650-Plus", "ASRock X670E Taichi"],
        'PSU': ["Corsair RM850x 850W 80+ Gold", "EVGA SuperNOVA 1000W 80+ Platinum", "Seasonic Focus GX-750 80+ Gold", "Cooler Master MWE 750W 80+ Bronze", "Thermaltake Toughpower GF3 1200W 80+ Gold"]
    }


    def display_stock(self):

        print(f'''
        Welcome to our PC Shop!

        Our Stock:

        ''')

        print("CPU: ")
        for x in self.parts_list["CPU"]:
            print(f"{x}")
        print("\nGPU: ")
        for x in self.parts_list["GPU"]:
            print(f"{x}")
        print("\nRam: ")
        for x in self.parts_list["RAM"]:
            print(f"{x}")
        print("\nStorage: ")
        for x in self.parts_list["Storage"]:
            print(f"{x}")
        print("\nMotherboard: ")
        for x in self.parts_list["Motherboard"]:
            print(f"{x}")
        print("\nPSU: ")
        for x in self.parts_list["PSU"]:
            print(f"{x}")

        print("\n\nEnjoy Building!\n")
    
    def display_parts(self):
        print("\nYour PC: \n")
        for parts, models in pc.__dict__.items():
            print(f"{parts}: {models}")
        print(f"\nHave fun gaming! :)")


#Main

isBuilding = True

Display = Display()
Display.display_stock()

while isBuilding:

    Computer_Builder = ComputerBuilder()
    pc = (Computer_Builder.cpu_model(input("Cpu Model: "))
                                .gpu_model(input("Gpu Model: "))
                                .ram_model(input("Ram Model: "))
                                .storage_model(input("Storage Model: "))
                                .motherboard_model(input("Motherboard Model: "))
                                .psu_model(input("PSU Model: ")).BuildPC())

    Display.display_parts()

    if input("Would you like to try again?: ").upper() == 'YES':
        pass
    else:
        print("Hope you enjoyed your build! :)")
        isBuilding = False



    

