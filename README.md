
# AHU32bit 

Heat Pump Controller

v1.0.0:
 
Wersja wyjściowa

v1.1.1:

Dodanie menu "Wyświetlacz LCD" w którym można:
- ustawić wartość podświetlenia
- ustawić wygaszenie podświetlenia po czasie
- ustawić wartość podświetlenia po wygaszeniu
- zał./wył. wyświetlanie częstotliwości pracy sprężarki na ekranie głównym
Dodanie możliwości zablokowania klawiatury poprzez przytrzymanie (~1s) dwóch środkowych przycisków.
Dodanie dłuższego (~1s) przytrzymania przycisku ON/OFF (ochrona przed przypadkowym naciśnięciem).
Możliwość kalibracji czułości przycisków z poziomu konsoli AHU32bit.

Poprawka drobnych błędów:
- likwidacja, występującego czasami, stałego pisku przy wyłączaniu alarmu
- zapis wartości nastawionej temperatury do pamięci przy zaniku zasilania

v1.1.2:

- poprawka błędów

v1.2.3:

Dodanie menu "Pompa obiegowa" w którym można:
- Ustawić postcyrkulację (opóźnienie wyłączenia pompy obiegowej)
- Wysterować stałą mocą pompę wyposażoną w wejście PWM
- Ustawić parametry wyjścia PWM (częstotliwość PWM)
W menu "Defrost" dodano możliwość ograniczenia czasu wymuszonego defrstu oraz dodano opóźnienie wyłączenia przekaźnika sygnalizującego defrost.

W menu "Zabezpieczenia" można wybrać, kidy zabezpieczenie od przypływu ma być aktywne: "Zawsze", "Tylko gdy defrost" lub "Nigdy".

Dodano menu "Olejowanie" w którym można ustawić interwał olejowania, częstotliwośc (moc) sprężarki w czasi olejowania oraz czas trwania olejowania. Moża też wymusić olejowania w celach diagnostycznych.

Dodano menu "Odzysk czynnika".

Poprawiono babole:
- wysterowanie przekaźnika pompy obiegowej
- zapisywanie do pamięci energii pobranej