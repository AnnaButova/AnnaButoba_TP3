from ui import AnimationMenuWindow
import animator

window = AnimationMenuWindow() # create the window
window.generate_button.clicked.connect(lambda:animator.animate_selected_objects(window)) # connect button to animator function
window.show() # show UI window