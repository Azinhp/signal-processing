import math
def framing(signal, frame_length, hop_length):
    """
    Segments the signal into overlapping frames.

    Args:
        signal (list): The input signal.
        frame_length (int): The length of each frame.
        hop_length (int): The hop size between frames (overlap).

    Returns:
        list: A list of frames, where each frame is a sublist of the signal.
    """

    frames = []
    for i in range(0, len(signal) - frame_length + 1, hop_length):
        frames.append(signal[i:i + frame_length])
    return frames

def windowing(frame, window_type='hamming'):
    """
    Applies a window function to a frame.

    Args:
        frame (list): The input frame.
        window_type (str, optional): The type of window function to use.
            Defaults to 'hann'. Other options include 'hamming', 'blackman', etc.

    Returns:
        list: The windowed frame.
    """


    if window_type == 'hamming':
        window = [0.54 - 0.46 * math.cos(2 * math.pi * i / (len(frame) - 1)) for i in range(len(frame))]
    # I wish I could add other windowing options but I ran out of time :(
    else:
        raise ValueError(f"Unsupported window type: {window_type}")

    return [frame[i] * window[i] for i in range(len(frame))]

def signal_energy(frame):
    """
    Calculates the energy of a signal frame.

    Args:
        frame (list): The input frame.

    Returns:
        float: The energy of the frame.
    """

    return sum(x**2 for x in frame)

def zero_crossing_rate(frame):
    """
    Calculates the zero-crossing rate of a signal frame.

    Args:
        frame (list): The input frame.

    Returns:
        int: The number of zero crossings in the frame.
    """

    zero_crossings = 0
    for i in range(1, len(frame)):
        if frame[i] * frame[i-1] < 0:
            zero_crossings += 1
    return zero_crossings

def autocorrelation(frame):
    """
    Calculates the autocorrelation coefficients of a signal frame.

    Args:
        frame (list): The input frame.

    Returns:
        list: The autocorrelation coefficients for lags from 0 to frame_length-1.
    """

    autocorrelation_coeffs = [sum(frame[i] * frame[i + lag] for i in range(len(frame) - lag)) for lag in range(len(frame))]
    return autocorrelation_coeffs

def amdf(frame1, frame2):
    """
    Calculates the Average Magnitude Difference Function (AMDF) between two frames.

    Args:
        frame1 (list): The first frame.
        frame2 (list): The second frame.

    Returns:
        float: The minimum value of the AMDF, indicating the time lag of the best match.
    """
    i = 0
    amdf_values = [sum(abs(frame1[i] - frame2[i + lag])) for lag in range(len(frame2))]
    return min(amdf_values)

def center_clipping(frame, threshold):
    """
    Applies center clipping to a signal frame.

    Args:
        frame (list): The input frame.
        threshold (float): The threshold for clipping.

    Returns:
        list: The center-clipped frame.
    """

    return [max(min(x, threshold), -threshold) for x in frame]

