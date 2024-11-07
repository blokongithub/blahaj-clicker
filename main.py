import pygame
import time

pygame.init()

WIDTH, HEIGHT = 600, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blahaj Clicker")

blahaj_img = pygame.image.load("assets/blahaj.png")
cookie_rect = blahaj_img.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2 - 10))

font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 14)
coins = 0
cps = 0

class Upgrade:
    def __init__(self, name, base_cost, cps_increase):
        self.name = name
        self.base_cost = base_cost
        self.cost = base_cost
        self.cps_increase = cps_increase
        self.quantity = 0
        self.rect = None
        
class PowerUp:
    def __init__(self, name, base_cost, clickpower):
        self.name = name
        self.base_cost = base_cost
        self.cost = base_cost
        self.clickpower = clickpower
        self.quantity = 0
        self.rect = None
        
upgrades = [
    Upgrade("DJUNGELSKOG", 10, 0.1),
    Upgrade("SKOGSDUVA", 100, 1),
    Upgrade("KRAMIG", 1000, 10),
    Upgrade("SKOGSDUVA", 10000, 100),
    Upgrade("JÄTTESTOR", 100000, 1000),
    Upgrade("MEGA BLAHAJ", 1000000, 10000),
    Upgrade("GIGA BLAHAJ", 10000000, 100000),
]

powerups = [
    PowerUp("2x click power", 10, 1),
]

last_time = time.time()

LIGHT_BLUE = (91, 206, 250)
PINK = (245, 169, 184)
WHITE = (255, 255, 255)

running = True
while running:
    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time
    
    coins += cps * delta_time
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cookie_rect.collidepoint(event.pos):
                coins += 1 * powerups[0].clickpower
            for index, upgrade in enumerate(upgrades):
                if upgrade.rect and upgrade.rect.collidepoint(event.pos):
                    if coins >= upgrade.cost:
                        coins -= upgrade.cost
                        cps += upgrade.cps_increase
                        upgrade.quantity += 1
                        upgrade.cost = int(upgrade.cost * 1.15)
            for index, upgrade in enumerate(powerups):
                if upgrade.rect and upgrade.rect.collidepoint(event.pos):
                    if coins >= upgrade.cost:
                        coins -= upgrade.cost
                        powerups[0].clickpower = powerups[0].clickpower * 2
                        upgrade.quantity += 1
                        upgrade.cost = int(upgrade.cost * 10)
    
    stripe_height = HEIGHT // 5
        
    window.fill(LIGHT_BLUE)
    pygame.draw.rect(window, PINK, (0, stripe_height, WIDTH, stripe_height))
    pygame.draw.rect(window, WHITE, (0,  stripe_height * 2, WIDTH, stripe_height))
    pygame.draw.rect(window, PINK, (0, stripe_height * 3, WIDTH, stripe_height))
    pygame.draw.rect(window, LIGHT_BLUE, (0, stripe_height * 4, WIDTH, stripe_height))
                        
    window.blit(blahaj_img, cookie_rect)
    
    coin_text = font.render(f"Coins: {int(coins)}", True, (0, 0, 0))
    window.blit(coin_text, (10, 20))
    
    cps_text = font.render(f"CPS: {round(cps, 1)}", True, (0, 0, 0))
    window.blit(cps_text, (10, 50))
    
    for index, upgrade in enumerate(upgrades):
        x = 10
        y = 100 + index * 70
        width = 200
        height = 60
        upgrade_rect = pygame.Rect(x, y, width, height)
        upgrade.rect = upgrade_rect
        
        pygame.draw.rect(window, (200, 200, 200), upgrade_rect)
        pygame.draw.rect(window, (0, 0, 0), upgrade_rect, 2)
        
        upgrade_name_text = font2.render(
            f"{upgrade.name} (Cost: {upgrade.cost}, Owned: {upgrade.quantity})", True, (0, 0, 0)
        )
        window.blit(upgrade_name_text, (x + 5, y + 35))
        
    for index, upgrade in enumerate(powerups):
        x = 350
        y = 100 + index * 70
        width = 200
        height = 60
        upgrade_rect = pygame.Rect(x, y, width, height)
        upgrade.rect = upgrade_rect
        
        pygame.draw.rect(window, (200, 200, 200), upgrade_rect)
        pygame.draw.rect(window, (0, 0, 0), upgrade_rect, 2)
        
        upgrade_name_text = font2.render(
            f"{upgrade.name} (Cost: {upgrade.cost}, Owned: {upgrade.quantity})", True, (0, 0, 0)
        )
        window.blit(upgrade_name_text, (x + 5, y + 35))
        
            
    pygame.display.flip()
    pygame.time.delay(16)
    
pygame.quit()