
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

v3.0.6

Płytka wyświetlacza LCD:
- Poprawione wyświetlanie "PWM in" w konsoli i MQTT. Poprzednio wartość była odświeżana tylko gdy na LCD była wyświetlona strona "Pompa obiegowa". 
- Poprawiono zapisywanie wartości parametru "Licz ciepło i moc" z menu "liczniki" do pamięci nieulotnej.
- Wprowadzono możliwość podania wartości przełączenia biegów wentylatora JZ przy pracy CO. 
- Organiczno zakres nastaw czujnika przepływu do 1...1000imp/l
- Do menu "Ustawienia CO" wprowadzono możliwość ustawienie progów zmiany obrotów wentylator jednostki zewnętrznej: "Próg 390/450(490)rpm" oraz "Próg 490/690(790)rpm". Histereza jest stała i wynosi 1C.

Konsola:
- Zmieniono nazwę klienta Mqtt z esp8266client-xxxx na AHU32bit_Client_xxxx
- Poprawiono literówka w słowie "Sprężarka" w zakładce "temperatury".
- Poprawiono wskaźnik temperatury "Falownik" dla jednostki 5kW.
- Wersja konsoli jest wyświetlana w zakładce "Inne"

v3.0.11

UWAGA! Podczas aktualizacji bardzo ważna jest kolejność wgrywania plików!
Video pordanik: https://youtu.be/dtAwadvea6k?si=yNV6m9RhdPWOf3Bx

Płytka wyświetlacza LCD:
- Dodano obsługę GWH12
- Dodano obsługę CH-S24FTXAL-WP
- Dodano zapis parametrów do pamięci przed aktualizacją 
- Zmieniono nazwy temperatur w zakładce 'temperatury' na polskie
- Dodano zabezpieczenie od zamarznięcia parownika. Jeśli różnica temperatury między parownikiem a zewnętrzną przekracza próg z menu ORAZ utrzymuje się przez czas ustawiony w menu, to agregat się wyłączy. Dostępne nastawy w menu "Zabezpieczenia": 
"Min. delta par.-zew.:" oraz "Min. czas błędu par.:"
Alarm sygnalizowany jest na ekranie: Err!(T*)
- Zmieniono dostępne nastawy dla pracy pompy obiegowej: 
"Zawsze gdy ON"
"Gdy praca sprężarki"
"Gdy żądanie CO/CWU"
- Dodano włączenie pompy obiegowej zawsze przy olejowaniu
- Gdy defrost aktywny, to zawór 3D (przekaźnik AUX) zostaje wyłączony. W ten sposób defrost zawsze robiony jest na zład CO.
- Poprawka wysterowania pompy PWM po błędzie zaniku przepływu. 
BYŁO: wartość wynikająca z regulatora delty lub aktualnie ustawiona stała moc.
JEST: 100% mocy
- Zmieniono komendę włączającą najwyższe obroty wentylatora. Lepsza praca przy wyższych mocach i niższych temperaturach.
- Dodano funkcję zapisującą przed aktualizacją aktualne wartości liczników do pamięci.

Konsola:
- W zakładce "Sprężarka" dodano do zegara wyświetlanie częstotliwości zadawanej przez AHU.
- W zakładce "Inne" wyświetlana jest wersja software dla LCD oraz Konsoli.

Po aktualizacji należy zresetować system (płytkę LCD i płytkę bazową).

v3.1.2

Płytka wyświetlacza LCD:
- Uruchomiono funkcję "Indywidualny defrost" w której można indywidualnie sprofilować przegieg defrostu (łagodnie/agresywnie, itp.).

Aby aktywować w pełni "Indywidualny defrost" należy: 
1. Włączyć w menu "Defrost" - > "Indywidualny defrost" -> "Aktywny" na TAK
oraz
2. Włączyć w menu "Defrost" - > "Własny profil" -> "Aktywny" na TAK

Indywidualny defrost jest dwufazowy:
a) faza pierwsza ok. 45Hz, około 3 min,
b) faza II: 65Hz, około 3 min lub szybciej, jeżeli temperatura parownika >20C (lub inna nastawiona).

Dostępne parametry w menu "Indywidualny defrost":
- "Interwał:" czas po którym AHU zacznie sprawdzać temperaturowy próg wyzwolenia defrostu (parametr: "Start defrsotu:"). Wartość domyślna: 90 min. (1,5h).
- "Start defrsotu:" próg temperaturowy wyzwolenia defrostu. Wartość domyślna: -4C. UWAGA! Nie jest to żadna wartość bezwzględna. Jest to różnica temperatur między temperaturą parownika, a temperaturą zewnętrzną!!!
- "Maks. czas defrostu:" czas po którym defrost zostanie ukończony, bez względu na uzyskaną temperaturę parownika. Wartość domyślna: 10 min. Wartość powinna być większa niż suma: 3min + "Faza I (sek.):" + "Faza II (sek.):"
- "Koniec defrostu:" osiągnięcie tej temperatury na parowniku zakończy defrost. Wartość domyślna: 20C
- "Faza I (Hz):" częstotliwość sprężarki podczas fazy I defrostu. Wartość domyślna: 45Hz.
- "Faza I (sek.):" czas trwania fazy I defrostu. Wartość domyślna: 180sek. (3 min)
- "Faza II (Hz):" częstotliwość sprężarki podczas fazy II defrostu. Wartość domyślna: 65Hz.
- "Faza II (sek.):" czas trwania fazy II defrostu. Wartość domyślna: 180sek. (3 min)

Wartości domyślne, są zbliżone do fabrycznych. 

Jeśli defrosty mają być wykonywane częściej, należy zmniejszyć wartość "Interwał" np. z 90 min do 75 min lub zmienić wartość "Start defrostu" (np. zamiast wartości -4C ustawić -3C).
Jeśli defrosty mają być wykonywane rzadziej, należy zwiększyć wartość "Interwał" np. z 90 min do 120 min lub zmienić wartość "Start defrostu" (np. zamiast wartości -4C ustawić -6C).
Jeśli defrost ma przebiegać łagodniej, to należy poeksperymentować z nastawami: "Faza I (Hz):" oraz "Faza II (Hz):". Proszę pamiętać, że zminiejszenie tej wartości może spowodować konieczność wydłużenia defrostu szeczególnie nastawy "Faza II (sek.):" oraz "Maks. czas defrostu:"

Dodatkowo warto zweryfikować nastawy zabezpieczeń w menu "Zabezpieczenia":
- "Minimalna tempeartura rury cieczowej:" próg zadziałania zabezpieczenia od za niskiej temperatury na rurze cieczowej. Wartość należy dobrać do swojej instalacji eksperymentalnie. Wartość domyślna: -5C.
- "Minimalny przepływ:" próg zadziałania zabezpieczenia od za niskiego przepływu. Wartość należy dobrać do swojej instalacji eksperymentalnie. Wartość domyślna: 500l/h.
- "Minimlany czas błędu:" po tym czasie od przekroczenia progu błędu, zostanie zasygnalizowany błąd. Wartość domyślna: 2s. Wartość zalecana: 1-5s.
- "Minimalna delta parownik-zewnętrzna:" próg temperaturowy wyzwolenia zabezpieczenia od zamarznięcia parownika. Wartość domyślna: -10C. UWAGA! Nie jest to żadna wartość bezwzględna. Jest to różnica temperatur między temperaturą parownika, a temperaturą zewnętrzną!!!
- "Minimalny czas błędu parownik-zewnętrzna" po tym czasie od przekroczenia progu błędu "Minimalna delta parownik-zewnętrzna:", zostanie zasygnalizowany błąd. Wartość domyślna: 90 min (1,5h). Wartość zalecana: dłuższa lub równa "Interwał:" w menu "Indywidualny defrost".

Zaleca się ustawić "Postcyrkulację" na minimum 5 min. w menu "Pompa obiegowa".

Defrost indywidualny jest sygnalizowany na ekranie głównym napisem 'CUSTOM' pod ikoną śnieżynką, w momencie jego trwania. 
Odliczany minimalny czas do kolejnego defrostu, widoczny jest w zakładce "Defrost".
Odliczany maksymalny czas do zakończenia trwającego defrostu, widoczny jest w zakładce "Defrost".
Praca sprężarki podczas defrostu indywidualnego rozpoczyna się po około 3 min, od ukazanie się ikonki sygnalizującej defrost ("śnieżynka").
Przełączenie na grzania po zakończeniu defrostu trwa około 3 min.

Aby próbnie wywołać defrost indywidualny, należy wybrać "Wymuś indywidualny defrost". Na rozpoczęcie fazy I defrostu trzeba poczekać około 3min.

"Defrost indywidualny" nie powoduje blokowania defrostu fabrycznego. Jeśli agregat uzna, że musi wykonać "suchy" lub "techniczny" defrost to go wykona.

Warunki rozpoczęcia odliczania w dół do "Indywidualnego defrostu": praca sprężarki ORAZ temperatura parownika <0C. Jeśli w czasie odliczania temperatura parownika będzie >=0C, to czas do defrostu zacznie się liczyć do góry (zwiększać się). Może się tak stać np. nad ranem, gdy temperatura zewnętzna urośnie.

Waruknki rozpoczęcia "Indywidualnego defrostu": odliczony  czas (nastawa "Interwał") ORAZ spełniony warunek temperaturowy (nastawa "Start defrostu").

Warunki zakończenia "Indywidualnego defrostu": osiągniescie zadanej temperatury na parowniku (nastawa "Koniec defrostu:") LUB minięcie nastawy czasu "Faza I (sek.):" + "Faza II (sek.):" LUB minięcie nastawy czasu "Maks. czas defrostu:".

- Menu "Defrost": usunięto funkcję "Łagodny defrost" w starym wydaniu. Zastąpiono ją nową funkcją "Własny profil".

v3.1.3

Aktualizacja od wersji 1.x.x lub 2.x.x :https://www.youtube.com/watch?v=skZjCgosQtY&list=PL7Yoy5k4_2IOb-d7yyhNmrepyGyvrlC-8&index=1&t=78s
Aktualizacja od wersji: 3.x.x: https://youtu.be/dtAwadvea6k?si=yNV6m9RhdPWOf3Bx

UWAGA! Podczas aktualizacji bardzo ważna jest kolejność wgrywania plików!

Płytka wyświetlacza LCD:
- Zmodyfikowano sposób wyświetlania wartości czasu do kolejengo defrostu w zakładce "Defrost". 
BYŁO: wartość w sekundach
JEST: wartość w formacie HH:MM:SS

- Zmodyfikowano sposób wyświetlania wartości czasu do zakończenia defrostu w zakładce "Defrost". 
BYŁO: wartość w sekundach
JEST: wartość w formacie MM:SS

- Dodano możliwość wyboru sposobu raportowania T gaz do JZ w menu "Ust. czujników"->"Pomiar T gaz"->"Sposób pomiaru":
  
a) "Tylko T gaz" - AHU raportuje do JZ T gaz jako rzeczywistą pomierzoną wartość, bezpośrednio z czujnika

b) "Średnia T gaz i T ciecz" - AHU raportuje do JZ i wyświetla T gaz, jako średnią ważoną pomiaru T gaz oraz T ciecz. Wagi również można ustawić w menu 

- Odliczanie do kolejnego defrostu:
BYŁO: resetowanie po wystąpieniu błędu (odliczanie od początku)
JEST: pozostaje poprzednia wartość

- Wzmocniono filtrowanie progów błędu od za niskiej temperatury, przepływu i delty zew.-parownik.

Konsola:

- poprawiono layout zakładki "Inne" na urządzeniach mobilnych (wyświetlanie kafelka z wersją oprogramowania)
- zmieniono zakres wskaźników dla temperatur ujemnych, BYŁO: 0C - 100C, JEST -40C - 100C


v3.2.3

Płytka wyświetlacza LCD:

- Zwiększono czytelność wprowadzania nastaw zadanej temperatury po naciśnięciu klawiszy plus i minus (wyświetlanie dodatkowego okna pop-up).
- Zamieniono przycisk "minus" z "plus" i vice versa, aby był spójny z układem przycisków w konsoli. 
- Zamieniono przycisk "up" z "down" i vice versa.
- Zmieniono miejsce wyświetlania częstotliwości, tak aby była widoczna podczas przeglądania zakładek oraz menu (prawy górny róg). 
- Dodano możliwość wyświetlenia dwóch dodatkowych parametrów na ekranie głównym. Wyboru parametrów w można dokonać w menu "Wyświetlacz LCD" ->"Pokaż na stronie głównej [pole I]" oraz "Pokaż na stronie głównej [pole II]". 
- Poprawiono raportowanie "PWM out" podczas trwania defrostu, itp.
- Poprawiono raportowanie częstotliwości zadanej podczas trwania defrostu oraz olejowania.
- Dodano wyświetlanie przepływu w zakładce "Pompa obiegowa".
- W menu "Inne" można włączyć/wyłączyć "Dźwięk alarmów" (pikanie).
- Wydłużono czas stanu "Aktualnie pod indywidualnym defrostem" o 3 min od momentu wyłączenia sprężarki.
- Korekta wyświetlanych wartość w zakładce "Energia", szczególnie po wyzerowaniu liczników.

Konsola:

- Gdy "Indywidualny defrost" włączony, dodano kafelek odliczający czasy do kolejnego defrostu i do zakończenia defrostu.
- Poprawiono wyświetlanie flagi "Aktualnie pod defrostem" podczas trwania defrostu indywidualnego.
- Poprawiono wysyłanie do konsoli i MQTT flagi "Aktualnie pod indywidualnym defrostem".
- Dodano do protokołu MQTT wysyłanie wersji firmware LCD.
