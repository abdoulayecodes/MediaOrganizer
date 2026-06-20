from pathlib import Path
import shutil

folder = Path(r"YOUR_FOLDER")

images = [".png", ".jpg", ".jpeg"]
videos_audio = [".mp4", ".mp3"]
pdf = [".pdf"]


for file in folder.iterdir():

    # Ignore folders
    if file.is_file():

        extension = file.suffix.lower()

        # Choose destination folder
        if extension in images:
            destination = folder / "Images"

        elif extension in videos_audio:
            destination = folder / "VideosAudio"

        elif extension in pdf:
            destination = folder / "PDF"

        else:
            print(f"Unknown extension: {file.name}")
            continue

        # Create folder if needed
        destination.mkdir(exist_ok=True)

        # Move file
        shutil.move(str(file), destination / file.name)

        print(f"{file.name} moved to {destination.name}")

print("Done.")
