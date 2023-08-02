from Simulation import Simulation

def main():
    # Default parameters
    n = 10000
    alpha = 0.01
    recovery_days = 14
    transmission_rate = 0.015
    fatality_rate = 0.03
    initial_setting = 0.01

    option = ""
    while option != "0":
        displayMenu()
        option = input()
        if option == "1":
            s = Simulation(5, n, alpha, recovery_days, transmission_rate, fatality_rate, initial_setting)
            days=int(input("How many days would you like the simulation to run: "))
            s.run(days)
        elif option=="2":
            s = Simulation(60, n, alpha, recovery_days, transmission_rate, fatality_rate, initial_setting)
            days = int(input("How many days would you like the simulation to run: "))
            s.run(days)
        elif option=="3":
            opt=""
            while opt!="0":
                print(f"""
=== === === === ===
n = {n}
ALPHA = {alpha}
RECOVERY_DAYS = {recovery_days}
TRANSMISSION_RATE = {transmission_rate}
FATALITY_RATE = {fatality_rate}
INITIAL_SETTING = {initial_setting}
=== === === === ===      

                        === === === === ===
                        0. Return to previous menu
                        1. Modify parameters
                        === === === === ===
                        """)
                opt=input()
                if opt=="1":
                    op=""
                    while op!="0":
                        print("""
                            === === === === ===
                            1, n
                            2. ALPHA
                            3. RECOVERY_DAYS
                            4. TRANSMISSION_RATE
                            5. FATALITY_RATE
                            6. INITIAL_SETTING
                            === === === === ===
                            0. Return to previous menu
                            """)
                        op=input()
                        if op=="1":
                            n=int(input("n: "))
                        elif op=="2":
                            alpha=float(input("ALPHA: "))
                        elif op=="3":
                            recovery_days=float(input("RECOVERY_DAYS: "))
                        elif op=="4":
                            transmission_rate=float(input("TRANSMISSION_RATE: "))
                        elif op=="5":
                            fatality_rate=float(input("FATALITY_RATE: "))
                        elif op=="6":
                            initial_setting=float(input("INITIAL_SETTING: "))

def displayMenu():
    print("""
                _____ ______      _______ _____        __  ___   
               / ____/ __ \ \    / |_   _|  __ \      /_ |/ _ \  
              | |   | |  | \ \  / /  | | | |  | |______| | (_) | 
              | |   | |  | |\ \/ /   | | | |  | |______| |\__, | 
              | |___| |__| | \  /   _| |_| |__| |      | |  / /  
               ___________/   \/   |_____|______   _   |_| /_/   
              / ____(_)               | |     | | (_)            
             | (___  _ _ __ ___  _   _| | __ _| |_ _  ___  _ __  
              \___ \| | '_ ` _ \| | | | |/ _` | __| |/ _ \| '_ \ 
              ____) | | | | | | | |_| | | (_| | |_| | (_) | | | |
             |_____/|_|_| |_| |_|\__,_|_|\__,_|\__|_|\___/|_| |_|                                                                                                                                    
                              
                              By Maxi Guillermo
                              
                            === === === === ===
                1. Run simulation with lockdown (INTERACTIONS = 5)
              2. Run simulation with no lockdown (INTERACTIONS = 60)
                            === === === === ===
                         3. View/Modify Parameters
                            === === === === ===
                              0. Exit Program
                            """)

if __name__ == "__main__":
    main()
