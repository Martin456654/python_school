def load_data():
    # Vstupní bod pro načtení dat od uživatele
    print("=================================")
    print("      Načtěte data              ")
    print("=================================")
    
    # Inicializace slovníku pro ukládání jmen a věků
    data = {'names': [], 'ages': []}
    
    # Cyklus pro načtení jmen a věků od uživatele a uložení do slovníku
    for i in range(5):
        # Načtení jména od uživatele
        while True:
            name = input(f"Jméno {i + 1}: ")
            # Kontrola, zda bylo zadáno neprázdné jméno
            if name.strip():
                data['names'].append(name)
                break
            else:
                print("Jméno nesmí být prázdné.")
        
        # Načtení věku od uživatele
        while True:
            try:
                age = int(input(f"Věk pro {name}: "))
                # Kontrola, zda byl zadán nezáporný věk
                if age >= 0:
                    data['ages'].append(age)
                    break
                else:
                    print("Věk musí být nezáporné číslo.")
            except ValueError:
                print("Neplatný vstup. Zadejte prosím platné číslo.")
                
    return data

def print_data(data):
    # Výstupní bod pro vypsání načtených dat
    print("\n=================================")
    print("        Vypsaná data            ")
    print("=================================")
    
    # Výpis jmen a věků uložených ve slovníku
    for name, age in zip(data['names'], data['ages']):
        print(f"Jméno: {name}, Věk: {age}")

def calculate_average_age(data):
    # Výstupní bod pro výpočet průměrného věku
    print("\n=================================")
    print("       Vypočítejte průměr       ")
    print("=================================")
    
    # Výpočet celkového součtu věků
    sum_ages = sum(data['ages'])
    # Výpočet průměrného věku
    average_age = sum_ages / len(data['names'])
    # Výpis průměrného věku
    print(f"Průměrný věk: {average_age}")

if __name__ == "__main__":
    try:
        # Vstupní bod pro spuštění aplikace
        print("=================================")
        print("   Vítejte v konzolové aplikaci  ")
        print("=================================")
        
        # Načtení dat od uživatele
        data = load_data()
        # Výpis načtených dat
        print_data(data)
        # Výpočet průměrného věku
        calculate_average_age(data)

    except Exception as e:
        # Zachycení a výpis chyby
        print(f"Nastala obecná chyba: {e}")

    # Čekání na stisknutí klávesy pro ukončení programu
    input("Stiskněte libovolnou klávesu pro ukončení.")