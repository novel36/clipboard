import pyperclip
import threading

def notify(callback, error_handler=None):
  """
  Registers a callback function to be called when the clipboard content changes.

  Args:
    callback: A callback function that will be called when the clipboard content changes.
    format: The clipboard format to monitor.
    error_handler: An error handler function that will be called if an error occurs while monitoring the clipboard.
  """

  def _monitor_clipboard():
    try:
      # Get the current clipboard content.
      previous_clipboard_content = pyperclip.paste(format=format)

      # Start monitoring the clipboard.
      while True:
        # Check if the clipboard content has changed.
        current_clipboard_content = pyperclip.paste(format=format)
        if current_clipboard_content != previous_clipboard_content:
          # Call the callback function with the new clipboard content.
          callback(current_clipboard_content)

          # Update the previous clipboard content.
          previous_clipboard_content = current_clipboard_content

        # Wait for 1 second.
        time.sleep(1)
    except Exception as e:
      if error_handler is not None:
        error_handler(e)

  # Create a new thread to monitor the clipboard.
  thread = threading.Thread(target=_monitor_clipboard)
  thread.start()

  # Return a function that can be used to unregister the callback function.




def on_clipboard_update(clipboard_content):
  print("Clipboard content changed:", clipboard_content)

# Register the callback function with pyperclip.
unregister = notify(on_clipboard_update)

# Start monitoring the clipboard.


# Do other things...

# Unregister the callback function.

