# Pluggklockan
# Det som jag ska göra är en klocka som kommer att hjälpa dig strukturera din fritid med ditt pluggande. Om du har svårtigheter att lägga ned spelandet eller det gu gör på fritiden med timern som räknar ned hur länge du vill ha en rast.Sedan så kommer den att ta fram en To do lista som gör så att du kan se vad du har att göra och sedan sätta en timer på saken som du bör göra.efter det kan du välja att ta en rast eller göra en till sak på listan. (Du kan inte ta 2 raster efter varrandra)

# språk
# Jag har använt mig av python i mitt programm för att det är det språket som jag har skrivit mest på och vet mest om. Jag har också använd mig av libraries som inport time som gör min timer fungerbar

# hur fungerar det

# timer
# Jag har använt mig av bibloteket time för att göra min timer fungerbart. Detta gör så att i kontrollpanelen ser man en klocka som går ned. Detta är möjligt med bibloteket time och dess funktioner som timeformat som gör att det går från min:sec (00:02 ex.) Detta gör så att man kan räkna ned en timer som man senare kan koppla med listan så man får programmet.
import time

def countdown(time_sec, to_do):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
     
# Programmet handlar om att göra en lista och sedan "checka" av listan som saker som du ska göra. Sedan har du en timer som du kan bestämma hurlång tid du ska göra sakerna som du sen kan ta bort när du har lagt ned den tiden som har lagt inn. Så prorammet använder sig av en slita som är listan med saker som du ska göra. Så du skriver hur många saker som du vill göra och sedan vad som sakerna heter. 
    to_do = []
    saker = int(input("Hur många saker ska du lägga till på listan?: "))
    for _ in range(saker):
        to_do.append(input("Sak: "))

# Ta bort saker från listan
# Detta var det svåraste i programmet tyckte jag. Det som denna del gör är se hur lång tid du vill tima. Efter timerna har tagit slut så ska du ta bort en sak från listan som du har gjort under den tiden. Detta loppas tills det inte finns något i lsitan kvar och sedan så printar det en mening som säjer att du har iget att göra.

    while len(to_do) > 0:
        tid = int(input("Hur många sekunder vill du tima: "))
        countdown(tid, to_do)

        to_do.remove(input("Vilken sak vill du ta bort? ")) 
        print(to_do)
    if len(to_do) == 0:
        print("Du har inget att göra, gör vad fan du vill")
     if __name__ == "__main__":
       main()
