import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Function to upload image
def upload_image():
    global img, img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if img_path:
        img = Image.open(img_path)
        img.thumbnail((400, 400))  # Resize for display
        img_tk = ImageTk.PhotoImage(img)
        panel.config(image=img_tk)
        panel.image = img_tk

# Function to add watermark
def add_watermark():
    global img, img_path
    if not img_path:
        messagebox.showerror("Error", "Please upload an image first.")
        return
    
    watermark_text = watermark_entry.get()
    if not watermark_text:
        messagebox.showerror("Error", "Please enter a watermark text.")
        return
    
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    font = ImageFont.load_default()  # You can also load a custom font using ImageFont.truetype()
    
    # Add watermark text at the bottom-right corner
    textwidth, textheight = draw.textsize(watermark_text, font)
    width, height = img_copy.size
    margin = 10
    position = (width - textwidth - margin, height - textheight - margin)
    draw.text(position, watermark_text, font=font, fill=(255, 255, 255, 128))  # White text with transparency
    
    # Display watermarked image
    img_copy.thumbnail((400, 400))
    img_tk = ImageTk.PhotoImage(img_copy)
    panel.config(image=img_tk)
    panel.image = img_tk
    
    # Ask to save the image
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpeg"), ("JPG files", "*.jpg")])
    if save_path:
        img_copy.save(save_path)
        messagebox.showinfo("Image Saved", f"Watermarked image saved to {save_path}")

# Initialize the GUI
root = tk.Tk()
root.title("Watermark Application")

# UI Elements
panel = tk.Label(root)
panel.pack(pady=20)

upload_btn = tk.Button(root, text="Upload Image", command=upload_image)
upload_btn.pack(pady=10)

watermark_label = tk.Label(root, text="Enter Watermark Text:")
watermark_label.pack(pady=5)

watermark_entry = tk.Entry(root)
watermark_entry.pack(pady=5)

watermark_btn = tk.Button(root, text="Add Watermark", command=add_watermark)
watermark_btn.pack(pady=20)

# Start the application
root.mainloop()