import soundcard as sc
import numpy as np
import time
import warnings
from soundcard import SoundcardRuntimeWarning


def wait_for_sound(*, threshold=None, sample_rate=None, chunk_size=None):
    # Ignore stupid SoundcardRuntimeWarning
    warnings.filterwarnings("ignore", category=SoundcardRuntimeWarning)

    # Get the default speaker's loopback sink
    sink = sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True)

    print("  Listening...")

    with sink.recorder(samplerate=sample_rate) as mic:
        while True:
            # Record a chunk of audio
            data = mic.record(numframes=chunk_size)

            # Convert data to mono by taking the mean across channels (if multi-channel)
            if data.ndim > 1:
                data = np.mean(data, axis=1)

            # Calculate the maximum amplitude in the chunk
            max_amplitude = np.max(np.abs(data))

            # Check if the maximum amplitude exceeds the threshold
            if max_amplitude > threshold:
                print(f"  Sound detected, Amplitude: {max_amplitude:.3f}")
                break

            time.sleep(0.01)
