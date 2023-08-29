
def progress_bar(progress: float, total: float, width: int = 75):
    percent = width * ((progress + 1) / total)
    bar = chr(9608) * int(percent) + "-" * (width - int(percent))
    print(f"\r|{bar}| {(100/width)*percent:.2f}%", end="\r")
    if progress == total: 
        print("\n\n")
