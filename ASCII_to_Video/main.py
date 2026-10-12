import sys
import cv2
import numpy as np
import pygame


def run_code_art(video_path, audio_path):
    COLUMNS = 200
    ROWS = 100
    FONT_SIZE = 8

    CODE_SYMBOLS = [
        "def",
        "for",
        "if",
        "print",
        "x",
        "=",
        "+",
        "return",
        "import",
        "class",
        "{",
        "}",
        ";",
        "0",
        "1",
        "ai",
    ]

    pygame.init()
    pygame.mixer.init()

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(
            f"Erore: Nu s-a putut deschide fișierul video '{video_path}'. Verifică"
            " dacă există în folder!"
        )
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0 or np.isnan(fps):
        fps = 30.0

    font = pygame.font.SysFont("Courier New", FONT_SIZE, bold=True)
    char_test_surface = font.render("X", True, (255, 255, 255))
    char_width = char_test_surface.get_width()
    char_height = char_test_surface.get_height()

    screen_width = COLUMNS * char_width
    screen_height = ROWS * char_height

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"Code Art Animation - Rulăm: {video_path}")

    clock = pygame.time.Clock()

    try:
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play(-1)
        print(f"Redare audio: {audio_path}")
    except Exception as e:
        print(f"Atenție: Nu s-a putut rula fișierul audio ({e}).")

    running = True
    frame_counter = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        small_frame = cv2.resize(frame, (COLUMNS, ROWS))
        screen.fill((5, 5, 5))

        for y in range(ROWS):
            for x in range(COLUMNS):
                b, g, r = small_frame[y, x]
                color = (int(r), int(g), int(b))

                symbol_index = (x + y + frame_counter // 6) % len(CODE_SYMBOLS)
                symbol = CODE_SYMBOLS[symbol_index]

                char_surface = font.render(symbol[0], True, color)
                screen.blit(char_surface, (x * char_width, y * char_height))

        pygame.display.flip()
        frame_counter += 1
        clock.tick(fps)

    cap.release()
    pygame.quit()
    sys.exit()


def main():
    print("========================================")
    print("      SELECTEAZĂ PIESA CODE ART        ")
    print("========================================")
    print(" 1. Caramella Girls - Caramelldansen HD Version (Swedish Original)")
    print(" 2. Smile - Butterfly")
    print("========================================")

    optiune = input("Introdu numărul opțiunii (1 sau 2): ").strip()

    if optiune == "1":
        video_file = "video_audio/Caramella_Video_Anime.mp4"
        audio_file = "video_audio/Caramella_Audio_Anime.mp3"
    elif optiune == "2":
        video_file = "video_audio/Butterfly_Video.mp4"
        audio_file = "video_audio/Butterfly_Audio.mp3"
    else:
        print("Ceva nu merge")

    run_code_art(video_file, audio_file)


if __name__ == "__main__":
    main()
