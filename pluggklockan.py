import time

def countdown(time_sec, to_do):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    if time_sec == 0:
        print("Det här har du att göra: ")
        for sak in to_do:
            print(sak)

def main():
    to_do = []
    saker = int(input("Hur många saker ska du lägga till på listan?: "))
    for _ in range(saker):
        to_do.append(input("Sak: "))

    while len(to_do) > 0:
        tid = int(input("Hur många sekunder vill du tima: "))
        countdown(tid, to_do)

        to_do.remove(input("Vilken sak vill du ta bort? ")) 
        print(to_do)
    if len(to_do) == 0:
        print("Du har inget att göra, gör vad fan du vill")


if __name__ == "__main__":
    main()
