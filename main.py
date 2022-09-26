import pygame
pygame.init()

screen = pygame.display.set_mode(size=(600, 300))
screen.fill("#00334d")

binary_to_hexadecimals = {
  "0000": "",
  "0001": "1",
  "0010": "2",
  "0011": "3",
  "0100": "4",
  "0101": "5",
  "0110": "6",
  "0111": "7",
  "1000": "8",
  "1001": "9",
  "1010": "A",
  "1011": "B",
  "1100": "C",
  "1101": "D",
  "1110": "E",
  "1111": "F"
}

class BinaryBox():
  def __init__(self, position):
    self.bg_colour = "#06001a"
    self.border_colour = "#666666"
    self.text_colour = "#bfbfbf"
    self.position = position
    self.dimensions = (50, 50)
    self.current_bit = "0"

    self.border_rect = pygame.Rect(self.position, self.dimensions)
    self.background_rect = pygame.Rect((0, 0), (self.dimensions[0]- 10, self.dimensions[1] - 10))
    self.background_rect.center = self.border_rect.center
    self.font = pygame.font.SysFont(None, 40)
    pygame.draw.rect(screen, self.border_colour, self.border_rect, 5)
    self.draw_box()

  def draw_box(self):
    pygame.draw.rect(screen, self.bg_colour, self.background_rect)
    
    binary_box_text = self.font.render(self.current_bit, True, self.text_colour)
    binary_box_text_rect = binary_box_text.get_rect()
    binary_box_text_rect.center = self.background_rect.center
    screen.blit(binary_box_text, binary_box_text_rect)
  
  
  def flip_bit(self):
    if self.current_bit == "0":
      self.current_bit = "1"
    else:
      self.current_bit = "0"
    self.bg_colour, self.text_colour = self.text_colour, self.bg_colour
    self.draw_box()

  def get_current_bit(self):
    return self.current_bit

class HexadecimalDisplay():
  def __init__(self, position, dimensions, font_size):
    self.bg_colour = "#06001a"
    self.text_colour = "#bfbfbf"
    self.current_hexadecimals = ""

    self.font = pygame.font.SysFont(None, font_size)
    self.background_rect = pygame.Rect(position, dimensions)
    self.draw_display()

  def draw_display(self):
    pygame.draw.rect(screen, self.bg_colour, self.background_rect)
    display_text = self.font.render(self.current_hexadecimals, True, self.text_colour)
    display_text_rect = display_text.get_rect()
    display_text_rect.center = self.background_rect.center
    screen.blit(display_text, display_text_rect)
  
  def update_display(self, binary_boxes):
    current_bits = [binary_box.get_current_bit() for binary_box in binary_boxes]
    first_4_bits = f"{current_bits[0]}{current_bits[1]}{current_bits[2]}{current_bits[3]}"
    last_4_bits = f"{current_bits[4]}{current_bits[5]}{current_bits[6]}{current_bits[7]}"
    first_hexadecimal = binary_to_hexadecimals[first_4_bits]
    second_hexadecimal = binary_to_hexadecimals[last_4_bits]
    if first_hexadecimal != "" and second_hexadecimal == "":
      second_hexadecimal = "0"
    self.current_hexadecimals = f"{first_hexadecimal}{second_hexadecimal}"
    self.draw_display()

bar_position_x = 50
bar_position_y = 50
box_width = 50
box_padding = 10

binary_boxes = [BinaryBox((bar_position_x + i*(box_width + box_padding), bar_position_y)) for i in range(8)]

display_dimensions = (70, 70)
display_position_x = bar_position_x + 4 * (box_width + box_padding) - 5 - display_dimensions[0] / 2
hexadecimal_display = HexadecimalDisplay((display_position_x, 130), display_dimensions, 50)

def update_when_keypressed(binary_box_index):
  binary_boxes[binary_box_index].flip_bit()
  hexadecimal_display.update_display(binary_boxes)

while True:
  pygame.display.flip()
  for event in pygame.event.get():
    match event.type:
      case pygame.QUIT:
        pygame.quit()
        exit()
      case pygame.KEYDOWN:
        match event.key:
          case pygame.K_z | pygame.K_a | pygame.K_q | pygame.K_1:
            update_when_keypressed(0)
          case pygame.K_x | pygame.K_s | pygame.K_w | pygame.K_2:
            update_when_keypressed(1)
          case pygame.K_c | pygame.K_d | pygame.K_e | pygame.K_3:
            update_when_keypressed(2)
          case pygame.K_v | pygame.K_f | pygame.K_r | pygame.K_4:
            update_when_keypressed(3)
          case pygame.K_b | pygame.K_g | pygame.K_t | pygame.K_5:
            update_when_keypressed(4)
          case pygame.K_n | pygame.K_h | pygame.K_y | pygame.K_6:
            update_when_keypressed(5)
          case pygame.K_m | pygame.K_j | pygame.K_u | pygame.K_7:
            update_when_keypressed(6)
          case pygame.K_COMMA | pygame.K_k | pygame.K_i | pygame.K_8:
            update_when_keypressed(7)