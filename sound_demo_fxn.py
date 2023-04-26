# co-written by Bard
# Samantha Sun | 2023

import numpy as np
from scipy.signal import butter, filtfilt

def calculate_alpha_power(data, fs=1000, wait_time=2, cutoff_frequency=10, bandwidth=4):
  """Calculates the 8-12 Hz power in the signal across the specified wait time.

  Args:
    data: A time-series streaming dataset.
    fs: The sampling frequency of the data.
    wait_time: The amount of time to wait (in seconds) for data before calculating the power.
    cutoff_frequency: The center frequency of the bandpass filter.
    bandwidth: The bandwidth of the bandpass filter.
    
  Returns:
    The 8-12 Hz power in the signal across the specified wait time.
  """

  # Initialize the data packet window.
  window = []

  # Loop over the data until we have enough data to calculate the power.
  for sample in data:
    # Add the sample to the window.
    window.append(sample)

    # If the window is full, filter the window and calculate the power.
    if len(window) >= wait_time * fs:
      # Convert the window to a NumPy array.
      window = np.array(window)

      # Create a 2nd order Butterworth bandpass filter with the specified cutoff frequency and bandwidth.
      filter_order = 2
      b, a = butter(filter_order, [(cutoff_frequency - bandwidth/2) / (2 * np.pi * fs),(cutoff_frequency + bandwidth/2) / (2 * np.pi * fs)], btype='bandpass', analog=False)

      # Filter the window using filtfilt.
      filtered_window = filtfilt(b, a, window)

      # Calculate the power.
      power = np.sum(filtered_window ** 2)

      # Return the power.
      return power

  # If we don't have enough data to calculate the power, return None.
  return None

def map_to_freq(value, freq_low=200, freq_high=400):
  """Linearly maps a normalized value between [0,1] to the specified frequency range.

  Args:
    value: The normalized value to be mapped.
    freq_low: The lower bound of the mapped range.
    freq_high: The upper bound of the mapped range.

  Returns:
    The mapped frequency value.
  """

  # Calculate the mapped value.
  output_freq = freq_low + (freq_high - freq_low) * value

  # Return the mapped value.
  return output_freq