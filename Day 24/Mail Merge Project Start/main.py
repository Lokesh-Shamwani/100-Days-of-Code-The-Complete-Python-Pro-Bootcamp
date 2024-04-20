

with open("./Input/Letters/starting_letter.txt") as letter_file:
    with open("./Input/Names/invited_names.txt") as names_file:
        content = letter_file.read()
        for guest_name in names_file:
            guest_name = guest_name.replace(
                "\n", ""
            )  # to remove '\n' at the end of name
            new_msg = content.replace("[name]", guest_name)
            with open(f".\Output\ReadyToSend\{guest_name}.txt", "w") as guest_file:
                guest_file.write(new_msg)


