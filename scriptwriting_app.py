import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import json
import os

class BaseView:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.setup_ui()
        self.hide()

    def setup_ui(self):
        pass

    def show(self):
        self.frame.grid()

    def hide(self):
        self.frame.grid_remove()

class ScriptWriterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Script Writer")
        self.root.geometry("1200x800")
        
        # Configure grid
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        self.create_header()
        self.create_main_content()
        
        # Initialize views
        self.views = {
            'home': HomeView(self.main_content),
            'templates': TemplatesView(self.main_content),
            'library': LibraryView(self.main_content),
            'learning': LearningView(self.main_content),
            'my_stories': MyStoriesView(self.main_content),
            'edit_profile': EditProfileView(self.main_content)
        }
        
        self.show_view('home')

    def create_header(self):
        self.header = ttk.Frame(self.root)
        self.header.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        
        # Logo
        self.logo_label = ttk.Label(self.header, text="Script Writer")
        self.logo_label.pack(side="left", padx=10)
        
        # Navigation tabs
        self.tab_frame = ttk.Frame(self.header)
        self.tab_frame.pack(side="left", expand=True)
        
        tabs = [("Home", "home"), ("Templates", "templates"), 
                ("Library", "library"), ("Learning", "learning")]
        
        for text, view_name in tabs:
            btn = ttk.Button(self.tab_frame, text=text,
                           command=lambda v=view_name: self.show_view(v))
            btn.pack(side="left", padx=5)
        
        # Profile menu
        self.profile_frame = ttk.Frame(self.header)
        self.profile_frame.pack(side="right", padx=10)
        
        self.profile_btn = ttk.Menubutton(self.profile_frame, text="Profile")
        self.profile_btn.pack(side="right")
        
        self.profile_menu = tk.Menu(self.profile_btn, tearoff=0)
        self.profile_btn["menu"] = self.profile_menu
        
        menu_items = [
            ("My Stories", lambda: self.show_view('my_stories')),
            ("Edit Profile", lambda: self.show_view('edit_profile')),
            ("Public Profile", lambda: self.handle_profile_action("public_profile")),
            ("Sign Out", lambda: self.handle_profile_action("sign_out"))
        ]
        
        for label, command in menu_items:
            self.profile_menu.add_command(label=label, command=command)

    def create_main_content(self):
        self.main_content = ttk.Frame(self.root)
        self.main_content.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

    def show_view(self, view_name):
        for view in self.views.values():
            view.hide()
        self.views[view_name].show()

    def handle_profile_action(self, action):
        print(f"Profile action: {action}")

class HomeView(BaseView):
    def setup_ui(self):
        ttk.Label(self.frame, text="Welcome to Script Writer!").pack(pady=20)

class TemplatesView(BaseView):
    def setup_ui(self):
        ttk.Label(self.frame, text="Script Templates").pack(pady=20)

class LibraryView(BaseView):
    def setup_ui(self):
        ttk.Label(self.frame, text="Your Script Library").pack(pady=20)

class LearningView(BaseView):
    def setup_ui(self):
        ttk.Label(self.frame, text="Learning Resources").pack(pady=20)

class EditProfileView(BaseView):
    def setup_ui(self):
        ttk.Label(self.frame, text="Edit Profile").pack(pady=20)

class MyStoriesView(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.story_editor = None

    def setup_ui(self):
        # Main container with sidebar and content area
        self.paned = ttk.PanedWindow(self.frame, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True)

        # Sidebar
        self.sidebar = ttk.Frame(self.paned)
        self.paned.add(self.sidebar)

        # Action buttons
        ttk.Button(self.sidebar, text="+ New Story", 
                  command=self.new_story).pack(fill=tk.X, padx=5, pady=2)
        ttk.Button(self.sidebar, text="Upload Script", 
                  command=self.upload_script).pack(fill=tk.X, padx=5, pady=2)
        ttk.Button(self.sidebar, text="New Folder", 
                  command=self.new_folder).pack(fill=tk.X, padx=5, pady=2)

        # Folder tree
        self.tree = ttk.Treeview(self.sidebar)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Content area
        self.content = ttk.Frame(self.paned)
        self.paned.add(self.content)
        
        # Stories list
        self.stories_list = ttk.Treeview(self.content, columns=("Title", "Modified", "Status"))
        self.stories_list.heading("Title", text="Title")
        self.stories_list.heading("Modified", text="Last Modified")
        self.stories_list.heading("Status", text="Status")
        self.stories_list.pack(fill=tk.BOTH, expand=True)

    def new_story(self):
        if hasattr(self, 'story_editor') and self.story_editor:
            self.story_editor.destroy()
        self.story_editor = StoryEditorView(self.frame)
        self.story_editor.show()

    def upload_script(self):
        filetypes = (
            ("Final Draft", "*.fdx"),
            ("PDF", "*.pdf"),
            ("Open Story Format", "*.osf"),
            ("All files", "*.*")
        )
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            print(f"Uploading: {filename}")

    def new_folder(self):
        print("Creating new folder...")

class StoryEditorView(BaseView):
    def setup_ui(self):
        # Main container
        self.main_container = ttk.Frame(self.frame)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        self.create_top_panel()
        self.create_content_panel()

    def create_top_panel(self):
        # Top panel container
        top_panel = ttk.Frame(self.main_container)
        top_panel.pack(fill=tk.X, pady=5)
        
        # Left section (Back button and story name)
        left_section = ttk.Frame(top_panel)
        left_section.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Button(left_section, text="← Back", command=self.go_back).pack(side=tk.LEFT, padx=5)
        ttk.Label(left_section, text="New Story").pack(side=tk.LEFT, padx=5)
        
        # Right section (View buttons)
        right_section = ttk.Frame(top_panel)
        right_section.pack(side=tk.RIGHT)
        
        view_buttons = [
            ("Home", self.view_home),
            ("Timeline", self.view_timeline),
            ("Cards", self.view_cards),
            ("Page", self.view_page),
            ("Characters", self.view_characters),
            ("Story Stats", self.view_stats),
            ("Slideshow", self.view_slideshow)
        ]
        
        for text, command in view_buttons:
            ttk.Button(right_section, text=text, command=command).pack(side=tk.LEFT, padx=2)
        
        # Options menu
        self.create_options_menu(top_panel)

    def create_options_menu(self):
        # Implementation remains the same as in the previous version...
        pass

    def create_content_panel(self):
        # Implementation remains the same as in the previous version...
        pass

    # View button commands
    def go_back(self): print("Going back...")
    def view_home(self): print("Viewing home...")
    def view_timeline(self): print("Viewing timeline...")
    def view_cards(self): print("Viewing cards...")
    def view_page(self): print("Viewing page...")
    def view_characters(self): print("Viewing characters...")
    def view_stats(self): print("Viewing stats...")
    def view_slideshow(self): print("Viewing slideshow...")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScriptWriterApp(root)
    root.mainloop()