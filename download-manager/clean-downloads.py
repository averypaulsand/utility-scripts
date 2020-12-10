import subprocess
from pathlib import Path
import sys

# global path variables
downloads_dir = str(Path('/Users/ave/Downloads'))
music_dir = str(Path('/Users/ave/Music/Library'))
movies_dir = str(Path('/Users/ave/Music/Movies'))
pictures_dir = str(Path('/Users/ave/Pictures/'))
readings_dir = str(Path('/Users/ave/Readings/'))
downloads_zips = Path('/Users/ave/Downloads').glob('**/*.zip')
#downloads_mp3s = Path('/Users/ave/Downloads').glob('**/*.mp3')
#downloads_mp4s = Path('/Users/ave/Downloads').glob('**/*.mp4')
#downloads_pdfs = Path('/Users/ave/Downloads').glob('**/*.pdf')


def clean_downloads():
    unzip()
    # remove_dmgs()


# unzips any zipped files and then moves the unzipped folder to trash
# depends on cli trash library
def unzip():
    for filepath in downloads_zips:
        # removes ".zip"
        dst_dir = str(filepath)[:-4]
        subprocess.run(["mkdir", str(dst_dir)])
        subprocess.run(["unzip", str(filepath), "-d", str(dst_dir)])
        move_music(dst_dir)
        subprocess.run(["trash", str(filepath)])
        #subprocess.run(["trash", "/Users/ave/Downloads/__MACOSX"])


def move_music(music_folder):
    subprocess.run(["cp", "-r", str(music_folder), music_dir])
    subprocess.run(["trash", str(music_folder)])


# calls function when .py script is executed
if __name__ == '__main__':
    clean_downloads()
