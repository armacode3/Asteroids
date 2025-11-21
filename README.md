# Asteroids

A Python implementation of the classic arcade game "Asteroids," built using the `pygame` library. This project features a fully playable game loop with player movement, shooting mechanics, and asteroid collision physics.

## Features

* **Player Mechanics**:
    * **Movement**: Accelerate, decelerate, and rotate your ship using keyboard controls.
    * **Combat**: Fire projectiles to destroy incoming asteroids.
    * **Cooldowns**: Weapon systems include a cooldown timer to prevent spamming.
* **Asteroid Physics**:
    * **Spawning**: An `AsteroidField` manages the random spawning of asteroids at the screen edges.
    * **Splitting**: Large asteroids split into two smaller, faster asteroids when hit. Small asteroids are destroyed completely.
* **Game Loop**:
    * Real-time rendering at 60 FPS.
    * Collision detection for Ship vs. Asteroid (Game Over) and Shot vs. Asteroid (Destruction).

## Project Structure

* `main.py`: Entry point handling the game loop and group updates.
* `player.py`: Defines the player ship, handling input (`WASD` + `Space`) and movement physics.
* `asteroid.py`: Logic for asteroid movement and the splitting mechanic upon destruction.
* `shot.py`: Handling for projectiles fired by the player.
* `constants.py`: Central configuration file for game balance (speed, sizes, spawn rates).

## Controls

* **`W` / `S`**: Move Forward / Backward
* **`A` / `D`**: Rotate Left / Right
* **`SPACE`**: Shoot

## Setup & Installation

### 1. Prerequisites
* Python **3.12** or higher.

### 2. Install Dependencies
This project relies on `pygame`.

```bash
pip install pygame
```

### 3. Run the Game
```bash
python main.py
```

## Configuration
You can tweak the game balance and physics by modifying `constants.py`:
* `SCREEN_WIDTH` / `SCREEN_HEIGHT`: Change window size.
* `PLAYER_SPEED` / `PLAYER_TURN_SPEED`: Adjust ship maneuverability.
* `ASTEROID_SPAWN_RATE`: Control how often new hazards appear.
