# --- Subsystem Components ---
class Projector:
    def on(self):
        print("Projector: ON")
    def off(self):
        print("Projector: OFF")
    def set_input(self, source):
        print(f"Projector: Input set to {source}")

class DvdPlayer:
    def on(self):
        print("DVD Player: ON")
    def off(self):
        print("DVD Player: OFF")
    def play(self, movie):
        print(f"DVD Player: Playing '{movie}'")
    def stop(self):
        print("DVD Player: Stopped")

class SoundSystem:
    def on(self):
        print("Sound System: ON")
    def off(self):
        print("Sound System: OFF")
    def set_volume(self, level):
        print(f"Sound System: Volume set to {level}")

# --- The Facade ---
class HomeTheaterFacade:
    def __init__(self, projector, dvd_player, sound_system):
        self.projector = projector
        self.dvd_player = dvd_player
        self.sound_system = sound_system

    def watch_movie(self, movie_title):
        print("\n--- Get ready to watch a movie ---")
        self.projector.on()
        self.projector.set_input("DVD")
        self.dvd_player.on()
        self.dvd_player.play(movie_title)
        self.sound_system.on()
        self.sound_system.set_volume(15)
        print("--- Movie started! ---")

    def end_movie(self):
        print("\n--- Shutting down home theater ---")
        self.dvd_player.stop()
        self.dvd_player.off()
        self.projector.off()
        self.sound_system.off()
        print("--- Home theater off ---")

# --- Client Code ---
if __name__ == "__main__":
    # Initialize subsystem components
    my_projector = Projector()
    my_dvd_player = DvdPlayer()
    my_sound_system = SoundSystem()

    # Create the Facade
    home_theater = HomeTheaterFacade(my_projector, my_dvd_player, my_sound_system)

    # Client interacts only with the Facade
    home_theater.watch_movie("The Matrix")
    # ... enjoy the movie ...
    home_theater.end_movie()