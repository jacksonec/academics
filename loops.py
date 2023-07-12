def good_loop():
    loop_count = 0
    keep_looping = 'y'
    while keep_looping == 'y':
        loop_count += 1
        keep_looping = input("Keep looping? [y/n] ")
        print(f"You have pleased the spirits of programming with your good loop {loop_count} times.")
        keep_looping = keep_looping[0]
        keep_looping = keep_looping.lower()

    print("See ya later.")

def bad_loop():
    loop_count = 0
    keep_looping = 'y'
    while 1 == 1:
        loop_count += 1
        keep_looping = input("Keep looping? [y/n] ")
        print(f"You have angered the spirits of programming with your bad loop {loop_count} times.")
        keep_looping = keep_looping[0]
        keep_looping = keep_looping.lower()

        if keep_looping != 'y':
            print ("Oh, thank goodness you are stopping. This is agony.")
            break



# Main code here
exit_program = False
while not exit_program:
    print("Welcome to Pointless Loop Program 1.0!")
    print("Would you like to do a bad loop, good loop, or quit like a quitter?")
    choice = input(
                   f"1) Good Loop\n"
                   f"2) Bad loop\n"
                   f"3) Quit\n"
                   f"[1/2/3]? "
                   )

    if choice == '1':
        good_loop()
    elif choice == '2':
        bad_loop()
    elif choice == '3':
        exit_program = True
        input("Lame...")
    else:
        input("Whatever you just typed was not an option. Try again. Press enter.")
