import math
import random
import sys

import pygame

W, H = 1024, 600
DARK = 228         
def make_room():
    """Draw a simple haunted room (wall, floor, window, clock, portrait)."""
    s = pygame.Surface((W, H))
    for y in range(400):                                   # wall
        t = y / 400
        pygame.draw.line(s, (int(52 - 18 * t), int(38 - 14 * t), int(46 - 14 * t)), (0, y), (W, y))
    for y in range(400, H):                                # floor
        t = (y - 400) / (H - 400)
        pygame.draw.line(s, (int(52 - 36 * t), int(34 - 25 * t), int(26 - 18 * t)), (0, y), (W, y))
    for i in range(-10, 26):                               # floor boards
        x0 = i * 64
        pygame.draw.line(s, (20, 12, 10), (x0, 400), (W / 2 + (x0 - W / 2) * 1.9, H), 2)

    # window with moon
    pygame.draw.rect(s, (12, 16, 38), (70, 70, 130, 200))
    pygame.draw.circle(s, (228, 228, 206), (156, 130), 17)
    pygame.draw.rect(s, (30, 18, 12), (70, 70, 130, 200), 7)
    pygame.draw.line(s, (30, 18, 12), (135, 70), (135, 270), 5)
    pygame.draw.line(s, (30, 18, 12), (70, 170), (200, 170), 5)

    # portraits with glowing eyes
    for (x, y, w, h) in ((260, 100, 110, 150), (700, 90, 120, 160)):
        pygame.draw.rect(s, (92, 66, 28), (x - 7, y - 7, w + 14, h + 14))
        pygame.draw.rect(s, (30, 26, 24), (x, y, w, h))
        pygame.draw.circle(s, (70, 62, 56), (x + w // 2, y + int(h * 0.38)), int(w * 0.17))
        for dx in (-9, 9):
            pygame.draw.circle(s, (220, 40, 40), (x + w // 2 + dx, y + int(h * 0.37)), 2)

    # grandfather clock
    pygame.draw.rect(s, (70, 42, 24), (470, 80, 90, 320), border_radius=6)
    pygame.draw.circle(s, (222, 212, 170), (515, 127), 27)
    pygame.draw.line(s, (20, 14, 10), (515, 127), (528, 140), 4)
    pygame.draw.line(s, (20, 14, 10), (515, 127), (505, 105), 2)
    pygame.draw.circle(s, (212, 175, 55), (515, 305), 15)

    # staircase
    for i in range(6):
        x = 790 + i * 38
        top = 400 - (i + 1) * 50
        pygame.draw.rect(s, (70, 46, 30), (x, top, W - x, 50))
        pygame.draw.rect(s, (34, 20, 14), (x, top + 14, W - x, 36))
    return s


# ------------------------------------------------------------ horror effect parts
def make_light(radius):
    """Flashlight: a soft circle. Centre removes the darkness, edge keeps it."""
    s = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    for r in range(radius, 0, -2):
        a = int(DARK * (1 - r / radius) ** 0.55)
        pygame.draw.circle(s, (0, 0, 0, a), (radius, radius), r)
    return s


def make_vignette():
    """Dark corners around the screen edges."""
    sw, sh = 64, 40
    small = pygame.Surface((sw, sh), pygame.SRCALPHA)
    for y in range(sh):
        for x in range(sw):
            dx, dy = (x / (sw - 1) - 0.5) * 2, (y / (sh - 1) - 0.5) * 2
            d = min(1.0, math.hypot(dx, dy) / 1.35)
            small.set_at((x, y), (0, 0, 0, int(190 * d ** 3)))
    return pygame.transform.smoothscale(small, (W, H))


def make_wisp():
    """One glowing ghost-light (soft bluish circle)."""
    s = pygame.Surface((70, 70), pygame.SRCALPHA)
    for r in range(34, 0, -2):
        pygame.draw.circle(s, (200, 220, 255, int(60 * (1 - r / 34)) + 2), (35, 35), r)
    return s

def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Haunted House - Horror Environment")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)

    room = make_room().convert()
    lights = [make_light(r) for r in (165, 178, 192)]      # 3 sizes -> flicker
    vignette = make_vignette().convert_alpha()
    wisp_img = make_wisp()
    dark = pygame.Surface((W, H), pygame.SRCALPHA)

    wisps = [dict(x=random.uniform(0, W), y=random.uniform(120, 480),
                  vx=random.uniform(8, 22), ph=random.uniform(0, 6)) for _ in range(6)]

    t = 0.0
    flick, flick_t = 1, 0.0
    bolt, bolt_cd = 0.0, random.uniform(3, 6)              # lightning timers

    while True:
        dt = min(clock.tick(60) / 1000.0, 0.05)
        t += dt
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        # 1) flashlight flicker: pick a random light size every ~0.1 sec
        flick_t -= dt
        if flick_t <= 0:
            flick_t = random.uniform(0.05, 0.14)
            flick = random.choices([0, 1, 2], [2, 5, 3])[0]

        # 2) lightning: starts at random times, fades in 0.45 sec
        bolt_cd -= dt
        if bolt_cd <= 0:
            bolt, bolt_cd = 0.45, random.uniform(6, 14)
        bolt = max(0.0, bolt - dt)

        # 3) floating spirits drift to the right
        for w in wisps:
            w["x"] += w["vx"] * dt
            if w["x"] > W + 40:
                w["x"], w["y"] = -40, random.uniform(120, 480)

        # ---------------- draw ----------------
        screen.blit(room, (0, 0))

        for w in wisps:                                    # spirits (bobbing up/down)
            y = w["y"] + math.sin(t * 0.8 + w["ph"]) * 22
            screen.blit(wisp_img, (w["x"] - 35, y - 35))

        mx, my = pygame.mouse.get_pos()                    # darkness + flashlight hole
        dark.fill((4, 0, 8, DARK))
        lm = lights[flick]
        dark.blit(lm, (mx - lm.get_width() // 2, my - lm.get_height() // 2),
                  special_flags=pygame.BLEND_RGBA_SUB)
        screen.blit(dark, (0, 0))

        screen.blit(vignette, (0, 0))                      # dark corners

        if bolt > 0:                                       # lightning flash
            flash = pygame.Surface((W, H))
            flash.fill((210, 220, 255))
            flash.set_alpha(int(120 * abs(math.sin(bolt * 18)) * bolt / 0.45))
            screen.blit(flash, (0, 0))

        screen.blit(font.render("Move the mouse = flashlight   |   Esc = quit",
                                True, (200, 190, 180)), (20, 15))
        pygame.display.flip()


if __name__ == "__main__":
    main()