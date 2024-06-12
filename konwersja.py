import sys
import json
import yaml
import xmltodict



def podaj_plik_json(plik_wej):
    try:
        with open(plik_wej, 'r') as plik:
            a = json.load(plik)
            return a
    except json.JSONDecodeError:
        print("Taki plik nie istnieje, sprawdź nazwę")
    except FileNotFoundError:
        print("Taki plik nie istnieje")



def zapisz_do_pliku_json(a, plik_wyj):
    try:
        with open(plik_wyj, 'w') as plik:
            json.dump(a, plik)
        print("Udana konwersja do formatu JSON")
    except:
        print("Błąd")



def podaj_plik_yml(plik_wej):
    try:
        with open(plik_wej, 'r') as plik:
            a = yaml.safe_load(plik)
            return a
    except yaml.YAMLError:
        print("Taki plik nie istnieje, sprawdź nazwę")
    except FileNotFoundError:
        print("Taki plik nie istnieje")



def zapisz_do_pliku_yml(a, plik_wyj):
    try:
        with open(plik_wyj, 'w') as plik:
            yaml.dump(a, plik)
        print("Udana konwersja do formatu YML")
    except:
        print("Błąd")



def podaj_plik_xml(plik_wej):
    try:
        with open(plik_wej, 'r') as plik:
            a = xmltodict.parse(plik.read())
            return a
    except FileNotFoundError:
        print("Taki plik nie istnieje")



def zapisz_do_pliku_xml(a, plik_wyj):
    try:
        with open(a, 'w') as plik:
            xml_str = xmltodict.unparse(plik_wyj, pretty=True)  # dodatkowy parametr by plik był czytylny
            plik.write(xml_str)
        print("Udana konwersja do formatu XML")
    except:
        print("Błąd")



def main():

    if len(sys.argv) != 3:
        print("Dozwolone sa tylko dwa argumenty")
        return
    else:
        pass

    plik_wej = sys.argv[1]
    plik_wyj = sys.argv[2]

    a = None

    if plik_wej.endswith('.json'):
        a = podaj_plik_json(plik_wej)
    elif plik_wej.endswith('.yml'):
        a = podaj_plik_yml(plik_wej)
    elif plik_wej.endswith('.xml'):
        a = podaj_plik_xml(plik_wej)
    else:
        print("Błędny format pliku.")
        return

    if plik_wyj.endswith('.json'):
        zapisz_do_pliku_json(a, plik_wyj)
    elif plik_wyj.endswith('.yml'):
        zapisz_do_pliku_yml(a, plik_wyj)
    elif plik_wyj.endswith('.xml'):
        zapisz_do_pliku_xml(a, plik_wyj)
    else:
        print("Błędny format pliku.")
        return



if __name__ == '__main__':
    main()