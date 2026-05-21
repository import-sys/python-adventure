class Animation:
    def __init__(self, frames, duration):
        self.frames = frames
        self.frames_count = len(frames)
        self.current_frame = 0
        self.duration = duration
        self.animation_started = False
        self.time_elapsed = 0
        self.frame_duration = self.duration / self.frames_count

    def play(self, dt):
        if not self.animation_started:
            self.animation_started = True
            self.time_elapsed = 0

        frame_index = self.time_elapsed / self.frame_duration
        frame_index = frame_index % self.frames_count  # <- modulo division
        self.time_elapsed += dt

        return self.frames[int(frame_index)]

    def stop(self):
        self.animation_started = False
        self.time_elapsed = 0
        self.current_frame = 0
