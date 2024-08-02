import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

def start_listening():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Adjust the recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source)
        messagebox.showinfo("Listening", "Speak now...")
        try:
            # Automatically stop listening when the user stops speaking
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            text_area.insert(tk.END, text + "\n")
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            messagebox.showerror("Error", f"Could not request results from Google Speech Recognition service; {e}")
        except sr.WaitTimeoutError:
            messagebox.showinfo("Timeout", "Listening timed out while waiting for phrase to complete")

app = tk.Tk()
app.title("Speech to Text")

frame = tk.Frame(app)
frame.pack(pady=20)

text_area = tk.Text(frame, wrap='word', width=50, height=10)
text_area.pack(pady=20)

listen_button = tk.Button(frame, text="Press and Speak", command=start_listening)
listen_button.pack()

app.mainloop()
