
# AHU32bit 

Heat Pump Controller


Jak połączyć AHU do sieci lokalnej?
https://youtu.be/T4DrFWYFrpU?si=GrnXhtAI3-qEB1rJ

Jak zaktualizować firmware?
https://youtu.be/g_uAfUcfIxk?si=aBbPRCSxZJbn4i6s

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

W menu "Zabezpieczenia" można wybrać, kiedy zabezpieczenie od przepływu ma być aktywne: "Zawsze", "Tylko gdy defrost" lub "Nigdy".

Dodano menu "Olejowanie" w którym można ustawić interwał olejowania, częstotliwośc (moc) sprężarki w czasie olejowania oraz czas trwania olejowania. Moża też wymusić olejowanie w celach diagnostycznych.

Dodano menu "Odzysk czynnika".

Poprawiono babole:
- wysterowanie przekaźnika pompy obiegowej
- zapisywanie do pamięci energii pobranej

v1.3.4:
- wprowadzono możliwość załącznia CO w zależności od t. zew. (w menu "Ustawienia CO")
- wprowadzono możliwość załączenia pompy obiegowej na zawsze, gdy sterownik jest załączony (w menu "Pompa obiegowa")
- poprawiono identyfikację agregatu 7kW 
- poprawiono wyświetlanie wartości EEV-A i EEV-B dla 7kW
- wprowadzono redukcję obrotów wentylatora przy wyższych temperaturach zewnętrznych dla agregatu 7kW

Poprawka błędów:
- ograniczono zakres nastaw maks. częstotliwość "łagodnego defrostu" od 56Hz do 85Hz
- sporadycznie występujące samoczynne, chwilowe startowanie agregatu, gdy T_cond > 20*C (dot. nowszych jednostek Gree i C&H >2022)
- wyeliminowanie problemów z wyłączaniem agregatu przed osiągnięciem temp zadanej (dot. nowszych jednostek Gree i C&H >2022)
- wyeliminowanie błędu uniemożliwiającego wymuszenie defrostu, gdy T_cond < (T_zew - 6)
- wyeliminowanie błędu uniemożliwiającego fabryczne wywołanie defrostu

v2.0.0:
- dodano nagłówki, ułatwiające poruszanie się po menu
- zmiana kroku nieczułości regulatorów CO i CWU z 0.5C na 0.1C
- uruchomiono funkcję ciepłomierza (konieczny czujnik przepływu!)
- rozdzielenie liczników energii: osobno dla CO i osobno dla CWU
- uruchomiono liczniki COP (konieczny czujnik przepływu i licznik energii!)
- dodano możliwość sterowania pompy obiegowej PWM w trybie stałej delty (menu: "Pompa obiegowa" -> "Tryb pracy PWM" -> "Stała delta")
- dodano stronę parametrów "Pompa obiegowa", gdzie można podejrzeć aktualny stan załączenia pompy obiegowej, wartości PWM i deltę.
- dodano możliwość wywołania olejowania co 3h
- zmieniono krok zadawania stałej mocy pracy pompy obiegowej PWM (było co 10%, jest co 1%)
- poprawiono działania klawiszy + i -, dodając funkcję przytrzymania z autoinkrementacją. Po naszemu: przytrzymać dłużej przycisk, aby wartość sama się zwiększała lub zmniejszała
- dodano menu "Liczniki", w którym można wyzerować wartość licznika energii, ilość defrostów, czas pracy sprężarki i ilość załączeń
- wprowadzono dynamic clamping we wszystkich regulatorach PI (znacznie poprawia dynamikę sterowania)

Poprawka błędów:
- wyeliminowanie błędu załączenia CWU wraz z blokadą załączenia CO od T_zew + dodanie ikonki sygnalizującej wyłączenia od temperatury zewnętrznej.
- próba wyeliminowania błędu uniemożliwiającego wymuszenie defrostu (dot. nowszych jednostek Gree i C&H >2022)

Uwaga!!! Aby liczniki energii działały prawidłowo, od teraz po każdej aktualizacji trzeba w pełni zrestartować system (zdjąć zasilanie z płytki bazowej na min. 20 sek.)

v2.0.1:

Poprawka błędów:
- aktywacja regulatora CWU

v2.0.2:

Poprawka błędów:
- Zapis wartości liczników do pamięci, zaraz po wyzerowaniu w menu. Poprzenio, po zrestowaniu sterownika wartości wracały do wartości sprzed zerowania.
- 
v3.0.5
Video poradnik do aktualizacji: https://youtube.com/playlist?list=PL7Yoy5k4_2IOb-d7yyhNmrepyGyvrlC-8&si=gwIATBIfl5vukARS

Płytka wyświetlacza LCD:
- W menu "Ustawienia CO" dodano funkcję "Mniejsze taktowanie". Poprawia ona fabryczną procedurę zadawania częstotliwości sprężarki. Taktowanie jest jeszcze mniejsze, kosztem delikatnego przeregulowania w stanach dynamicznych. Załączenie funkcji pomaga wyeliminować wyłączenia sprężarki przy przełączaniu z CWU na CO oraz po "olejowaniu".
- Wprowadzono funkcję wyłączenia pompy obiegowej, gdy sterownik jest wyłączony od temperatury zewnętrznej (gdy ikonka "słoneczka" na ekranie głównym jest aktywna). Poprawnie ustawiona funkcja pozwala na poprawę COP całego układu, szczególnie w okresach przejściowych. 
- W menu "Liczniki" dodano możliwość wyboru pracy ciepłomierza: "Zawsze" lub "Gdy praca sprężarki". 
- "Moc oddana" o wartości z zakresu od -100W do 100W jest wyświetlana jako "0W" (zero watt) i nie jest wykorzystywana do liczenia energii oddanej. 
- Uporządkowano menu "Defrost". 
- Proszę nie korzystać! TESTY: Dodano funkcję "Indywidualny defrost", gdzie można ustawić: interwał defrostów, zwłokę defrostu po osiągnięciu progu, próg rozpoczęcia defrostu, maksymalny czas defrostu, próg zakończenia defrostu. Funkcja ogranicza lub eliminuje całkowicie występowanie tzw. suchych lub technicznych defrostów. 
- Dodano możliwość wprowadzenia offsetow w czujnikach temperatury w menu "Ust. czujników".
- Dodano identyfikację jednostki GWH09 (3,5kW).
- Wersję oprogramowania można sprawdzić w menu "Inne".
- Tymczasowo wyłączona zostaje funkcja "łagodny defrost". Funkcja wymaga poprawek.
  
Poprawki błędów:
- Strona "Energia": Gdy brak licznika energii pobranej w systemie, to "Moc pobrana" wyświetlana jest jako "0W", a nie "/W".
- Poprawiono błąd, uniemożliwiający start jednostki gdy temperatura parownika (T_cond)<(-9*C).
- Poprawiono drobne błędy w poruszaniu się po menu.

Konsola:
- Dodano obsługę MQTT
- UWAGA! Wyłączono obsługę Telnet.
- Dodano aplikację webową (AHU32bit Console) umożliwiającą podgląd parametrów online oraz podstawowe sterowanie w sieci lokalnej.
- Wprowadzono możliwość ustawienia stałego IP. 

Znane niedociągnięcia w konsoli:
- jeśli AHU nie połączy się z routerem w ciągu około 1 min, np. po utracie zasilania w domu, to konieczne będzie kliknięcie przycisku "zresetuj komunikację" w konsoli

Po aktualizacji należy zresetować system (płytkę LCD i płytkę bazową).

MQTT dla Home Assistant wspaniale opisał @Łukasz Wojtas.
