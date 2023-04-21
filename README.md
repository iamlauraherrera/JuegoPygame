# JuegoPygame
Curso de programacion de Udemy con Python, creación de juegos con Pygame

¿De qué trata?

Este es un código Python que utiliza la biblioteca Pygame para crear un juego en 2D llamado "Spaguetti Head". El código importa varias clases para elementos del juego, incluyendo las clases Hero, Suelo (suelo), Bola_hielo (bola de hielo) y Enemy. También importa la biblioteca Pygame e inicializa para empezar a crear una ventana para mostrar el juego. La ventana del juego está configurada para ser de 800 píxeles de ancho y 600 píxeles de alto. El color de fondo está configurado como una tonalidad de azul. También se inicializa un reloj para optimizar las animaciones. El juego tiene efectos de sonido que se cargan utilizando el módulo mixer de Pygame. Los efectos de sonido incluyen game over, explosión, disparo y colisión con enemigos.

El juego tiene un botón de inicio y un botón de salida que se crean como instancias de una clase Button. Cuando se hace clic en el botón de inicio, comienza el juego. El jugador tiene tres vidas y puede disparar bolas de hielo para destruir enemigos. Los enemigos se generan aleatoriamente en la pantalla. El juego lleva un registro de la puntuación del jugador y la muestra en la pantalla junto con el número de vidas restantes. El juego verifica las colisiones entre el jugador y el suelo, el jugador y los enemigos, y la bola de hielo del jugador y los enemigos.

El juego tiene un bucle while que continúa hasta que el jugador se queda sin vidas. El bucle ejecuta dos sub-bucles, uno para la pantalla de inicio y otro para el juego real. La pantalla de inicio muestra los botones de inicio y salida, mientras que la pantalla del juego muestra al jugador, los enemigos y la información del juego.

# English.

This is a Python code that uses the Pygame library to create a 2D game called "Spaguetti Head." The code imports several classes for game elements, including the Hero, Suelo (ground), Bola_hielo (ice ball), and Enemy classes. It also imports the Pygame library and initializes it to start creating a window to display the game. The game window is set to be 800 pixels wide and 600 pixels high. The background color is set to be a shade of blue. A clock is also initialized to optimize the animations. The game has sound effects that are loaded using Pygame's mixer module. The sound effects include game over, explosion, shooting, and enemy collision.

The game has a start button and an exit button that are created as instances of a Button class. When the start button is clicked, the game begins. The player has three lives and can shoot ice balls to destroy enemies. Enemies are randomly generated on the screen. The game keeps track of the player's score and displays it on the screen along with the number of lives remaining. The game checks for collisions between the player and the ground, the player and enemies, and the player's ice ball and enemies.

The game has a while loop that continues until the player runs out of lives. The loop runs two sub-loops, one for the start screen and one for the actual game. The start screen displays the start and exit buttons, while the game screen displays the player, enemies, and game information.
