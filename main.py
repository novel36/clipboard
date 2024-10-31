import subprocess
import time
import pyperclip

def on_clipboard_update(clipboard_content):
  print("Clipboard content changed:", clipboard_content)

# Register the callback function with pyperclip.
pyperclip.waitForNewPaste

# Start monitoring the clipboard.
pyperclip.start()

previous_clipboard_content = None

def on_clipboard_update():
  global previous_clipboard_content

  # Get the new clipboard content.
  clipboard_content = subprocess.check_output(["xclip", "-selection", "clipboard", "-o"], text=True)

  # Only print the new clipboard content if it has changed.
  if clipboard_content != previous_clipboard_content:
    print("Clipboard content changed:", clipboard_content)

    # Update the previous clipboard content.
    previous_clipboard_content = clipboard_content

# Start monitoring the clipboard.
subprocess.Popen(["xclip", "-watch", "-selection", "clipboard"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Wait for the clipboard content to change.
while True:
  time.sleep(1)
  on_clipboard_update()
