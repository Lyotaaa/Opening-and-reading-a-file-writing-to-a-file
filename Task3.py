def textual_systematisation(number_files, recording_file):
    joint_file = {}
    for i in range(1, number_files + 1):
        name = f"{i}.txt"
        with open(name, "r", encoding="utf-8") as f:
            joint_file[name] = [x for x in f.read().splitlines() if x]
    with open(recording_file, "w", encoding="utf-8") as file:
        for file_number, value in sorted(joint_file.items(), key=lambda x: len(x[1])):
            file.write(file_number + "\n")
            file.write(str(len(value)) + "\n")
            file.write("\n".join(value))
            file.write("\n")
    return


textual_systematisation(3, "4.txt")
