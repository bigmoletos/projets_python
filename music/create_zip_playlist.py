# import zipfile
import os
from pydub import AudioSegment


def create_segments_and_zip():
    """
    Ce script extrait des segments spécifiques de plusieurs fichiers audio et les compile dans un fichier zip.

    Étapes :
    1. Charger les fichiers audio depuis les chemins spécifiés.
    2. Extraire des segments spécifiques de chaque fichier audio.
    3. Enregistrer les segments extraits dans un répertoire de sortie.
    4. Créer un fichier zip contenant tous les segments extraits.
    """

    # Chemins des fichiers audio (remplacer par les chemins réels sur ton ordinateur)
    files = {
        "September":
        "N:/programmation/projets_python/music/playlist/September.mp3",
        "Hold the Line":
        "N:/programmation/projets_python/music/playlist/Toto - Hold the Line (Audio HQ).mp3",
        "Sweet Dreams":
        "N:/programmation/projets_python/music/playlist/Sweet Dreams (Are Made of This) (Remastered).mp3",
        "Sarà perché ti amo":
        "N:/programmation/projets_python/music/playlist/Ricchi E Poveri - Sarà perché ti amo (Audio).mp3",
        "Mambo No. 5":
        "N:/programmation/projets_python/music/playlist/Lou Bega - Mambo No. 5 (A Little Bit of...).mp3",
        "All Day and Night":
        "N:/programmation/projets_python/music/playlist/Europa (Jax Jones & Martin Solveig) - All Day and Night with Madison Beer.mp3",
        "Gimme! Gimme! Gimme!":
        "N:/programmation/projets_python/music/playlist/ABBA - Gimme! Gimme! Gimme! (A Man After Midnight).mp3",
        "Love Today":
        "N:/programmation/projets_python/music/playlist/MIKA - LOVE TODAY.mp3",
        "Beggin'":
        "N:/programmation/projets_python/music/playlist/Maneskin-Beggin (CD Audio).mp3",
        "I Love Rock 'n' Roll":
        "N:/programmation/projets_python/music/playlist/Joan Jett - I Love Rock n Roll.mp3",
        "La tribu de Dana":
        "N:/programmation/projets_python/music/playlist/Manau - La tribu de Dana (Clip Officiel remasterisé).mp3",
        "In Hell I'll Be in Good Company":
        "N:/programmation/projets_python/music/playlist/The Dead South - In Hell Ill Be In Good Company [Official Music Video].mp3"
    }

    # Définir les segments à extraire pour chaque chanson
    segments = {
        "September": (60000, 120000),  # Refrain avec les cuivres entraînants
        "Hold the Line": (60000, 120000),  # Solo de guitare et refrain
        "Sweet Dreams": (0,
                         60000),  # Introduction avec le synthé caractéristique
        "Sarà perché ti amo": (60000, 120000),  # Refrain mélodique et doux
        "Mambo No. 5": (60000, 120000),  # Partie avec le swing et les cuivres
        "All Day and Night":
        (60000, 120000),  # Moment énergique avec une montée en intensité
        "Gimme! Gimme! Gimme!": (60000,
                                 120000),  # Refrain entraînant et groovy
        "Love Today": (60000,
                       120000),  # Moment accrocheur et joyeux du refrain
        "Beggin'": (60000,
                    120000),  # Moment puissant avec un groove rock distinctif
        "I Love Rock 'n' Roll":
        (60000, 120000),  # Passage énergique avec le riff de guitare
        "La tribu de Dana":
        (60000, 120000
         ),  # Partie dynamique avec le mélange de rap et de musique celtique
        "In Hell I'll Be in Good Company":
        (60000, 120000)  # Moment caractéristique de la chanson
    }

    output_files = []

    # Chemin du répertoire de sortie
    output_dir = "N:/programmation/projets_python/music/segments_playlist"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Extraire et sauvegarder les segments
    for song, (start, end) in segments.items():
        if os.path.exists(files[song]):
            audio = AudioSegment.from_mp3(files[song])
            segment = audio[start:end]
            output_file = os.path.join(
                output_dir,
                "segment_" + song.replace(' ', '_').replace('\'', '') + ".mp3")
            segment.export(output_file, format="mp3")
            output_files.append(output_file)
        else:
            print(f"File not found: {files[song]}")

    # Vérifier les segments extraits
    print("Segments extraits :", output_files)

    # Créer un fichier zip contenant tous les segments
    zip_path = os.path.join(output_dir, "segments_playlist.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in output_files:
            zipf.write(file, arcname=os.path.basename(file))

    print(f"Fichier zip créé : {zip_path}")


if __name__ == "__main__":
    create_segments_and_zip()
