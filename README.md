<p align="center">
  <img src="https://www.mirea.ru/upload/medialibrary/c1a/MIREA_Gerb_Colour.jpg" alt="MIREA" width="80"/>
  <img src="https://www.mirea.ru/upload/medialibrary/26c/FTI_colour.jpg" alt="IPTIP" width="137"/> 
</p>

# Математика для программирования (часть 1/2) [I.24-25]

## Практическое занятие 7 Управление объектом с помощью прерываний в обстановке.
Работу выполнил студент `Папин Николай Алексеевич` группы `ЭФБО-02-22`.

## Описание проекта

### Функции
- [x] Матрица лабиринта
- [x] Перемещение игрока
- [x] Коллизия со стенами
- [x] Заавершение при выходе
- [x] Дальность обзора (выход маскируется) 

### Работа с прерываниями
В игре прерывания используются для обработки нажатия клавиш. Получая из `pygame` массив нажатых клавиш, мы определяем направление движения, после чего либо разрешаем его, либо прерываем (в зависимости от наличия препятствия). Коллизия с выходом на карте приводит к завершению игры.

```python
def think(self):
    keys = pygame.key.get_pressed()

    # Вычисляем, в какую клетку должен попасть игрок
    new_x, new_y = self.player.x, self.player.y

    if keys[pygame.K_LEFT] and self.player.x > 0:
        new_x -= MAZE_SIZE
    elif keys[pygame.K_RIGHT] and self.player.x < SCR_WIDTH - MAZE_SIZE:
        new_x += MAZE_SIZE
    elif keys[pygame.K_UP] and self.player.y > 0:
        new_y -= MAZE_SIZE
    elif keys[pygame.K_DOWN] and self.player.y < SCR_HEIGHT - MAZE_SIZE:
        new_y += MAZE_SIZE

    # Отменяем движение, если оно попадает в стену
    for cell in self.cells:
        if cell.x == new_x and cell.y == new_y:
            if cell.color == COL_PRIMARY:
                return

    # Завершаем игру, если игрок попадает в выход
    if self.exit.x == new_x and self.exit.y == new_y:
        pygame.quit()

    # Обновление позиции
    self.player.x, self.player.y = new_x, new_y
    self.player_pos = self.player.x, self.player.y
```
