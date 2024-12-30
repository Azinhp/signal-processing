import scipy.io.wavfile as wavfile
import signal_processing as sp

def process_wav_signal(input_file):
  """
  Processes a WAV signal file.

  Args:
    input_file: Path to the input WAV file.

  Returns:
    A tuple containing:
      - Sampling rate of the audio.
      - Audio data as a NumPy array.
  """
  try:
    # Load the WAV file
    sampling_rate, data = wavfile.read(input_file)

    return sampling_rate, data 

  except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found.")
    return None, None

if __name__ == "__main__":
  input_wav_file = "D:\uni\NLP\speech_project\salam.wav" 
  sampling_rate, audio_data = process_wav_signal(input_wav_file) 
  print(f"Sampling Rate: {sampling_rate} Hz")

  frame_length = 25 #int(input("Enter the frame length (in samples): "))
  hop_length = 10 #int(input("Enter the hop length (in samples): "))
  window_type = 'hamming' #input("Enter the window type (hann, hamming, etc.): ")
  threshold = 0.2 #float(input("Enter the threshold: "))
 

  frames = sp.framing(audio_data, frame_length, hop_length)

  for frame in frames[::20]: # enter every 20 frames as an input
        windowed_frame = sp.windowing(frame, window_type)
        clipped_frame = sp.center_clipping(windowed_frame, threshold)

        # Calculate and print results
        energy = sp.signal_energy(clipped_frame)
        zero_crossings = sp.zero_crossing_rate(clipped_frame)
        autocorrelation_coeffs = sp.autocorrelation(clipped_frame)


        print(f"Frame energy: {energy}")
        print(f"Zero crossing rate: {zero_crossings}")
        print(f"Autocorrelation coefficients: {autocorrelation_coeffs}")